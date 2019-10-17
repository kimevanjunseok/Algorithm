# My solution

def solution(arrangement):
    result = 0
    cnt = 0
    S = arrangement.replace('()', '1')

    for i in range(len(S)):
        if S[i] == '(':
            cnt += 1
            result += 1
        elif S[i] == ')':
            cnt += -1
        elif S[i] == '1':
            result += cnt

    return result