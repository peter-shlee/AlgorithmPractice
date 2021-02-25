#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int init(vector<int> &st, const vector<int> &seq, int left, int right, int index) {
	if (left == right) {
		return st[index] = seq[left];
	}

	int mid = (left + right) / 2;

	return st[index] = init(st, seq, left, mid, index * 2) + init(st, seq, mid + 1, right, index * 2 + 1);
}

int query(const vector<int> &st, const vector<int> &seq, int left, int right, int index, int q_left, int q_right) {
	if (q_right < left || right < q_left) return 0;

	if (q_left <= left && right <= q_right) return st[index];

	int mid = (left + right) / 2;

	return query(st, seq, left, mid, index * 2, q_left, q_right) + query(st, seq, mid + 1, right, index * 2 + 1, q_left, q_right);
}

int main() {
	int seq_len, num_of_question, next_num, q_left, q_right;
	vector<int> seq;

	scanf("%d%d", &seq_len, &num_of_question);

	vector<int> st(4 * seq_len, -1);

	for (int _ = 0; _ < seq_len; ++_) {
		scanf("%d", &next_num);
		seq.push_back(next_num);
	}
	sort(seq.begin(), seq.end());
//	for (int _ = 0; _ < seq_len; ++_) {
//		printf("%d ", seq[_]);
//	}
//	printf("\n");

	init(st, seq, 0, seq.size() - 1, 1);
	
	for (int _ = 0; _ < num_of_question; ++_) {
		scanf("%d%d", &q_left, &q_right);
		printf("%d\n", query(st, seq, 0, seq.size() - 1, 1, q_left - 1, q_right - 1));
	}

	return 0;
}
