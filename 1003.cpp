#include <cstdio>
#include <vector>
using namespace std;

vector<int> fib(100, -1);
int get_fib(int n);

int main() {
	int c;
	scanf("%d", &c);

	for (int i = 0; i < c; ++i) {
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("1 0\n");
			continue;
		}
		printf("%d %d\n", get_fib(n - 1), get_fib(n));
	}

	return 0;
}

int get_fib(int n) {
	if (n < 2) return fib[n] = n;

	if (fib[n] != -1) return fib[n];

	return fib[n] = get_fib(n - 1) + get_fib(n - 2);
}
