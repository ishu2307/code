#include<stdio.h>
int main()
{
 char x;
 scanf("%s",&x);
 if(x=='a'||x=='e'||x=='i'||x=='o'||x=='u')
 {
 	printf("vowel");
 	
 }
 else if(x>="a"&&x<="z")
 {
 	printf("consodant");
 }
 else
 {
 	printf("invalid");
 }
}
