#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

string str_to_num(string str);
string sum(string a, string b);
string num_to_str(int n);
string calc_comb(int n, int m);
vector<vector<string> > comb(101, vector<string>(101, ""));

int main() {
	int n, m;
	scanf("%d%d", &n, &m);

	cout << str_to_num(calc_comb(n, m)) << endl;

	return 0;
}

string calc_comb(int n, int m) {
	if (m == 1) return comb[n][m] = num_to_str(n);
	if (m == n) return comb[n][m] = "1";

	if (comb[n][m] != "") return comb[n][m];

	return comb[n][m] = sum(calc_comb(n - 1, m - 1) ,calc_comb(n - 1, m));
}

string str_to_num(string str) {
	reverse(str.begin(), str.end());

	return str;
}

string num_to_str(int n) {
	string result = to_string(n);
	reverse(result.begin(), result.end());

	return result;
}

string sum(string a, string b) {
	string result = "";
	int i = 0;
	int o = 0;

	for (; i < a.length() && i < b.length(); ++i) {
		int sum = (a[i] - '0') + (b[i] - '0') + o;
		if (sum >= 10) {
			sum -= 10;
			o = 1;
		} else {
			o = 0;
		}

		result += sum + '0';
	}

	for (; i < a.length(); ++i) {
		int sum = (a[i] - '0') + o;
		if (sum >= 10) {
			sum -= 10;
			o = 1;
		} else {
			o = 0;
		}

		result += sum + '0';
	}
	for (; i < b.length(); ++i) {
		int sum = (b[i] - '0') + o;
		if (sum >= 10) {
			sum -= 10;
			o = 1;
		} else {
			o = 0;
		}

		result += sum + '0';
	}

	if (o) result += o + '0';

	return result;
}

