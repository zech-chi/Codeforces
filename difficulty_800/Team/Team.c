#include <stdio.h>

int main()
{
    int n;
    int res = 0;
    int s;
    int can_solve_it;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        s = 0;
        for (int j = 0; j < 3; j++)
        {
            scanf("%d", &can_solve_it);
            s += can_solve_it;
        }
        if (s >= 2)
            res += 1;
    }
    printf("%d", res);
    return (0);
}