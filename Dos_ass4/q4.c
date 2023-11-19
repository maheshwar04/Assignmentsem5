#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

// Function to check if a number is prime
int isPrime(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

// Function to generate Fibonacci series and store it in an array
void generateFibonacci(int length, int *fibonacciArray) {
    int a = 0, b = 1, next;

    for (int i = 0; i < length; i++) {
        fibonacciArray[i] = a;
        next = a + b;
        a = b;
        b = next;
    }
}

int main() {
    int length;
    
    printf("Enter the length of the Fibonacci series: ");
    scanf("%d", &length);

    if (length <= 0) {
        printf("Invalid length. Please enter a positive integer.\n");
        return 1;
    }

    int *fibonacciArray = (int *)malloc(length * sizeof(int));

    pid_t child_pid = fork();

    if (child_pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0) {
        // Child process
        generateFibonacci(length, fibonacciArray);
        printf("Child process completed\n");
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        wait(NULL);

        printf("Parent process:\n");
        printf("Fibonacci Series: ");
        for (int i = 0; i < length; i++) {
            printf("%d ", fibonacciArray[i]);
        }
        printf("\n");

        // Finding and displaying the prime Fibonacci number along with its position
        printf("Prime Fibonacci number: ");
        for (int i = 0; i < length; i++) {
            if (isPrime(fibonacciArray[i])) {
                printf("%d (at position %d)\n", fibonacciArray[i], i + 1);
                break;
            }
        }

        free(fibonacciArray);
    }

    return 0;
}
