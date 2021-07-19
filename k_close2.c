#include <stdio.h>
#include <stdlib.h>


//This is a comment.
//Resolved pulling request.

int* k_close (int * nums, int x, int k, int len) {
 printf("Lens = %d\n", len);
 int left = 0;
 int right = len - k;
 int mid;
 while (left < right) {
  mid = (left + right) / 2;
  if ((x - nums[mid]) > (nums[mid + k] - x)) {
   left = mid + 1;
  }
  else {
   right = mid;
  }
 } 
 printf("Left = %d\n",left);
 printf("num = %d\n",nums);
 return (nums + left);
}

int main() {
 int nums[] = {1,2,3,4,5,6,7,8,9,10,11,12};
 int i;
 int * p;
 printf("num = %d\n",nums);
 p = k_close(nums, 7, 2, sizeof(nums)/sizeof(int));
 printf("num = %d\n",nums);
 printf("*p = %d\n",*p);
 printf("\n");
 for (i = 0;i < 2;i++) {
  printf("%d, ",*(p+i));
 }
 printf("\n");
 return 0;
}
