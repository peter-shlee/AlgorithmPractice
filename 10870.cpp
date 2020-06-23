#include <iostream>
using namespace std;

#define BUFFER_SIZE 1024

int fibonacci_buffer[BUFFER_SIZE];

int fibonacci(int n);

int main(void)
{
	int n;

	cin >> n;
	cout << fibonacci(n) << endl;

	return 0;
}

int fibonacci(int n) {
	if (n <= 1) return n;

	if (fibonacci_buffer[n] == 0 && n != 0) {
		fibonacci_buffer[n] = fibonacci(n - 1) + fibonacci(n - 2);
	}
	return fibonacci_buffer[n];
}
