#include <cstdio>
#include <cmath>

int main() {
	int answer = 0;

	for (int i = 0; i < 5; ++i) {
		int num;
		scanf("%d", &num);
		answer += pow(num, 2);
	}
	answer %= 10;
	printf("%d", answer);

	return 0;
}
