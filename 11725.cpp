#include <cstdio>
#include <vector>
using namespace std;

void dfs(const vector<vector<int> > &t, vector<int> &p, int cur_v, int par_v);

int main() {
	int n, p, s;
	scanf("%d", &n);
	vector<vector<int> > t(n + 1);
	vector<int> par(n + 1);

	for (int i = 1; i < n; ++i) {
		scanf("%d%d", &p, &s);
		t[p].push_back(s);
		t[s].push_back(p);
	}
	dfs(t, par, 1, 0);

	for (int i = 2; i < par.size(); ++i) {
		printf("%d\n", par[i]);
	}

	return 0;
}

void dfs(const vector<vector<int> > &t, vector<int> &p, int cur_v, int par_v) {
	for (int i = 0; i < t[cur_v].size(); ++i) {
		if (t[cur_v][i] == par_v) continue;
		p[t[cur_v][i]] = cur_v;
		dfs(t, p, t[cur_v][i], cur_v);
	}
}
