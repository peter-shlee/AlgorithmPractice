// https://www.acmicpc.net/problem/1764
// 듣보잡

#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
	int n, m;
	set<string> ns;
	set<string> ms;
	string name;

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		cin >> name;
		ns.insert(name);
	}

	for (int i = 0; i < m; ++i) {
		cin >> name;
		ms.insert(name);
	}

	set<string> nms;
	set_intersection(ns.begin(), ns.end(), ms.begin(), ms.end(), inserter(nms, nms.end()));

	cout << nms.size() << endl;
	for (auto itr = nms.begin(); itr != nms.end(); ++itr) {
		cout << *itr << endl;
	}

	return 0;
}
