# Baseball game
# Integer record that score
# + Record sum of two previous two scores 
# D Record double of previous score
# C Invalidate(Remove) previous score

# Input: ["5", "2", "C", "D", "+"]
# Output: 30

def calculate_points_brute(opeartions):
    scores = []
    
    for op in operations:
        if op == "+":
            scores.append(scores[len(scores)-1] + scores[len(scores)-2])
        elif op == "D":
            doubled = scores[-1] * 2
            scores.append(doubled)
        elif op == "C":
            scores = scores[:-1]
        else:
            scores.append(int(op))
    
    return sum(scores)

if __name__ == "__main__":
    operations = ["5", "2", "C", "D", "+"]
    print(calculate_points_brute(operations))
    
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(calculate_points_brute(operations))


