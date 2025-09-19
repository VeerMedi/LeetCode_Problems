class Spreadsheet:

    def __init__(self, rows: int):
        self.rows= rows
        self.dict = {}

    def setCell(self, cell: str, value: int) -> None:
        self.dict[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.dict:
            del self.dict[cell]

    def reint(self,a:str) -> int:   
        if a.isdigit():
            return int(a)
        else:
            return self.dict.get(a,0)

    def getValue(self, formula: str) -> int:
        if formula[0] == '=':
            left,right = formula[1:].split('+')
        c= self.reint(left)
        b= self.reint(right)
        return c+b
        
    def reint(self,a:str) -> int:   
        if a.isdigit():
            return int(a)
        else:
            return self.dict.get(a,0)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)