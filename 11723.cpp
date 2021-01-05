#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	int M, n;
	char str[10];
	int s[21] = {0,};
	scanf("%d", &M);

	for (int i = 0; i < M; ++i) {
		scanf("%s", str);
		if (!strcmp(str, "all")) {
			for (int j = 1; j <= 20; ++j) {
				s[j] = 1;
			}
			continue;
		} else if (!strcmp(str, "empty")) {
			for (int j = 1; j <= 20; ++j) {
				s[j] = 0;
			}
			continue;
		}

		scanf("%d", &n);
		if (!strcmp(str, "add")) {
			s[n] = 1;
		} else if (!strcmp(str, "remove")) {
			s[n] = 0;
		} else if (!strcmp(str, "check")) {
			printf("%d\n", s[n]);
		} else if (!strcmp(str, "toggle")) {
			if (s[n]) {
				s[n] = 0;
			} else {
				s[n] = 1;
			}
		}
	}

	return 0;
}
