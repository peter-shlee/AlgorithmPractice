#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

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
		a[i][0] = a[i - 1][0] + min(v[i][1], v[i][2]);
		a[i][1] = a[i - 1][1] + min(v[i][0], v[i][2]);
		a[i][2] = a[i - 1][2] + min(v[i][0], v[i][1]);
	}
	answer = min(a[a.size() - 1][0], a[a.size() - 1][1]);
	answer = min(answer, a[a.size() - 1][2]);
	printf("%d\n", answer);

	return 0;
}
