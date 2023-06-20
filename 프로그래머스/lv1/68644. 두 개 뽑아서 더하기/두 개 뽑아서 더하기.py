def solution(numbers):
    answer = []
        
    for i, j in enumerate(numbers):
        for c, k in enumerate(numbers):
            if j + k not in answer:
                if i != c:
                    answer.append(j+k)
                    
    answer.sort()
        
    return answer