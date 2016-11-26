#include <stdio.h>

extern void* _etext;

int main() {
    printf("Hello, World!\n");
    // FIXME: this cause a length violation: printf("_etext = %p\n", _etext);
    return 0;
}
