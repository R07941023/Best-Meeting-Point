import pytest
from typing import List

def bestMeetingPoint(arr: List[List[int]]) -> int:

    def findFlags(arr):
        n, m = len(arr), len(arr[0])
        flags = []
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    flags += [[i, j]]
        return flags
    
    n, m = len(arr), len(arr[0])
    flags = findFlags(arr)
    res = (n*m)**2
    for i in range(n):
        for j in range(m):
            curr = 0
            for flag in flags:
                curr += abs(flag[0]-i) + abs(flag[1]-j)
            res = min(res, curr)
    return res

# define the test case
tasks = [([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 6), ([[1, 1]], 1)]
@pytest.mark.parametrize("arr, ans", tasks)

def test_fn(arr, ans):
    result = bestMeetingPoint(arr)
    assert result == ans

