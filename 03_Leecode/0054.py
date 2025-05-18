from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 想象一下外围有四条线，也就是遍历顺序
        res = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1  # 左右上下
        while l <= r and t <= b:
            # l -> r
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1

            if t > b: break  # ✅ 防止越界
            # t -> b
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            if l > r: break  # ✅ 防止越界
            # r -> l
            for i in range(r, l -1, -1):
                res.append(matrix[b][i])
            b -= 1

            if t > b: break  # ✅ 防止越界
            # b -> t
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        )
    ]
    for case in cases:
        result = solution.spiralOrder(case[0])
        print(result, case[1])
