#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main() {
    
    int sugar = 0;
    int k = 0;
    int a = 1;
    int b = 1;
    int res = 0;
    int i = 0;

    scanf("%d", &sugar);
   
    k = sugar;
    while(1)
    {
        if (sugar % 5 == 0)
         {
        res = sugar / 5;
        i += res;
        break;
         }
    
        sugar -= 3;
        i++;
        if (sugar <0) break;
    }

    if (k!=  res * 5+ (i-res)*3) printf("-1");
    else printf("%d", i);
    return 0;
      
  }