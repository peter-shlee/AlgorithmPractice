#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

void print(multiset<int> &s) {
	for (auto itr = s.begin(); itr != s.end(); ++itr) {
		cout << *itr << ',';
	}
	cout << endl;
}

int main() {
	int T;
	char tmp;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		int delete_count = 0;
		int input_count = 0;
		int k;
		multiset<int> s;
		scanf("%d", &k);
		for (int j = 0; j < k; ++j) {
			char ch;
			int n;
			cin >> ch >> n;

			switch(ch) {
				case 'I':
					s.insert(n);
					break;
				case 'D':
					if (n > 0) {
						auto itr = s.rbegin();
						if (itr != s.rend()) {
							int min = *itr;
							auto itr2 = s.find(min);
							s.erase(itr2);
						}
					} else {
						auto itr = s.begin();
						if (itr != s.end()) {
							s.erase(itr);
						}
					}
					break;
				default:
					break;
			}
			//print(s);
		}

		if (s.empty()) {
			printf("EMPTY\n");
			continue;
		}
		int max, min;
		max = *(s.rbegin());
		min = *(s.begin());

		printf("%d %d\n", max, min);
	}

	return 0;
}
