from itertools import combinations

card, max = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
r=3


answer=[]
#반복문으로 조합 구하기
def find_combinations(number, r):
  return list(combinations(number, r))
combination_list=find_combinations(number,3)

for i in combination_list:
  answer.append(i[0]+i[1]+i[2])
answer=list(set(answer))
answer.sort()

answer_max=0
j=0
for j in range(len(answer)):
  if answer[j]>max:
    break
  else:
    if answer[j]>answer_max:
      answer_max=answer[j]
print( answer_max)