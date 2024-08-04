#include <stdio.h>

int countOfHanoi(int num)
{
    if (num == 1)
    {
        return 1;
    }
    else
    {
        return 2 * countOfHanoi(num - 1) + 1;
    }
}

void HanoiTower(int n, int from, int by, int to)
{

    if (n == 1)
    {
        printf("%d %d\n", from, to);
    }
    else
    {
        HanoiTower(n - 1, from, to, by);
        printf("%d %d\n", from, to);

        HanoiTower(n - 1, by, from, to);
    }
}

int main()
{
    int t;
    scanf("%d", &t);

    int cnt = countOfHanoi(t);
    printf("%d\n", cnt);
    HanoiTower(t, 1, 2, 3);

    return 0;
}