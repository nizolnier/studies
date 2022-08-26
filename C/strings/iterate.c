#include <stdio.h>

int    main(void)
{
    char    s[] = "NIni\0abobrinha";
    int        i = 0;

    printf("%c\n", *s);// N
    printf("%c\n", *(s + 1));// I
    while (s[i] != '\0')
        i++;
    i = 0;
    while (*(s + i) != '\0')
        i++;
    while (*s != '\0')
        s++;
        // s = endereço
        // s + 1 = endereço do próximo caractere
    // s = endereço do '\0'
    return (0);
}