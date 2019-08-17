#include <stdio.h>

 
int main()
{
    int n, j, flag;
 
    
    printf("%d", n);

    flag = 0;
    for (j = 2; j <= n / 2; j++)
    {
        if ((n % j) == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        printf("yes");
     else
        printf("no");
        return 0;
}
