#18258 큐
import sys
import queue

input= sys.stdin.readline

n=int(input())
my_queue=queue.Queue()

for _ in range(n):
    command=input()
   
    if ' ' in command:
        parts=command.split()
        number=int(parts[1])
        my_queue.put(number)
       
    elif 'pop' in command:
    
        if my_queue.empty():
            print(-1)
          
        else:
            x=my_queue.get()
            print(x)
            
    elif 'size' in  command:
      
        print(my_queue.qsize())
    elif 'front' in command:
      
        if my_queue.empty():
            print(-1)
        else:
            x=my_queue.queue[0]
            print(x)
    elif 'back' in command:
   
        if my_queue.empty():
            print(-1)
        else:
            x=my_queue.queue[-1]
            print(x)
    elif 'empty' in command:
        if my_queue.empty():
            print(1)
        else:
            print(0)
    else:
        continue