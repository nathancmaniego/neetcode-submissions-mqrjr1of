class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p)/ s) # time = distance/speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if the new car takes less time than the car before it then it catches up
                stack.pop()
        return len(stack)