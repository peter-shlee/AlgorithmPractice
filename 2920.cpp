#include <cstdio>
#include <vector>
using namespace std;

int main() {
	vector<int> numbers(8);
	bool flag = true;

	for (int i = 0; i < 8; ++i) {
		scanf("%d", &(numbers[i]));
	}

	if (numbers[0] == 1) {
		for (int i = 0; i < 8; ++i) {
			if (numbers[i] != i + 1) {
				flag = false;
				break;
			}
		}
		if (flag) printf("ascending");
	} else if (numbers[0] == 8) {
		for (int i = 0; i < 8; ++i) {
			if (numbers[i] != 8 - i) {
				flag = false;
				break;
			}
		}
		if (flag) printf("descending");
	} else {
		flag = false;
	}
	if (!flag)
		printf("mixed");

	return 0;
}
