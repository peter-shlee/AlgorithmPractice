#include <cstdio>

int main() {
	int E, S, M;

	scanf("%d%d%d", &E, &S, &M);

	for (int i = 1; ; ++i) {
		if (i % 15 == E % 15 && i % 28 == S % 28 && i % 19 == M % 19) {
			printf("%d\n", i);
			break;
		}
	}

	return 0;
}
