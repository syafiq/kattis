#include "stdio.h"
#include "math.h"

int n;
double atas = 0;
double bawah;
double all;
double out;
int c;

int main(){
    while (!feof(stdin)) {
        scanf("%d", &n);
        if (n == 0){
            break;
        }
        for (c = 1; c <= n; c++){
            atas = atas + log(c);
        }
        out = pow(2.71828182, atas-(n+0.5)*log(n)+n-0.918938533);
        printf("%8.8f\n", out);
        atas = 0;
    }
}