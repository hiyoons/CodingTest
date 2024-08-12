import sys
import queue

input= sys.stdin.readline

n=int(input())
my_queue=queue.Queue()

for i in range(n):
    my_queue.put(i+1)



while my_queue.qsize()>1:
    my_queue.get() #제일 위에 삭제
    next=my_queue.get() # 그 다음 제일 위에 있는 카드 값 가져오기 (삭제 된 값 반환)
    my_queue.put(next) # 제일 위에 있는 카드 제일 아래에 있는 카드 밑으로 옮기기

print(my_queue.get())