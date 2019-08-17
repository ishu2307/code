#include <stdio.h>
int main()
{
    
    int i,count = 0;
    
    printf("%d", i);
    while(i != 0)
    {
        
        i /= 10;
        ++count;
    }
    scanf(" %d", count);
    return 0;
}
