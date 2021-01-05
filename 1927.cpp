#include <cstdio>
#include <set>
using namespace std;

int main() {
	multiset<int> pq;
	int N, x;
	scanf("%d", &N);

	for (int i = 0; i < N; ++i) {
		scanf("%d", &x);
		if (x) {
			pq.insert(x);
		} else {
			auto itr = pq.begin();
			if (itr == pq.end()) {
				printf("0\n");
			} else {
				printf("%d\n", *itr);
				pq.erase(itr);
			}
		}
	}

	return 0;
}
