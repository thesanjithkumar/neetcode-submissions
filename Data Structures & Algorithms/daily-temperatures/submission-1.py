class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize an array of 0s. This handles the "return 0 if no warmer day" rule automatically.
        res = [0] * len(temperatures)
        
        # The stack will store the INDICES of the days we are waiting to find a warmer temperature for.
        stack = [] 
        
        for i, curr_temp in enumerate(temperatures):
            # While the stack is not empty AND today's temperature is hotter 
            # than the temperature of the index sitting at the top of the stack:
            while stack and curr_temp > temperatures[stack[-1]]:
                # We found a warmer day for the top element!
                prev_day_index = stack.pop()
                
                # Calculate how many days they waited
                res[prev_day_index] = i - prev_day_index
                
            # Add today's index to the stack to wait for a warmer day
            stack.append(i)
            
        return res