class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices
        
        for cur_i, cur_temp in enumerate(temperatures):
            # While current temp is warmer than the temperature at stack's top index
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                # The wait time is the difference between indices
                answer[prev_i] = cur_i - prev_i
                
            # Always push the current day's index onto the stack
            stack.append(cur_i)
            
        return answer