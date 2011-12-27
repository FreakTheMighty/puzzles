
BOARD_WIDTH = 9
BOARD_HEIGHT = 9

GRID_WIDTH = 3
GRID_HEIGHT = 3

class Board(object):

    def __init__(self):

        self._board =[[Cell() for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]
        self._initGrids()
        self._initRows()
        self._initColumns()

    def _initGrids(self):
        self._grids = []
        for row in range(GRID_WIDTH):
            gridRow = []
            for col in range(GRID_HEIGHT):
                gridRow.append(Grid(self,row,col))
            self._grids.append(gridRow)

    def _initRows(self):
        self._rows = []
        for row in range(BOARD_HEIGHT):
            self._rows.append(Row(self,row))

    def _initColumns(self):
        self._columns = []
        for col in range(BOARD_WIDTH):
            self._columns.append(Column(self,col))

    def row(self,row):
        return self._rows[row]

    def column(self,column):
        return self._columns[column]

    def grid(self,row,col):
        return self._grids[row][col]

    def cells(self):
        cells = []
        for row in self._board:
            cells.extend(row)
        return cells

    def cell(self,row,col):
        return self._board[row][col]

    def setCellValue(self,row,col,value):
        cell = self.cell(row,col)
        cell.value = value

    def prettyPrint(self):
        for rIdx, row in enumerate(self._rows):
            cells = row.cells()
            bar ="+========"*len(cells)
            if rIdx % GRID_HEIGHT == 0:
                bar = Color.bold(bar)
            else:
                bar = Color.grey(bar)
            values = ""
            for colIdx, cell in enumerate(cells):
                value = str(cell.value)
                cell = "%s" % value.rjust(8)

                coloredCell = Color.red(cell)

                if colIdx % GRID_WIDTH == 0:
                    values += Color.bold("|")+coloredCell
                else:
                    values += Color.grey("|")+coloredCell

            print Color.bold(bar)
            print values

        print Color.bold(bar)

class Cell(object):

    def __init__(self,row=None,col=None):
        self.row = None
        self.column = None
        self.value = None
        self.board = None

    def __repr__(self):
        if self.row is not None and self.column is not None:
            return "< Sudoku.Cell row=%s, col=%s at %s >"%(int(self.row),int(self.column),id(self))
        else:
            return "< Sudoku.Cell row=%s, col=%s at %s >"%(self.row,self.column,id(self))

class Element(object):

    def values(self):
        return [cell.value for cell in self.cells()]

class Grid(Element):

    def __init__(self,board,row,col):
        self.board = board
        self.row = row
        self.column = col
        for cell in self.cells():
            cell.grid = self

    def __repr__(self):
        return "< Sudoku.Grid row=%s, col=%s at %s >" % (self.row,self.column,id(self))

    def cells(self):
        rows = self.board._board[self.row*GRID_HEIGHT:self.row*GRID_HEIGHT+GRID_HEIGHT]
        cells = []
        for row in rows:
            cells.extend(row[self.column*GRID_WIDTH:self.column*GRID_WIDTH+GRID_WIDTH])
        return cells

class Row(Element):

    def __init__(self,board,row):
        self.board = board
        self.row = row
        for cell in self.cells():
            cell.row = self

    def __repr__(self):
        return "< Sudoku.Grid row=%s at %s >" % (self.row,id(self))

    def __int__(self):
        return self.row

    def cells(self):
        return self.board._board[self.row]

class Column(Element):

    def __init__(self,board,col):
        self.board = board
        self.column = col
        for cell in self.cells():
            cell.column = self

    def __repr__(self):
        return "< Sudoku.Grid col=%s at %s >" % (self.column,id(self))

    def __int__(self):
        return self.column

    def cells(self):
        column = []
        for row in self.board._board:
            column.append(row[self.column])
        return column


class Color(object):

    @staticmethod
    def red(text):
        return "\033[22;31m%s\033[22;30m" % text

    @staticmethod
    def green(text):
        return "\033[22;32m%s\033[22;30m" % text

    @staticmethod
    def blue(text):
        return "\033[22;34m%s\033[22;30m" % text

    @staticmethod
    def grey(text):
        return "\033[22;37m%s\033[22;30m" % text

    @staticmethod
    def bold(text):
        return "\033[1m%s\033[0;0m" % text
