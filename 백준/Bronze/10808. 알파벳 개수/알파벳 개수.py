from string import ascii_lowercase

al_list=list(ascii_lowercase)
s=input()
for alphabet in al_list:
    cnt=0
    for word in s:
        if word==alphabet:
            cnt+=1
    print(cnt,end=' ')