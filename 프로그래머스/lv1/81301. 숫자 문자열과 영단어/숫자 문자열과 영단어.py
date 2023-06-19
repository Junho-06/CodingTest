def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, c in enumerate(arr):
        # enumerate는 리스트의 인덱스와 요소를 한번에 사용할 수 있어서 편리함
        s = s.replace(c, str(idx))
    return int(s)