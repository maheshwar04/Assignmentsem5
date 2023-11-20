#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    pid = fork();

    if (pid < 0) {
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (pid == 0) {
        printf("Child with PID: %d\n", getpid());
        while (1) {
        }
    } else {
        printf("Parent with PID: %d\n", getpid());
        while (1) {
        }
    }

    return 0;
}
