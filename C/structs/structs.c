#include <stdio.h>
#include <stdlib.h>    // malloc, free

typedef struct s_var
{
    char *name;
    int value;
    struct s_var *next;
} t_var;

t_var create_struct(char *name, int value);
t_var* create_struct_pointer(char *name, int value);
void swap_value(t_var *s1, t_var *s2);

int main(void)
{
    t_var st;
    char str[] = "bob";

    st.name = str;
    st.value = 5;
    st.next = NULL;

    printf("%s \n", st.name);

    st = create_struct("bobo", 51);

    printf("%s\n", st.name);

    t_var *st2;
    t_var *st3;

    printf("aaaaaaaaaaaaaaaaaaa");
    st2 = create_struct_pointer("bobobob", 53);
    // *st2 = create_struct("bobobob", 53);
    st3 = create_struct_pointer("bobobob", 54);

    printf("%s\n", st2->name);

    printf("%d\n", st2->value);
    printf("%d\n", st3->value);

    swap_value(st2, st3);

    printf("%d\n", st2->value);
    printf("%d\n", st3->value);

    return (0);
}

t_var create_struct(char *name, int value)
{
    t_var r;

    r.name = name;
    r.value = value;
    r.next = NULL;

    return r;
}

t_var* create_struct_pointer(char *name, int value)
{
    t_var *r;

    r = malloc(sizeof(t_var));

    r->name = name;
    r->value = value;
    r->next = NULL;

    return r;
}

void swap_value(t_var *s1, t_var *s2)
{
    int c = s1->value;

    s1->value = s2->value;
    s2->value = c;
}