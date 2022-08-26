#include <stdio.h>

int    main(void)
{
    char    c;

    c = 'a';
    printf("%p\n", &c); //0x7ffde11e815b
    c = 'b';
    printf("%p\n", &c); //0x7ffde11e815b
    return (0);
}

int    main(void)
{
    char c;
    void *p;

    c = 'a';
    printf("&c = %p\n", &c); //&c = 0x7ffdfc900ebb
    p = &c;
    printf("p = %p\n", p); //p = 0x7ffdfc900ebb
    *((char *)(p)) = 'b';
    printf("&c = %p\n", &c); //&c = 0x7ffdfc900ebb
    printf("c = %c\n", c); //c = b
    // *(endereço) == conteúdo no endereço
    return (0);
}