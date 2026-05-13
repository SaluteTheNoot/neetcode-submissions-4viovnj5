class Solution:
    def calPoints(self, operations: List[str]) -> int:

       
        score = []

        for operation in operations:
            if operation == "+":
                first = score[-1]
                second = score[-2]
                score.append(first + second)
            elif operation == "C":
                score.pop()
            elif operation == "D":
                score.append(score[-1]*2)
            else:
                score.append(int(operation))
        
        return sum(score)
            
        