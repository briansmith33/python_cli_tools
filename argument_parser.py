from collections import namedtuple
from colors import Error
import sys


class Service:
    def __init__(self, name, args=None, version=None, usage=None, description=None):
        self.name = name
        if args is None:
            self.args = {}
        else:
            self.args = args
        self.args[name] = {}
        self.version = version
        self.usage = usage
        self.description = description

    def add_arg(self, flag, dest, type=None, default=None, required=False, help=None):
        if dest is None:
            name = flag.strip('-')
        else:
            name = dest
        self.args[self.name][name] = {
            "flag": flag,
            "type": type,
            "default": default,
            "required": required,
            "help": help
        }

    def parse_args(self, sys_args):
        srvc_args = []
        values = []
        for arg in self.args[self.name].keys():
            flag = self.args[self.name][arg]['flag']
            val_type = self.args[self.name][arg]['type']
            default = self.args[self.name][arg]['default']
            required = self.args[self.name][arg]['required']
            try:
                flag_index = sys_args.index(flag)
            except ValueError:
                if required:
                    Error(f"Flag '{flag}' is required!\n")
                    self.get_help()
                    sys.exit()
                if val_type is bool:
                    value = False
                    values.append(value)
                    srvc_args.append(arg)
                if val_type is int:
                    value = int(default)
                    values.append(value)
                    srvc_args.append(arg)
                if val_type is float:
                    value = float(default)
                    values.append(value)
                    srvc_args.append(arg)
                if val_type is str:
                    value = default
                    values.append(value)
                    srvc_args.append(arg)
                continue

            if val_type is float:
                value = sys_args[flag_index + 1]
                if not value.isnumeric():
                    Error(f"Flag {flag} must be integer!\n")
                    self.get_help()
                    sys.exit()
                value = float(value)

            elif val_type is int:
                value = sys_args[flag_index + 1]
                if not value.isnumeric():
                    Error(f"Flag {flag} must be integer!\n")
                    self.get_help()
                    sys.exit()
                value = int(value)

            elif val_type is bool:
                value = True
            else:
                value = sys_args[flag_index + 1]
                if value.startswith('-') or value.startswith('--'):
                    value = default

            values.append(value)
            srvc_args.append(arg)
        Parsed = namedtuple(self.name, srvc_args)
        return Parsed(*values)

    def get_usage(self):
        if not self.usage:
            usage = ""
            usage += self.name + " "
            for arg in self.args[self.name].keys():
                flag = self.args[self.name][arg]['flag']
                usage += f"[{flag}, {arg}] "
            usage += "[-h, --help]"
            return usage
        return self.usage

    def get_help(self):
        print(f"{self.name} {self.version if self.version is not None else ''}\n")
        print("Usage:", self.get_usage(), "\n")
        print("Options:")
        for flag in self.args[self.name].keys():
            flag_obj = self.args[self.name][flag]
            print(f"\t{flag}: ({flag_obj['type'].__name__ if flag_obj['type'] is not None else ''}) {flag_obj['help']}")


class ArgParser:
    proc_args = None
    args = {}
    services = []

    def __init__(self, name=None, version=None, usage=None, description=None):
        if name is None:
            self.name = sys.argv[0].split('/')[-1]
        else:
            self.name = name
        self.version = version
        self.usage = usage
        self.description = description

    def add_service(self, name, version=None, usage=None, description=None):
        new_serv = Service(name, args=self.args, version=version, usage=usage, description=description)
        self.services.append(new_serv)
        return new_serv

    def add_arg(self, flag, dest=None, type=None, default=None, required=False, help=None):
        if dest is None:
            name = flag.strip('-')
        else:
            name = dest
        self.args[name] = {
            "flag": flag,
            "type": type,
            "default": default,
            "required": required,
            "help": help
        }

    def process_values(self, arg, flag, required, val_type, default, values, srvc_args):
        try:
            flag_index = self.proc_args.index(flag)
        except ValueError:
            if required:
                Error(f"Flag '{flag}' is required!\n")
                self.get_help()
                sys.exit()
            if val_type is bool:
                value = False
                values.append(value)
                srvc_args.append(arg)
            if val_type is int:
                value = int(default)
                values.append(value)
                srvc_args.append(arg)
            if val_type is float:
                value = float(default)
                values.append(value)
                srvc_args.append(arg)
            if val_type is str:
                value = default
                values.append(value)
                srvc_args.append(arg)
            return

        if val_type is float:
            value = self.proc_args[flag_index + 1]
            if not value.isnumeric():
                Error(f"Flag {flag} must be integer!\n")
                self.get_help()
                sys.exit()
            value = float(value)

        elif val_type is int:
            value = self.proc_args[flag_index + 1]
            if not value.isnumeric():
                Error(f"Flag {flag} must be integer!\n")
                self.get_help()
                sys.exit()
            value = int(value)

        elif val_type is bool:
            value = True
        else:
            value = self.proc_args[flag_index + 1]
            if value.startswith('-') or value.startswith('--'):
                value = default

        values.append(value)
        srvc_args.append(arg)

    def parse_args(self, args=None):
        if args is None:
            self.proc_args = sys.argv[1:]
        else:
            self.proc_args = args

        services = []
        service_names = []
        values = []
        if len(services) > 0:
            for service in self.args.keys():
                service_names.append(service)
                srvc_args = []
                for arg in self.args[service].keys():
                    flag = self.args[service][arg]['flag']
                    val_type = self.args[service][arg]['type']
                    default = self.args[service][arg]['default']
                    required = self.args[service][arg]['required']
                    self.process_values(arg, flag, required, val_type, default, values, srvc_args)
                Srvc = namedtuple(service, srvc_args)
                new_service = Srvc(*values)
                services.append(new_service)
            Parsed = namedtuple('Parsed', [*service_names])
            return Parsed(*services)

        srvc_args = []
        for arg in self.args.keys():
            flag = self.args[arg]['flag']
            val_type = self.args[arg]['type']
            default = self.args[arg]['default']
            required = self.args[arg]['required']
            self.process_values(arg, flag, required, val_type, default, values, srvc_args)
        Srvc = namedtuple('Srvc', [*srvc_args])
        return Srvc(*values)

    def get_usage(self):
        if not self.usage:
            usage = ""
            usage += self.name + " "
            for arg in self.args.keys():
                flag = self.args[arg]['flag']
                usage += f"[{flag}, {arg}] "
            usage += "[-h, --help]"
            return usage
        return self.usage

    def get_help(self):
        if self.usage is not None:
            print(f"Usage: {self.usage}")

        if len(self.services) > 0:
            if self.description is not None:
                print(f"Description: {self.description}\n")
            print("Services:")
            for i, service in enumerate(self.args.keys()):
                print(f"\t{service} {self.services[i].version if self.services[i].version is not None else ''}")
                if self.services[i].description:
                    print(f"\tDescription: {self.services[i].description}")
                print(f"\tUsage: {self.services[i].get_usage()}\n")
        else:
            print(f"{self.name} {self.version if self.version is not None else ''}")
            if self.description:
                print(f"Description: {self.description}")
            print(f"Usage:{' python' if self.name.endswith('.py') else ''} {self.get_usage()}\n")