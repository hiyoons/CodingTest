def solution(s):
    answer = ''
    s_list=s.split(' ')
    for word in s_list:
        for j in range(len(word)):
            if j%2==0:
                answer+=word[j].upper()
            else:
                answer+=word[j].lower()
        answer+=' '
    return answer[0:-1]