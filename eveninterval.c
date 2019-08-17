#include<stdio.h> 

int main(){

           int a,b,rem,i;
           scanf("%d",a);

           scanf("%d",b);

           scanf("%d%d",a,b); 

           for(i=a; i<=b; ++i){

               rem = i % 2;

               if(rem == 0)

               printf("\n  %d",i);

           }

    return 0; 

    } 
