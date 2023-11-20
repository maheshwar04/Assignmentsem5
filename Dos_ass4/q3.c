#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void copyFile(char *sourceFileName, char *destinationFileName) {
    FILE *sourceFile = fopen(sourceFileName, "r");
    FILE *destinationFile = fopen(destinationFileName, "w");
    
    if (sourceFile == NULL || destinationFile == NULL) {
        perror("Error opening files");
        exit(EXIT_FAILURE);
    }

    int ch;
    while ((ch = fgetc(sourceFile)) != EOF) {
        fputc(ch, destinationFile);
    }

    fclose(sourceFile);
    fclose(destinationFile);
}

void displayFileContent(char *fileName) {
    FILE *file = fopen(fileName, "r");

    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    int ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
}

void displaySortedReverseFileContent(char *fileName) {
    FILE *file = fopen(fileName, "r");

    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    fseek(file, 0, SEEK_END);
    long pos = ftell(file);

    while (pos > 0) {
        fseek(file, --pos, SEEK_SET);
        int ch = fgetc(file);
        putchar(ch);
    }

    fclose(file);
}

int main() {
    pid_t child1, child2, child3;

    // Creating the first child process
    child1 = fork();
    if (child1 == 0) {
        // First child: copy the content of file1 to file2
        printf("First child: id=%d, parent id=%d\n", getpid(), getppid());
        copyFile("file1.txt", "file2.txt");
        printf("First child completed\n");
        exit(EXIT_SUCCESS);
    }
    usleep(1000000);  // Delay for 1 second

    // Creating the second child process
    child2 = fork();
    if (child2 == 0) {
        // Second child: display the content of file2
        printf("Second child: id=%d, parent id=%d\n", getpid(), getppid());
        displayFileContent("file2.txt");
        printf("Second child completed\n");
        exit(EXIT_SUCCESS);
    }
    usleep(1000000);  // Delay for 1 second

    // Creating the third child process
    child3 = fork();
    if (child3 == 0) {
        // Third child: display the sorted content of file2 in reverse order
        printf("Third child: id=%d, parent id=%d\n", getpid(), getppid());
        displaySortedReverseFileContent("file2.txt");
        printf("Third child completed\n");
        exit(EXIT_SUCCESS);
    }
    usleep(1000000);  // Delay for 1 second

    // Parent process
    printf("Parent process: id=%d\n", getpid());

    // Waiting for all child processes to complete
    wait(NULL);
    wait(NULL);
    wait(NULL);

    printf("All child processes completed\n");

    return 0;
}
