// https://www.acmicpc.net/problem/17952
// 과제는 끝나지 않아!
#include <cstdio>
#include <stack>
#include <utility>
using namespace std;

int main() {
	int n;
	int is_new_assignment_comming;
	int new_assignment_time;
	int new_score;
	int score = 0;

	scanf("%d", &n);
	stack<pair<int, int> > assignments; // pair(남은시간, 점수)

	while (n--) {
		scanf("%d", &is_new_assignment_comming);
		if (is_new_assignment_comming) {
			scanf("%d%d", &new_score, &new_assignment_time);
			assignments.push(make_pair(new_assignment_time, new_score));
		}
		if (!assignments.empty()) {
			pair<int, int> &current_assignment = assignments.top();
			--current_assignment.first;
			if (current_assignment.first == 0) {
				score += current_assignment.second;
				assignments.pop();
			}
		}
	}

	printf("%d\n", score);

	return 0;
}
