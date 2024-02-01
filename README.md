# Algorithm: Best Meeting Point

## Overview
給定一個2D array，array的元素是"0"或"1"。矩陣中的任意一個位置，可以與所有"1"計算出Manhattan Distance距離，此距離最短為多少?
備註: ...

## Features
Brute Force O(N*M*K):
-  窮舉所有2D array的所有位置。(N*M)
    -  加總此位置與所有"1"的距離。(K)

Greedy O(N*M)
-  建構column壓縮數組，並記錄出現的頻率，函數命名colMap (N*M)
    -  arr = [[1, 0, 0, 1], [1, 1, 1, 1]], colMap = [2, 1, 1, 2]
-  建構row壓縮數組，並記錄出現的頻率，函數命名rowMap (N*M)
    -  arr = [[1, 0, 0, 1], [1, 1, 1, 1]], rowMap = [2, 4]
-  距離[i][j] = rowMap[i] + colMap[j]，故min距離 = min(rowMap) + min(colMap)

```python
# PyTest
pytest "brute force O(N^M^K).py"
pytest "greedy O(N^M).py"