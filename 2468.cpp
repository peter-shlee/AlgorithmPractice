// 안전 영역
// https://www.acmicpc.net/problem/2468

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void print_graph(vector<vector<int> >& graph);
void flood(vector<vector<int> >& graph, int depth);
void dfs(vector<vector<int> >& graph, int r, int c);

int main() {
	int n;
	scanf("%d", &n);

	vector<vector<int> > graph = vector<vector<int> >(n, vector<int>(n, 0));

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			scanf("%d", &graph[i][j]);
		}
	}

	//print_graph(graph);
	int current_depth = 0;
	int answer = 1;
	bool changed_flag = true;
	while (changed_flag) {
		vector<vector<int> > tmp_graph = graph;
		int current_answer = 0;
		changed_flag = false;
		current_depth += 1;
		flood(tmp_graph, current_depth);

		for (int r = 0; r < tmp_graph.size(); ++r) {
			for (int c = 0; c < tmp_graph[r].size(); ++c) {
				if (tmp_graph[r][c] != 0) {
					changed_flag = true;
					current_answer += 1;
					dfs(tmp_graph, r, c);
				}
			}
		}

		answer = max(answer, current_answer);
	}

	printf("%d\n", answer);

	return 0;
}

int adjacent_indices[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; 

bool is_valid_index(vector<vector<int> >& graph, int r, int c) {
	if (r < 0 || c < 0) {
		return false;
	}

	if (graph.size() <= r) {
		return false;
	}

	if (graph[r].size() <= c) {
		return false;
	}

	return true;
}

void dfs(vector<vector<int> >& graph, int r, int c) {
	graph[r][c] = 0;

	for (int i = 0; i < 4; ++i) {
		int next_r = r + adjacent_indices[i][0];
		int next_c = c + adjacent_indices[i][1];

		if (is_valid_index(graph, next_r, next_c)) {
			if (graph[next_r][next_c] != 0) {
				dfs(graph, next_r, next_c);
			}
		}

	}

	return;
}

void flood(vector<vector<int> >& graph, int depth) {
	for (int i = 0; i < graph.size(); ++i) {
		for (int j = 0; j < graph[i].size(); ++j) {
			if (graph[i][j] <= depth) {
				graph[i][j] = 0;
			}
		}
	}

	return;
}

void print_graph(vector<vector<int> >& graph) {
	for (int i = 0; i < graph.size(); ++i) {
		for (int j = 0; j < graph[i].size(); ++j) {
			printf("%d ", graph[i][j]);
		}
		printf("\n");
	}

	return;
}
