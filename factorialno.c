#include <stdio.h>
 
int main()
{
  int c, n, fact = 1;
 
  
  printf("%d", &n);
 
  for (c = 1; c <= n; c++)
    fact = fact * c;
 
  printf(" %d = %d\n", n, fact);
 
  return 0;
}
