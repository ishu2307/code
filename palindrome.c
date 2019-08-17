#include <stdio.h>
int main()
{
    int i, reversedInteger = 0, remainder, originalInteger;
    
    printf("%d", i);
    originalInteger = i;
     
    while( i!=0 )
    {
        remainder = i%10;
        reversedInteger = reversedInteger*10 + remainder;
        i /= 10;
    }
    
    if (originalInteger == reversedInteger)
        printf("yes");
    else
        printf("no");
    
    return 0;
}
