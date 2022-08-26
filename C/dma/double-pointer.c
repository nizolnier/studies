#include <stdlib.h>    // malloc, free
#include <stdio.h>    // printf
#include <string.h>    // strdup

char    **make_nini_matrix(void);
void free_nini_string(char*** m);

int    main(void)
{
    char    **m;

    m = make_nini_matrix();
    for (int i = 0; m[i] != NULL; i++)
    {
        printf("m[%i]: %s\n", i, m[i]);
    }

    free_nini_string(&m);
    printf("m = %p\n", m);

    return (0);
}

char    **make_nini_matrix(void)
{
    char *s0;
    char *s1;
    char *s2;
    char **m;

    // m = [s0, s1, s2, NULL]
    s0 = strdup("nickles");
    s1 = strdup("is");
    s2 = strdup("a homie");
    m = malloc(4 * sizeof(char *));
    // m em si: endereço do começo da memória alocada
    *m = s0;
    *(m + 1) = s1;
    m[2] = s2;
    *(m + 3) = NULL;
    return (m);
}

void free_nini_string(char*** n) {
    for(int i = 0; (*n)[i] != NULL; i++) {
        free((*n)[i]);
    }

    free(*n);
    *n = NULL;
}