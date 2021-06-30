// https://www.acmicpc.net/problem/10999
// 구간 합 구하기 2

#include <cstdio>
#include <vector>
using namespace std;

void print_vector(const vector<long long> &v);
long long init(const vector<long long> &numbers, vector<long long> &tree, int node, int start, int end);
long long update(vector<long long> &tree, vector<long long> &lazy, int node, int start, int end, const int update_start, const int update_end, const long long add_value);
long long query(vector<long long> &tree, vector<long long> &lazy, int current_index, int start, int end, const int query_start, const int query_end);
void propagation(vector<long long> &tree, vector<long long> &lazy, int node, int start, int end);

int main() {
	int n, m, k;
	int input_num;
	int x, y, z;
	scanf("%d%d%d", &n, &m, &k);
	vector<long long> numbers(1, 0);
	vector<long long> seg_tree(n * 4);
	vector<long long> lazy(n * 4, 0);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &input_num);
		numbers.push_back(input_num);
	}

	init(numbers, seg_tree, 1, 1, n);
	// print_vector(seg_tree);
	// print_vector(lazy);

	for (int i = 0; i < m + k; ++i) {
		scanf("%d", &input_num);
		switch (input_num) {
			case 1:
				scanf("%d%d%d", &x, &y, &z);
				update(seg_tree, lazy, 1, 1, n, x, y, z);
				// print_vector(seg_tree);
				// print_vector(lazy);
				break;
			case 2:
				scanf("%d%d", &x, &y);
				// print_vector(seg_tree);
				// print_vector(lazy);
				printf("%lld\n", query(seg_tree, lazy, 1, 1, n, x, y));
				break;
			default:
				break;
		}

	}

	return 0;
}

void print_vector(const vector<long long> &v) {

	printf("\n");
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		printf("%lld ", *itr);
	}
	printf("\n");

	return;
}

long long init(const vector<long long> &numbers, vector<long long> &tree, int node, int start, int end) {
	if (start == end) {
		return tree[node] = numbers[start];
	}

	int middle = (start + end) / 2;

	return tree[node] = init(numbers, tree, 2 * node, start, middle) + init(numbers, tree, 2 * node + 1, middle + 1, end);
}

long long update(vector<long long> &tree, vector<long long> &lazy, int node, int start, int end, const int update_start, const int update_end, const long long add_value) {

	if (update_end < start || end < update_start) {
		return tree[node];
	}

	if (update_start <= start && end <= update_end) {
		lazy[node] += add_value;
		return tree[node] += (end - start + 1) * add_value;
	}

	int middle = (start + end) / 2;
	propagation(tree, lazy, node, start, end);

	return tree[node] = update(tree, lazy, 2 * node, start, middle, update_start, update_end, add_value)
		+ update(tree, lazy, 2 * node + 1, middle + 1, end, update_start, update_end, add_value);

}

long long query(vector<long long> &tree, vector<long long> &lazy, int node, int start, int end, const int query_start, const int query_end) {

	if (query_end < start || end < query_start) {
		return 0;
	}

	if (query_start <= start && end <= query_end) {
		return tree[node];
	}

	int middle = (start + end) / 2;
	propagation(tree, lazy, node, start, end);

	return query(tree, lazy, 2 * node, start, middle, query_start, query_end)
		+ query(tree, lazy, 2 * node + 1, middle + 1, end, query_start, query_end);
}

void propagation(vector<long long> &tree, vector<long long> &lazy, int node, int start, int end) {
	int middle = (start + end) / 2;

	tree[node * 2] += (middle - start + 1) * lazy[node];
	lazy[node * 2] += lazy[node];
	tree[node * 2 + 1] += (end - middle) * lazy[node];
	lazy[node * 2 + 1] += lazy[node];
	lazy[node] = 0;

	return;
}
