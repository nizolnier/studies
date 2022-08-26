#include <stdio.h>

int    main(void)
{
    char    s[] = "NIni\0abobrinha";

    printf("%p\n", &s);// 0x7ffe92d3b97d
    printf("%p\n", s);// 0x7ffe92d3b97d
    printf("%s\n", s);// NIni
    printf("%c\n", *s);// N
    printf("%c\n", *(s + 1));// I
    return (0);
}