#include <cstdio>
#include <vector>
using namespace std;

vector<int> m(1001, -1);
int calc(int n);

int main() {
	int n;
	scanf("%d", &n);

	printf("%d\n", calc(n));

	return 0;
}

int calc(int n) {
	if (n <= 2) return n;

	if (m[n] != -1) return m[n];
	return m[n] = (calc(n - 1) + calc(n - 2)) % 10007;
}
