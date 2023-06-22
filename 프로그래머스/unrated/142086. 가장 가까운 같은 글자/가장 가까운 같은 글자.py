def solution(s):
    answer = []
    
    for idx, att in enumerate(s):
            
        cutting = s[:idx]
            
        if att in cutting:
            answer.append(idx - cutting.rindex(att))
        else:
            answer.append(-1)
        
    
    return answer