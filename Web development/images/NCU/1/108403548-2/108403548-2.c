#include <stdio.h>
#include <stdlib.h>

int
main ()
{
  int a, a1, a2, a3, a4, a5;
  printf ("Enter a integer with 5 digits: ");
  scanf ("%d", &a);
  a1 = a % 10;
  a /= 10;
  a2 = a % 10;
  a /= 10;
  a3 = a % 10;
  a /= 10;
  a4 = a % 10;
  a /= 10;
  a5 = a;
  printf ("%d   %d   %d   %d   %d", a5, a4, a3, a2, a1);
  system ("pause");
  return 0;

}
