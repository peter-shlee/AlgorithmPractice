#include <cstdio>
#include <cmath>

int calc(int N, int r, int c);

int main() {
	int N, r, c;
	scanf("%d%d%d", &N, &r, &c);

	printf("%d\n", calc(pow(2, N), r, c));

	return 0;
}

int calc(int N, int r, int c) {
	int next_N = N / 2;
	int answer = 0;

	if (N == 1) return answer;

	if (r < next_N && c < next_N) {
		answer = calc(next_N, r, c);
	} else if (r >= next_N && c < next_N) {
		answer = pow(next_N, 2) * 2 + calc(next_N, r - next_N, c);
	} else if (r < next_N && c >= next_N) {
		answer = pow(next_N, 2) + calc(next_N, r, c - next_N);
	} else {
		answer = pow(next_N, 2) * 3 + calc(next_N, r - next_N, c - next_N);
	}

	return answer;
}

