#include <stdio.h>

void swap (int *a, int *b);

int main(void) {
    int a=1, b=2;

    printf("%d %d \n", a, b);
    swap(&a, &b);

    printf("%d %d", a, b);
}

void swap (int *a, int *b) {
    int c;
    c = *a;
    *a = *b;
    *b = c;
}