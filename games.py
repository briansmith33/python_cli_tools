from colorama import Fore
import colorama
import random
colorama.init(autoreset=True)


class TicTacToe:
    def __init__(self):
        self.option_board = [["1_|", "2_", "|3_"],
                             ["4_|", "5_", "|6_"],
                             ["7 |", "8 ", "|9 "]]

        self.board = [["   ", "   ", "   "],
                      ["   ", "   ", "   "],
                      ["   ", "   ", "   "]]

        self.positions = {
                "1": (0, 0),
                "2": (0, 1),
                "3": (0, 2),
                "4": (1, 0),
                "5": (1, 1),
                "6": (1, 2),
                "7": (2, 0),
                "8": (2, 1),
                "9": (2, 2)
            }

        self.open_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def game_won(self):
        if "".join(self.board[0]) == " X  X  X ":
            self.board[0][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[0][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[0][2] = f"{Fore.CYAN} X {Fore.RESET}"
            return True
        if "".join(self.board[1]) == " X  X  X ":
            self.board[1][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][2] = f"{Fore.CYAN} X {Fore.RESET}"
            return True
        if "".join(self.board[2]) == " X  X  X ":
            self.board[2][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[2][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[2][2] = f"{Fore.CYAN} X {Fore.RESET}"
            return True

        if self.board[0][0] == " X " and self.board[1][0] == " X " and self.board[2][0] == " X ":
            self.board[0][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[2][0] = f"{Fore.CYAN} X {Fore.RESET}"
            return True

        if self.board[0][1] == " X " and self.board[1][1] == " X " and self.board[2][1] == " X ":
            self.board[0][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[2][1] = f"{Fore.CYAN} X {Fore.RESET}"
            return True

        if self.board[0][2] == " X " and self.board[1][2] == " X " and self.board[2][2] == " X ":
            self.board[0][2] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][2] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[2][2] = f"{Fore.CYAN} X {Fore.RESET}"
            return True

        if self.board[0][0] == " X " and self.board[1][1] == " X " and self.board[2][2] == " X ":
            self.board[0][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[2][2] = f"{Fore.CYAN} X {Fore.RESET}"
            return True

        if self.board[2][0] == " X " and self.board[1][1] == " X " and self.board[0][2] == " X ":
            self.board[2][0] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[1][1] = f"{Fore.CYAN} X {Fore.RESET}"
            self.board[0][2] = f"{Fore.CYAN} X {Fore.RESET}"
            return True

        return False

    def game_lost(self):
        if "".join(self.board[0]) == " O  O  O ":
            self.board[0][0] = f"{Fore.RED} O {Fore.RESET}"
            self.board[0][1] = f"{Fore.RED} O {Fore.RESET}"
            self.board[0][2] = f"{Fore.RED} O {Fore.RESET}"
            return True
        if "".join(self.board[1]) == " O  O  O ":
            self.board[1][0] = f"{Fore.RED} O {Fore.RESET}"
            self.board[1][1] = f"{Fore.RED} O {Fore.RESET}"
            self.board[1][2] = f"{Fore.RED} O {Fore.RESET}"
            return True
        if "".join(self.board[2]) == " O  O  O ":
            self.board[2][0] = f"{Fore.RED} O {Fore.RESET}"
            self.board[2][1] = f"{Fore.RED} O {Fore.RESET}"
            self.board[2][2] = f"{Fore.RED} O {Fore.RESET}"
            return True

        if self.board[0][0] == " O " and self.board[1][0] == " O " and self.board[2][0] == " O ":
            self.board[0][0] = f"{Fore.RED} O {Fore.RESET}"
            self.board[1][0] = f"{Fore.RED} O {Fore.RESET}"
            self.board[2][0] = f"{Fore.RED} O {Fore.RESET}"
            return True

        if self.board[0][1] == " O " and self.board[1][1] == " O " and self.board[2][1] == " O ":
            self.board[0][1] = f"{Fore.RED} O {Fore.RESET}"
            self.board[1][1] = f"{Fore.RED} O {Fore.RESET}"
            self.board[2][1] = f"{Fore.RED} O {Fore.RESET}"
            return True

        if self.board[0][2] == " O " and self.board[1][2] == " O " and self.board[2][2] == " O ":
            self.board[0][2] = f"{Fore.RED} O {Fore.RESET}"
            self.board[1][2] = f"{Fore.RED} O {Fore.RESET}"
            self.board[2][2] = f"{Fore.RED} O {Fore.RESET}"
            return True

        if self.board[0][0] == " O " and self.board[1][1] == " O " and self.board[2][2] == " O ":
            self.board[0][0] = f"{Fore.RED} X {Fore.RESET}"
            self.board[1][1] = f"{Fore.RED} X {Fore.RESET}"
            self.board[2][2] = f"{Fore.RED} X {Fore.RESET}"
            return True

        if self.board[2][0] == " O " and self.board[1][1] == " O " and self.board[0][2] == " O ":
            self.board[2][0] = f"{Fore.RED} O {Fore.RESET}"
            self.board[1][1] = f"{Fore.RED} O {Fore.RESET}"
            self.board[0][2] = f"{Fore.RED} O {Fore.RESET}"
            return True

        return False

    def play(self):

        while True:
            for line in self.option_board:
                print("".join(line))
            for line in self.board:
                print("".join(line))
            choice = input("Choose a spot: ")
            if choice not in self.open_spots:
                print("Already taken!")
                continue
            y, x = self.positions[choice]

            self.open_spots.remove(choice)
            self.board[y][x] = "\u0332".join(" X ")

            if self.game_won():
                print("You won!")
                for line in self.board:
                    print("".join(line))
                new_game = input("Play again?(y, n): ")
                if new_game == "y":
                    self.open_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    self.board = [["   ", "   ", "   "],
                             ["   ", "   ", "   "],
                             ["   ", "   ", "   "]]
                    continue
                else:
                    break

            if len(self.open_spots) == 0:
                print("Stalemate!")
                for line in self.board:
                    print("".join(line))
                new_game = input("Play again?(y, n): ")
                if new_game == "y":
                    self.open_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    self.board = [["   ", "   ", "   "],
                             ["   ", "   ", "   "],
                             ["   ", "   ", "   "]]
                    continue
                else:
                    break

            comp_choice = random.choice(self.open_spots)
            comp_y, comp_x = self.positions[comp_choice]
            self.open_spots.remove(comp_choice)
            self.board[comp_y][comp_x] = "\u0332".join(" O ")

            if self.game_lost():
                print("You lost!")
                for line in self.board:
                    print("".join(line))
                new_game = input("Play again?(y, n): ")
                if new_game == "y":
                    self.open_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    self.board = [["   ", "   ", "   "],
                                  ["   ", "   ", "   "],
                                  ["   ", "   ", "   "]]
                    continue
                else:
                    break
