def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]
    # 결과
    # 홀수 - [x:x+1]
    # 짝수 - [x:x+2]

def solution2(s):
    answer = ''
    length = len(s)
    if length % 2 == 0:
        answer = s[length//2-1:length//2+1]
    else:
        answer = s[length//2]
    return answer
