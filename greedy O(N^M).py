import pytest
from typing import List

def bestMeetingPoint(arr: List[List[int]]) -> int:

    def calCost(arr):
        res = [0]*len(arr)
        for i in range(len(arr)):
            for j in range(len(arr)):
                res[i] += abs(i-j)*arr[j]
        return res

    def costByRow(arr):
        n, m = len(arr), len(arr[0])
        res = [0]*m
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    res[j] += 1
        return calCost(res)
    
    def costByColumn(arr):
        n, m = len(arr), len(arr[0])
        res = [0]*n
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    res[i] += 1
        return calCost(res)

    rowMap = costByRow(arr)
    colMap = costByColumn(arr)
    return min(rowMap) + min(colMap)

# define the test case
tasks = [([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 6), ([[1, 1]], 1)]
@pytest.mark.parametrize("arr, ans", tasks)

def test_fn(arr, ans):
    result = bestMeetingPoint(arr)
    assert result == ans

