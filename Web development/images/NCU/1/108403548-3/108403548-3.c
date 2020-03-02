#include <stdio.h>
#include <stdlib.h>

int
main ()
{
  int a, h, m, s;
  printf ("Enter the seconds that had passed:");
  scanf ("%d", &a);
  h = a / 3600;
  a %= 3600;
  m = a / 60;
  a %= 60;
  s = a % 60;
  printf ("%d:%d:%d\n", h, m, s);
  system ("pause");
  return 0;

}
