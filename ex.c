#include <stdio.h>
int main()
{
    int b, ex;
    long long end = 1;
    
    printf("%d", b);

printf("%d", ex);
    while (ex != 0)
    {
        end *= b;
        --ex;
    }
    printf(" %lld", end);
    return 0;
}
