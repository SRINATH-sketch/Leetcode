class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        prev = 0

        for log in logs:
            id, type, time = log.split(":")
            id = int(id)
            time = int(time)

            if type == "start":
                if stack:
                    result[stack[-1]] += time - prev

                stack.append(id)
                prev = time

            else:
                result[stack[-1]] += time - prev + 1
                stack.pop()
                prev = time + 1

        return result