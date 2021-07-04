from collections import deque
from pprint import pprint

class Solution:
    def numIslands(self, grid):
        island_count = 0

        def bfs(u, v):
            q = deque()
            q.append([u, v])

            while q:
                y, x = q.popleft()

                """
                # grid[y][x] = "0"  # 동일 지점 가는 것을 막음
                grid size 가 작을 때는 문제가 없으나, 클 경우에는 병목 현상이 생김
                그리고 시작하는 지점을 굳이 0으로 바꿀 필요는 없다. 연결된 부분이 0이 되면 된다.
                큰 차이가 없어보이는데 이유는 정확히는 모르겠다.
                """

                # y, x에서 상하좌우 이동
                adjacents = [
                    [y, x + 1], [y, x - 1], [y - 1, x], [y + 1, x]
                ]

                for next_y, next_x in adjacents:
                    if next_y < 0 or next_y >= len(grid) or next_x < 0 or next_x >= len(grid[0]) or \
                            grid[next_y][next_x] == "0":
                        # Grid 밖의 영역은 갈 수 없음
                        # 방문 불가능한 지점 설정
                        continue

                    grid[next_y][next_x] = "0"  # 가야 할 지점은 미리 0으로 변경
                    q.append([next_y, next_x])

        # pprint(grid)
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == "1":
                    bfs(j, i)
                    # pprint(grid)
                    island_count += 1

        return island_count



if __name__ == "__main__":
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # grid = [
    #     ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    #     ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    #     ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    #     ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    #     ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #     ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
    # ]
    solution = Solution()
    res = solution.numIslands(grid)
    print(res)






"""
class Solution:
    def numIslands(self, grid):
        island_count = 0

        # pprint(grid)
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == "1":
                    self.bfs(j, i, grid)
                    # pprint(grid)
                    island_count += 1

        return island_count

    def bfs(self, u, v, grid):
        q = deque()
        q.append([u, v])

        while q:
            y, x = q.popleft()

            # y, x에서 상하좌우 이동
            adjacents = [
                [y, x+1], [y, x-1], [y-1, x], [y+1, x]
            ]

            for next_y, next_x in adjacents:
                if next_y < 0 or next_y >= len(grid) or next_x < 0 or next_x >= len(grid[0]) or \
                        grid[next_y][next_x] == "0":
                    # Grid 밖의 영역은 갈 수 없음
                    # 방문 불가능한 지점 설정
                    continue

                grid[next_y][next_x] = "0"  # 동일 지점 가는 것을 막음
                q.append([next_y, next_x])

"""




"""
class Solution:
    def numIslands(self, grid):
        start_vectors = []
        island_count = 0

        for j, component in enumerate(grid):
            for i, value in enumerate(component):
                if value == "1":
                    start_vectors.append([j, i])
        m = j + 1
        n = i + 1

        q = deque()
        visited = [[False for i in range(n)] for j in range(m)]
        distance = [[0 for i in range(n)] for j in range(m)]
        for y, x in start_vectors:
            visited[y][x] = True
            distance[y][x] = 1

        def bfs(u, v):
            q.append([u, v])

            while q:
                y, x = q.popleft()
                visited[y][x] = False # 동일 지점 가는 것을 막음
                # y, x에서 상하좌우 이동
                adjacents = [
                    [y-1, x], [y+1, x], [y, x+1], [y, x-1]
                ]

                for next_y, next_x in adjacents:
                    if next_y < 0 or next_y >= m or next_x < 0 or next_x >= n:
                        # Grid 밖의 영역은 갈 수 없음
                        continue

                    if not visited[next_y][next_x] or grid[next_y][next_x] == "0":
                        # 방문 불가능한 지점 설정
                        continue

                    q.append([next_y, next_x])
                    distance[next_y][next_x] = distance[y][x] + 1

        for y, x in start_vectors:
            if visited[y][x]:
                bfs(y, x)
                island_count += 1

        return island_count
"""