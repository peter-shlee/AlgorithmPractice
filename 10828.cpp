// https://www.acmicpc.net/problem/10828
// 스택

#include <iostream>
#include <stack>
using namespace std;

int main() {
	int n;
	string query;
	int input_num;
	stack<int> s;

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> query;

		if (query == "push") {
			cin >> input_num;
			s.push(input_num);
		} else if (query == "pop") {
			if (!s.empty()) {
				cout << s.top() << endl;
				s.pop();
			} else {
				cout << -1 << endl;
			}
		} else if (query == "top") {
			if (!s.empty()) {
				cout << s.top() << endl;
			} else {
				cout << -1 << endl;
			}
		} else if (query == "size") {
			cout << s.size() << endl;
		} else if (query == "empty") {
			cout << s.empty() << endl;;
		}
	}

	return 0;
}
