import sys
input = sys.stdin.readline

N = int(input())
log = set()
for i in range(N):
    name, commute = input().split()
    if commute == 'enter':
        log.add(name)
    elif commute == 'leave':
        log.remove(name)
        
log_list = list(log)
log_list.sort(reverse=True)
for employee in log_list:
    print(employee)