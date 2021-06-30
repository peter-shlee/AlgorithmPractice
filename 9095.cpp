#include <cstdio>

void dfs(int n, int target);

int answer = 0;

int main() {
	int t, n;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		answer = 0;
		scanf("%d", &n);
		dfs(0, n);
		printf("%d\n", answer);
	}

	return 0;
}

void dfs(int n, int target) {
	if (n == target) {
		++answer;
		return;
	}
	if (n > target) return;

	dfs(n + 1, target);
	dfs(n + 2, target);
	dfs(n + 3, target);
}
