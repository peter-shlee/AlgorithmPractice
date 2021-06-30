#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	int N = 0;

	scanf("%d", &T);

	vector<long long> v = vector<long long>(1000001, 1);
	for (int i = 2; i <= 1000000; ++i) {
		for (int j = 1; i * j <= 1000000; ++j) {
			v[i * j] += i;
		}
	}

	vector<long long> s = vector<long long>(1000001);
	s[0] = 0;
	for (int i = 1; i <= 1000000; ++i) {
		s[i] = s[i - 1] + v[i];
	}

	for (int _ = 0; _ < T; ++_) {
		scanf("%d", &N);
		printf("%lld\n", s[N]);
	}

	return 0;
}
