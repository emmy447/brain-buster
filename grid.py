import os
import random
import time


class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]  # Creates a size x size grid of Nones
        self.cover_grid = [[True for _ in range(size)] for _ in range(size)]  # Creates a size x size grid of Trues
        self.guess_counter = 0
        self.cheat_counter = 0

    def display(self):
        header = "     " + "  ".join(f"[{chr(65 + column)}]" for column in range(self.size))
        print(header)
        print()

        for row_index, row in enumerate(self.grid):
            formatted_row = "  ".join(
                f"{str(item) if not self.cover_grid[row_index][col_index] else 'X':>3}"
                for col_index, item in enumerate(row)
            )
            print(f"[{row_index}] {formatted_row}")
            print()
        print()

    def index_randomizer(self, element):
        free_positions = [(r,c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] is None]

        if not free_positions:
            return False

        row, column = random.choice(free_positions)
        self.grid[row][column] = element

        return True

    def place_elements(self, elements):
        for element in elements:
            if not self.index_randomizer(element):
                break

    def uncover(self, coordinate):
        column_letter = coordinate[0:len(coordinate)//2]
        column = ord(column_letter.upper()) - 65

        row_string = coordinate[len(coordinate)//2 if len(coordinate)%2 == 0 else ((len(coordinate)//2)+1)]
        row = int(row_string)

        if row < 0 or row > self.size:
            print()
            print("Input error: row entry is out of range for this grid. Please try again.")
            return

        if column < 0 or column > self.size:
            print()
            print("Input error: column entry is out of range for this grid. Please try again.")
            return

        if 0 <= row < self.size and 0 <= column < self.size:
            self.cover_grid[row][column] = False
            self.guess_counter += 2
            self.cheat_counter += 1

        if self.size == 2 and self.cheat_counter == 4:
            print()
            print("You cheated - LOSER!!!!!!!!!!!! You're score is 0!")
        if self.size == 4 and self.cheat_counter == 16:
            print()
            print("You cheated - LOSER!!!!!!!!!!!! You're score is 0!")
        if self.size == 6 and self.cheat_counter == 36:
            print()
            print("You cheated - LOSER!!!!!!!!!!!! You're score is 0!")

    def uncover_pair(self):

        coordinate1 = input("Enter first cell coordinates to uncover (e.g., a0) : ")

        column_letter1 = coordinate1[0:len(coordinate1)//2]
        column1 = ord(column_letter1.upper()) - 65
        row_string1 = coordinate1[len(coordinate1)//2 if len(coordinate1) % 2 == 0 else ((len(coordinate1)//2)+1)]
        row1 = int(row_string1)

        if row1 < 0 or row1 > self.size:
            print()
            print("Input error: row entry is out of range for this grid. Please try again.")
            return

        if column1 < 0 or column1 > self.size:
            print()
            print("Input error: column entry is out of range for this grid. Please try again.")
            return

        coordinate2 = input("Enter second cell coordinates to uncover (e.g., a0) : ")

        column_letter2 = coordinate2[0:len(coordinate2)//2]
        column2 = ord(column_letter2.upper()) - 65
        row_string2 = coordinate2[len(coordinate2)//2 if len(coordinate2) % 2 == 0 else ((len(coordinate2)//2)+1)]
        row2 = int(row_string2)

        if row2 < 0 or row2 > self.size:
            print()
            print("Input error: row entry is out of range for this grid. Please try again.")
            return

        if column2 < 0 or column2 > self.size:
            print()
            print("Input error: column entry is out of range for this grid. Please try again.")
            return

        if coordinate1 == coordinate2:
            print("Please don't input the same coordinate twice.")
            return

        if 0 <= row1 < self.size and 0 <= column1 < self.size and 0 <= row2 < self.size and 0 <= column2 < self.size:
            self.cover_grid[row1][column1] = False
            self.cover_grid[row2][column2] = False

            self.guess_counter += 1

            if self.grid[row1][column1] == self.grid[row2][column2]:
                if self.is_complete():
                    if self.size == 2:
                        score = (2 / self.guess_counter) * 100
                        formated_score = f"{score:.2f}"
                        print()
                        print(f"OH Happy day, You've won!! Your score is: {formated_score}")
                        return
                    elif self.size == 4:
                        score = (8 / self.guess_counter) * 100
                        formated_score = f"{score:.2f}"
                        print()
                        print(f"OH Happy day, You've won!! Your score is: {formated_score}")
                        return
                    elif self.size == 6:
                        score = (18 / self.guess_counter) * 100
                        formated_score = f"{score:.2f}"
                        print()
                        print(f"OH Happy day, You've won!! Your score is: {formated_score}")
                        return

            else:
                self.display()
                print("Try again:(")
                time.sleep(2)
                self.cover_grid[row1][column1] = True
                self.cover_grid[row2][column2] = True
                os.system("clear")

    def uncover_all(self):
        for row in range(self.size):
            for column in range(self.size):
                self.cover_grid[row][column] = False

    def reset_game(self, new_size=None):
        if new_size:
            self.size = new_size
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.cover_grid = [[True for _ in range(self.size)] for _ in range(self.size)]

        if self.size == 2:
            elements = ['1', '1', '2', '2']
        elif self.size == 4:
            elements = ['1', '1', '2', '2','3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8']
        else:
            elements = ['1', '1', '2', '2','3', '3', '4', '4', '5', '5', '6', '6',
                        '7', '7', '8', '8', '9', '9','10','10', '11', '11', '12', '12',
                        '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18', '18']

        for element in elements:
            self.index_randomizer(element)
        self.guess_counter = 0
        self.cheat_counter = 0

    def is_complete(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] is not None and self.cover_grid[row][column] is True:
                    return False
        return True


