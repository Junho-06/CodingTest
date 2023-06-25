import datetime

def solution(a, b):
    answer = ''
    
    weekday_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    weekday_info = datetime.datetime(2016, a, b).weekday()
    
    answer = weekday_list[weekday_info]
    
    return answer