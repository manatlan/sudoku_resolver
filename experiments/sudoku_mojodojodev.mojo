# https://mojodojo.dev/guides/benchmarks/sudoku.html

#INFO: another algo from mojodojo.dev

"""
This is the sudoku solver from here : https://mojodojo.dev/guides/benchmarks/sudoku.html
which resolve the first 100 grids from g_simples.txt ... in less than 2sec

it's a lot faster than my version ;-)
"""

from time import now
from math import sqrt


struct Board[grid_size: Int]:
    var data: DTypePointer[DType.uint8]
    var sub_size: Int
    alias elements = grid_size**2

    fn __init__(inout self, *values: Int) raises:
        "The original one."
        let args_list = VariadicList(values)
        if len(args_list) != grid_size**2:
            raise Error("The amount of elements must be equal to the grid_size parameter squared")

        let sub_size = sqrt(Float64(grid_size))
        if sub_size - sub_size.cast[DType.int64]().cast[DType.float64]() > 0:
            raise Error("The square root of the grid grid_size must be a whole number 9 = 3, 16 = 4")
        self.sub_size = sub_size.cast[DType.int64]().to_int()


        self.data = DTypePointer[DType.uint8].alloc(grid_size**2)
        for i in range(len(args_list)):
            self.data.simd_store[1](i, args_list[i])

    fn __init__(inout self, grid: String) raises:
        "Special version, to undestand grid:String"

        var args_list = DynamicVector[UInt8](81)
        for x in range(len(grid)):
            let c=grid[x]
            if c==".":
                args_list.push_back( 0 )
            else:
                args_list.push_back( ord(c)-48)

        if len(args_list) != grid_size**2:
            raise Error("The amount of elements must be equal to the grid_size parameter squared")

        let sub_size = sqrt(Float64(grid_size))
        if sub_size - sub_size.cast[DType.int64]().cast[DType.float64]() > 0:
            raise Error("The square root of the grid grid_size must be a whole number 9 = 3, 16 = 4")
        self.sub_size = sub_size.cast[DType.int64]().to_int()


        self.data = DTypePointer[DType.uint8].alloc(grid_size**2)
        for i in range(len(args_list)):
            self.data.simd_store[1](i, args_list[i])


    fn __getitem__(self, row: Int, col: Int) -> UInt8:
        return self.data.simd_load[1](row * grid_size + col)

    fn __setitem__(self, row: Int, col: Int, data: UInt8):
        self.data.simd_store[1](row * grid_size + col, data)

    fn print_board(inout self):
        for i in range(grid_size):
            print(self.data.simd_load[grid_size](i * grid_size))

    fn is_valid(self, row: Int, col: Int, num: Int) -> Bool:
        # Check the given number in the row
        for x in range(grid_size):
            if self[row, x] == num:
                return False

        # Check the given number in the col
        for x in range(grid_size):
            if self[x, col] == num:
                return False

        # Check the given number in the box
        let start_row = row - row % self.sub_size
        let start_col = col - col % self.sub_size
        for i in range(self.sub_size):
            for j in range(self.sub_size):
                if self[i+start_row, j+start_col] == num:
                    return False
        return True

    fn solve(self) -> Bool:
        for i in range(grid_size):
            for j in range(grid_size):
                if self[i, j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self[i, j] = num
                            if self.solve():
                                return True
                            # If this number leads to no solution, then undo it
                            self[i, j] = 0
                    return False
        return True

    fn to_string(inout self) -> String:
        return self.data.simd_load[81](0)



def main():

    let buf = open("grids.txt", "r").read()

    let t=now()
    for i in range(100):
        var board = Board[9](buf[i*82:i*82+81])
        board.solve()
        print( board.to_string() )

    print("Took:",(now() - t)/1_000_000_000,"s")