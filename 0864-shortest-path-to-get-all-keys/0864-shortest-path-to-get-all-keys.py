
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = 0

        for row in grid:
            for ch in row:
                if ch.islower():
                    keys += 1

        target = (1 << keys) - 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    start = (r, c)
                    break

        q = deque([(start[0], start[1], 0, 0)])
        visited = {(start[0], start[1], 0)}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, steps = q.popleft()

            if mask == target:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                ch = grid[nr][nc]

                if ch == '#':
                    continue

                if ch.isupper() and not (mask & (1 << (ord(ch.lower()) - ord('a')))):
                    continue

                new_mask = mask

                if ch.islower():
                    new_mask |= 1 << (ord(ch) - ord('a'))

                state = (nr, nc, new_mask)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, new_mask, steps + 1))

        return -1
