#include <iostream>
using namespace std;

int factorial(int n);

int main(void)
{
	int N;
	int N_factorial;

	cin >> N;
	N_factorial = factorial(N);
	cout << N_factorial << endl;

	return 0;
}

int factorial(int n) {
	if (n < 1) return 0;
	if (n == 1) return 1;

	return n * factorial(n - 1);
}
