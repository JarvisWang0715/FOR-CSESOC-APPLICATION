
# include <stdio.h>
# include <stdlib.h>

int main(){
   int a, b, c, min, max;
   printf("Enter three different integers:\n");
   scanf("%d %d %d",&a, &b, &c);
   printf("Sum is %d\n", a+b+c);
   printf("Average is %d\n", (a+b+c)/3);
   printf("Product is %d\n", a*b*c);
   if (a >= b && b >= c)
   {
      min = c;
      max = a;
   }
   if (b >= c && c >= a)
   {
      min = a;
      max = b;
   }
   if (a >= c && c >= b)
   {
      min = b;
      max = a;
   }
   if (c >= a && a >= b)
   {
      min = b;
      max = c;
   }
   if (c >= b && b >= a)
   {
      min = a;
      max = c;
   }
   if (b >= a && a >= c)
   {
      min = c;
      max = b;
   }
   printf("Smallest is %d\n", min);
   printf("Biggest is %d\n", max);
   system("pause");
   return 0;
   
}
