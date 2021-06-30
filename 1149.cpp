#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int get_min_index(const vector<int> &v, int prev);

int main() {
	int n ,answer, next;
	scanf("%d", &n);
	vector<vector<int> > v(n, vector<int>(3));
	vector<vector<int> > a(n, vector<int>(3));
	vector<int> prev(3);

	for (int i = 0; i < n; ++i) {
		scanf("%d%d%d", &(v[i][0]), &(v[i][1]), &(v[i][2]));
	}

	a[0][0] = v[0][0];
	a[0][1] = v[0][1];
	a[0][2] = v[0][2];
	prev[0] = 0;
	prev[1] = 1;
	prev[2] = 2;

	for (int i = 1; i < n; ++i) {
		for (int j = 0; j < 3; ++j) {
			int next_j = get_min_index(v[i], prev[j]);
			a[i][j] = a[i - 1][j] + v[i][next_j];
			prev[j] = next_j;
		}
	}

	answer = min(a[a.size() - 1][0], a[a.size() - 1][1]);
	answer = min(answer, a[a.size() - 1][2]);
	printf("%d\n", answer);

	return 0;
}

int get_min_index(const vector<int> &v, int prev) {
	int min = 987654321;
	int min_index = -1;

	for (int i = 0; i < v.size(); ++i) {
		if (i == prev) continue;

		if (v[i] < min) {
			min = v[i];
			min_index = i;
		}
	}

	return min_index;
}
