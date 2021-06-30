#include<cstdio>
#include<vector>
using namespace std;

int main() {
	int s, e;
	scanf("%d%d", &s, &e);
	if (s < 2) s = 2;

	vector<bool> isPrime(e + 1, true);

	for (long long i = 2; i <= e; ++i) {
		if (!isPrime[i]) continue;
		for (long long j = i * i; j <= e; j += i) {
			isPrime[j] = false;
		}
	}

	for (int i = s; i <= e; ++i) {
		if (isPrime[i]) printf("%d\n", i);
	}

	return 0;
}
