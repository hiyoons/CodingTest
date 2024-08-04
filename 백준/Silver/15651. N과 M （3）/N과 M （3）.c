#include <stdio.h>
#include <stdlib.h>

void backTrack(int ar[], int cnt, int n, int m)
{
    if (cnt == m)
    {
        for (int i = 0; i < m; i++)
        {
            printf("%d ", ar[i]);
        }
        printf("\n");
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            ar[cnt] = i + 1;
            backTrack(ar, cnt + 1, n, m);
        }
    }
}

int main()
{
    int n;
    int m;

    scanf("%d %d", &n, &m);

    // 입력 받은 크기만큼 정수형 배열을 동적으로 할당
    int *array = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        array[i] = i + 1;
    }

    backTrack(array, 0, n, m);

    free(array);
    return 0;
}