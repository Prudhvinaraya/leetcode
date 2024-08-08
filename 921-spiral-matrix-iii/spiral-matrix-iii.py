class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i_col = cStart
        i_row = rStart
        ans = [[rStart, cStart]]
        itr=1
        while len(ans) < rows*cols:
            col_itr = False
            row_itr = False

            if itr%2==0:
                reverse = True
            else:
                reverse = False

            while not col_itr or not row_itr:
                j = 0
                while j < itr:
                    if not col_itr:
                        if reverse:
                            i_col -= 1
                        else:
                            i_col += 1
                        j += 1
                        if i_col >= 0 and i_col < cols and i_row >= 0 and i_row < rows:
                            ans.append([i_row, i_col])
                        if j==itr:
                            col_itr = True
                    else:
                        if reverse:
                            i_row -= 1
                        else:
                            i_row += 1
                        j += 1
                        if i_row >= 0 and i_row < rows and i_col >= 0 and i_col < cols:
                            ans.append([i_row, i_col])
                        if j==itr:
                            row_itr = True
            # print(ans)
            itr += 1
        return ans