def solution(food):
    answer = ''
    
    player = ''
    
    for idx, att in enumerate(food):
        player += int(att / 2) * str(idx)
        print(player)
        
    answer += player
    answer += '0' + player[::-1]
    return answer
