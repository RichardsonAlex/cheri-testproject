#include <stdio.h>
#include <unistd.h>
#include <string.h>

extern void* _etext;

int main() {
    write(STDOUT_FILENO, "Hello, World!\n", strlen("Hello, World!\n"));
    // printf("Hello, World!\n");
    // FIXME: this causes a length violation: printf("_etext = %p\n", _etext);
    return 0;
}
