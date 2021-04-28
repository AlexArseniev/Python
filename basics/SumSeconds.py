import math
first_runner_seconds = int(input())
second_runner_second = int(input())
third_runner_second = int(input())
total_time = first_runner_seconds + second_runner_second + third_runner_second
minutes = 0
seconds = 0
if total_time < 60:
    if total_time < 10:
        print(f'{minutes}:0{total_time}')
    else:    
        print(f'{minutes}:{total_time}')
else:
    minutes = math.floor(total_time / 60)
    seconds = total_time - (minutes * 60)
    if seconds < 10:
        print(f'{minutes}:0{seconds}')
    else:
        print(f'{minutes}:{seconds}')
    
