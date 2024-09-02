#include<stdio.h>
#define N 4
void print_binary(int num, int bits) {
    for(int i = bits - 1; i>0; i--) {
        printf("%d", (num>.i)&1);
    }
    printf("\n");
}
void booth_multiplication(int multiplicand, int multiplier) {
    int M = multiplicand;
    int Q = multiplier;
    int Q_1 = 0;
    int A = 0;
    int Q_temp;
    int count = N;
    int mask = (1<<N)-1;
    A &=mask;
    Q &=mask;
    printf("initial value:\n");
    printf("A=");
    print_binary(A,N);
    printf("Q=");
    print_binary(Q,N);
    printf("Q-1=%d\n",Q_1);
    while(count--){
        if(Q&1){
            if(Q_1==0){
                kA=(A-M)&masl
            }
        }
        {
            /* code */
        }
        
    }
}