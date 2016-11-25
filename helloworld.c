#include <stdio.h>

extern void* _etext;

int main() {
    printf("Hello, World %p!\n", _etext);
    return 0;
}
