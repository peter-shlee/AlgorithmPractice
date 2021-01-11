#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	int s;
	int n;
	bool valid;
	char params[100];

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		valid = true;
		s = 0;
		scanf("%s", params);

		for (int j = 0; j < strlen(params); ++j) {
			if (params[j] == '(') {
				++s;
			} else {
				if (s > 0) --s;
				else {
					valid = false;
					break;
				}
			}
		}
		if (s != 0) valid = false;

		if (valid) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}
