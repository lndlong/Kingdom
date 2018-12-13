# Kingdom
#include <stdio.h>
int main(void){
	 int n,i,t;
	 scanf("%d",&n);
	 int a[n];
	 for(i=0;i<n;i++)
	 scanf("%d",&a[i]);
//	 printf("\n");//
//	  for(i=0;i<n;i++)//
//	 printf("a[%d]=%d ",i,a[i]);  //
//	 printf("\n");//
	  if(n%2==0){
	//  	printf("循环偶数");//
	 	for(i=0;i<=n/2;i++){
	 		t = a[i];
	 		a[i] = a[n-i-1];
	 		a[ n -i-1] = t;
	 //		printf("a[i]=%d a[n-i]=%d",a[i],a[n-i]);//
		 }
	} else {
//		 	printf("循环非偶数\n"); //
		for(i=0;i<=(n-1)/2;i++){
		 	t=a[i];
//		 	printf("n-i的值为%d\n",n-i); //
//		 	printf("当i为%d时	t为%d\n",i,t);//
			a[i] = a[n-i-1];
//			printf("当i为%d时	a[i]为%d\n",i,a[i]);//
			a[ n -i-1] = t;
//			printf("当i为%d时	a[n-i]为%d\n",i,a[n-i]);//
			 }
	 	} 
		for(i=0;i<n-1;i++)
			printf("%d ",a[i]);
			printf("%d",a[n-1]);
			return 0;
}
