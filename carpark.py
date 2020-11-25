class carpark:
    def __init__(self, r, c):
        self.grid = []
        self.rows = int(r)
        self.columns = int(c)
        for row in range(0, self.rows):
            self.grid.append([])
            for column in range(0, self.columns):
                self.grid[row].append("empty")

    def display(self):
        print(self.grid)

    def empty(self):
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                self.grid[row][column] = "empty"
        print("Car park is now empty.")

    def park_car(self):
        regNo = input("Enter your car’s registration number: ")
        print("Enter the grid reference that your car has parked at.")
        r = int(input("Row: ")) - 1
        c = int(input("Column: ")) - 1
        while (self.grid[r][c] != "empty") or (r > self.rows or r < 0) or (c > self.columns or c < 0):
            print("Wrong input! Enter the grid reference that your car has parked at:")
            r = input("Row: ")
            c = input("Column: ")
        self.grid[r][c] = regNo
        print("Please park at [", r, "][", c, "].")
        print("You now have a parking space!")

    def remove_car(self):
        found = False
        regNo = input("Enter your car’s registration number: ")
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.grid[row][column] == regNo:
                    self.grid[row][column] = "empty"
        if found:
            print("The space is now empty.")
        else:
            print("The car hasn't been found.")