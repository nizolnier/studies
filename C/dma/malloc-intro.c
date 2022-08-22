#include <stdlib.h>    // malloc, free
#include <stdio.h>    // printf
#include <string.h>    // strlen

char    *make_nini_string(void);

int    main(void)
{
    char    *s;

    s = make_nini_string();
    printf("%s", s);
    free(s);
    return (0);
}

char *make_nini_string(void)
{
    char nini_string[] = "nini";
    char *str;

    str = malloc((strlen(nini_string) + 1) * sizeof(char));

    int i = 0;
    while (nini_string[i] != '\0') {
        str[i] = nini_string[i];
        i++;
    }

    return (str);
}