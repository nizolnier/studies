#include <stdio.h>

int nini_strlen(char *s);

int main(void) {
    char s[] = "NIni\0abobrinha";

    int length = nini_strlen(s);

    printf("%d", length);

    return 0;

}

/* int nini_strlen(char *s) {
    int counter = 0;
    while (*s != '\0') {
        counter++;
        s++;
    }
    
    return counter;
}
 */
int nini_strlen(char *s) {
    char *p = 0;
    p = s;
    while (*s != '\0') {
        s++;
    }
    
    return s-p;
}