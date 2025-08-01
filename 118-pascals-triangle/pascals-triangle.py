class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = []
            c = 1
            for j in range(i+1):    
                row.append(c)
                c = c *(i-j)//(j + 1)
            triangle.append(row)

        return triangle