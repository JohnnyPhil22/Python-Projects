from tkinter import *


# Symbol generation for n columns
# Supports n from 1 to 16 (1-9, A-F)
def make_symbols(n):
    if n < 1 or n > 16:
        raise ValueError("This GUI supports 1 <= n <= 16 (single-character symbols).")
    base = [str(i) for i in range(1, min(n, 9) + 1)]
    if n > 9:
        extra = [chr(ord("A") + k) for k in range(n - 9)]
        base.extend(extra)
    return base


class SolveSudoku:
    def __init__(self, savedNumbers, m, n, sub_m, sub_n, symbols):
        self.savedNumbers = savedNumbers
        self.m = m
        self.n = n
        self.sub_m = sub_m
        self.sub_n = sub_n
        self.symbols = symbols
        self._normalize_empty()
        self._start_solution()

    # Set all non-valid inputs to 0
    def _normalize_empty(self):
        valid = set(self.symbols)
        for i in range(self.m):
            for j in range(self.n):
                val = self.savedNumbers[i][j].get().strip()
                if val not in valid:
                    self.savedNumbers[i][j].set("0")

    # Entry point for the backtracking recursion; fills from top-left
    def _start_solution(self, i=0, j=0):
        i, j = self._find_next_cell_to_fill(i, j)
        if i == -1:
            return True  # No empty cells left => solved

        for sym in self.symbols:
            if self._is_valid(i, j, sym):
                self.savedNumbers[i][j].set(sym)
                if self._start_solution(i, j):
                    return True
                # Backtrack
                self.savedNumbers[i][j].set("0")

        return False

    # Scan from (i,j) to find the next cell with 0
    def _find_next_cell_to_fill(self, i, j):
        for x in range(i, self.m):
            for y in range(j if x == i else 0, self.n):
                if self.savedNumbers[x][y].get() == "0":
                    return x, y

        for x in range(self.m):
            for y in range(self.n):
                if self.savedNumbers[x][y].get() == "0":
                    return x, y

        return -1, -1

    # Check Sudoku constraints for placing 'sym' at (i, j):
    def _is_valid(self, i, j, sym):
        # Row check
        for x in range(self.n):
            if self.savedNumbers[i][x].get() == sym:
                return False

        # Column check
        for x in range(self.m):
            if self.savedNumbers[x][j].get() == sym:
                return False

        # Subgrid check
        start_row = i - (i % self.sub_m)
        start_col = j - (j % self.sub_n)
        for r in range(start_row, start_row + self.sub_m):
            for c in range(start_col, start_col + self.sub_n):
                if self.savedNumbers[r][c].get() == sym:
                    return False

        return True


class Launch:
    def __init__(self, master, m=9, n=9, sub_m=3, sub_n=3):
        # Basic validation
        if m % sub_m != 0 or n % sub_n != 0:
            raise ValueError("m must be divisible by sub_m and n by sub_n.")
        self.master = master
        self.m = m
        self.n = n
        self.sub_m = sub_m
        self.sub_n = sub_n
        self.symbols = make_symbols(n)
        self.valid_set = set(self.symbols)

        # Window setup
        master.title("Sudoku Solver (Generalized)")
        # Width tuning: each Entry ~ 36px wide; keep it compact but readable.
        cell_px = 32
        pad_px = 8
        w = n * cell_px + 2 * pad_px
        h = m * (cell_px + 2) + 70
        master.geometry(f"{max(260, w)}x{max(280, h)}")

        # Build StringVar grid (model)
        self.savedNumbers = [[StringVar(master) for _ in range(n)] for _ in range(m)]

        # Build Entry grid (view)
        # Use single-character width and a readable font.
        font = ("Arial", 16)
        bg = "white"
        self._table = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                e = Entry(
                    master,
                    width=2,
                    font=font,
                    bg=bg,
                    cursor="arrow",
                    borderwidth=0,
                    highlightcolor="yellow",
                    highlightthickness=1,
                    highlightbackground="black",
                    textvariable=self.savedNumbers[i][j],
                    justify="center",
                )
                # Light block borders every subgrid for visual aid
                top = 2 if i % self.sub_m == 0 else 1
                left = 2 if j % self.sub_n == 0 else 1
                e.grid(row=i, column=j, padx=(left, 1), pady=(top, 1))
                e.bind("<KeyRelease>", self._sanitize_inputs)
                e.bind("<FocusOut>", self._sanitize_inputs)
                e.bind("<Button-1>", self._sanitize_inputs)
                self._table[i][j] = e

        # Menu setup
        menu = Menu(master)
        master.config(menu=menu)
        menu.add_command(label="Solve", command=self.solve_input)
        menu.add_command(label="Clear", command=self.clear_all)
        menu.add_command(label="Exit", command=master.quit)

    # Ensure only valid symbols (or empty) remain in the fields
    def _sanitize_inputs(self, event=None):
        for i in range(self.m):
            for j in range(self.n):
                v = self.savedNumbers[i][j].get().strip().upper()
                if v == "":
                    # allow blank; solver will convert to "0"
                    continue
                # only single-char symbols 1..n allowed
                if len(v) != 1 or v not in self.valid_set:
                    self.savedNumbers[i][j].set("")

    # Clear every cell in the grid
    def clear_all(self):
        for i in range(self.m):
            for j in range(self.n):
                self.savedNumbers[i][j].set("")

    # Solve using current grid values.
    def solve_input(self):
        solver = SolveSudoku(
            self.savedNumbers, self.m, self.n, self.sub_m, self.sub_n, self.symbols
        )
        if not solver._start_solution():
            print("No solution exists for the given input.")


if __name__ == "__main__":
    root = Tk()

    m, n = 9, 9
    sub_m, sub_n = 3, 3

    app = Launch(root, m=m, n=n, sub_m=sub_m, sub_n=sub_n)
    root.mainloop()
