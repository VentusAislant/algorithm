"""
    def convert(self, s: str, numRows: int) -> str:
        cur_col = 0
        i = 0
        matrix = [[] for _ in range(numRows)]
        if numRows == 1:
            return ' '.join(s.split()).strip()
        while i < len(s):
            for j in range(numRows):
                if cur_col % (numRows-1) == 0:
                    if i >= len(s):
                        break
                    matrix[j].append(s[i] + ' ')
                    i += 1
                else:
                    matrix[j].append('  ')

            if cur_col % (numRows-1) != 0:
                if i >= len(s):
                    break
                tgt_row = numRows - 1 - cur_col % (numRows-1)
                matrix[tgt_row][cur_col] = s[i] + ' '
                i += 1
            cur_col += 1

        res = ''
        for m in matrix:
            for c in m:
                res += c
            res += '\n'
        return res
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cur_col = 0
        i = 0
        matrix = [[] for _ in range(numRows)]
        if numRows == 1:
            return ' '.join(s.split()).strip()
        while i < len(s):
            for j in range(numRows):
                if cur_col % (numRows-1) == 0:
                    if i >= len(s):
                        break
                    matrix[j].append(s[i])
                    i += 1

            if cur_col % (numRows-1) != 0:
                if i >= len(s):
                    break
                tgt_row = numRows - 1 - cur_col % (numRows-1)
                matrix[tgt_row].append(s[i])
                i += 1
            cur_col += 1
        return  ''.join([c for s in matrix for c in s]).strip()


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
        ('A', 1, 'A')
    ]
    for s, numRows, gt in cases:
        result = solution.convert(s, numRows)
        print(result, gt)
