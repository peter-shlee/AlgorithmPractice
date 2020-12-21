#include <cstdio>
#include <cstdlib>

int main() {
	int n, m;
	int r1, r2;
	int **relations;
	int result;

	scanf("%d%d", &n, &m);
	relations = (int **) malloc(sizeof(int *) * n);
	for (int i = 0; i < n; ++i) {
		relations[i] = (int *) calloc(n, sizeof(int));
	}

	for (int i = 0; i < m; ++i) {
		scanf("%d%d", &r1, &r2);
		relations[r1][r2] = 1;
		relations[r2][r1] = 1;
	}


	return 0;
}
