#include <stdio.h>
int main()
{
    int y;
        scanf("%d",&y);
    if(y%4 == 0)
    {
        if( y%100 == 0)
        {
            
            if ( y%400 == 0)
                printf("%d yes", y);
            else
                printf("%d  no", y);
        }
        else
            printf("%d yes", y );
    }
    else
        printf("%d not", y);
    
    return 0;
}
