#include <cstdio>
#include <string>
using namespace std;

int main() {
	int num = 0;
	string num_str;

	while (true) {
		scanf("%d", &num);
		if (num == 0) break;

		num_str = to_string(num);
		int flag = true;
		for (int i = 0; i <= num_str.length() / 2; ++i) {
			if (num_str[i] != num_str[num_str.length() - 1 - i]) {
				flag = false;
				break;
			}
		}

		if (flag) printf("yes\n");
		else printf("no\n");
	}

	return 0;
}
