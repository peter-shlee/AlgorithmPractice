#include <cstdio>
#include <cstdlib>
#include <set>
#include <queue>
using namespace std;

void bfs(int **graph, int start_v, int n);
void dfs(int **graph, int v, int n);

queue<int> bfsqueue;
set<int> visited;

int main() {
	int n, m, v;
	int **graph;
	int v1, v2;

	scanf("%d%d%d", &n, &m, &v);

	graph = (int **) malloc(n * sizeof(int *));
	for (int i = 0; i < n; ++i) {
		graph[i] = (int *) calloc(n ,sizeof(int));
	}

	for (int i = 0; i < m; ++i) {
		scanf("%d%d", &v1, &v2);
		graph[v1 - 1][v2 - 1] = 1;
		graph[v2 - 1][v1 - 1] = 1;
	}

	dfs(graph, v - 1, n);
	printf("\n");
	bfs(graph, v - 1, n);

	return 0;
}

void dfs(int **graph, int v, int n) {
	visited.insert(v);
	printf("%d ", v + 1);
	for (int i = 0; i < n; ++i) {
		if (graph[v][i]) {
			if (visited.find(i) == visited.end()) {
				dfs(graph, i, n);
			}
		}
	}
}

void bfs(int **graph, int start_v, int n) {
	int current_v;
	bfsqueue.push(start_v);
	visited.clear();
	visited.insert(start_v);
	
	while (!bfsqueue.empty()) {
		current_v = bfsqueue.front();
		bfsqueue.pop();
		printf("%d ", current_v + 1);
		for (int i = 0; i < n; ++i) {
			if (graph[current_v][i]) {
				if (visited.find(i) == visited.end()) {
					visited.insert(i);
					bfsqueue.push(i);
				}
			}
		}

	}

	printf("\n");
}
