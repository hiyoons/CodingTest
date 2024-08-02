#include <stdio.h>

long long factorial(int n)
{
    if (n == 1 || n == 0)
        return 1;

    else
        return n * factorial(n - 1);
}

int main(void)
{

    int n;
    scanf("%d", &n);

    printf("%lld",factorial(n));

    return 0;
}