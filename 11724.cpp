#include <cstdio>
#include <vector>
using namespace std;

void check(vector<vector<int> > &g, int v);

int main() {
	int n, m;
	int answer = 0;
	scanf("%d%d", &n, &m);
	vector<vector<int> > g(n + 1, vector<int>(n + 1, 0));

	for (int i = 1; i < g.size(); ++i) {
		g[i][i] = 1;
	}

	for (int i = 0; i < m; ++i) {
		int u, v;
		scanf("%d%d", &u, &v);
		g[u][v] = 1;
		g[v][u] = 1;
	}

	for (int i = 1; i < g.size(); ++i) {
		for (int j = 0; j < g[i].size(); ++j) {
			if (g[i][j]) {
				++answer;
				check(g, j);
			}
		}
	}

	printf("%d\n", answer);

	return 0;
}

void check(vector<vector<int> > &g, int v) {

	for (auto itr = g.begin(); itr != g.end(); ++itr) {
		itr->at(v) = 0;
	}

	for (int i = 0; i < g[v].size(); ++i) {
		if (g[v][i]) {
			check(g, i);
		}
	}

}
