#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void print_3_dim_vector(const vector<vector<vector<int> > > &v);
void print_2_dim_vector(const vector<vector<int> > &v);
void print_vector(const vector<int> &v);

int main() {
	int n, a;
	scanf("%d", &n);
	vector<int> nums(n);
	vector<vector<vector<int> > > dp(n, vector<vector<int> >(n));

	for (int i = 0; i < n; ++i) {
		scanf("%d", &a);
		nums[i] = a;
	}

	int s = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0, k = i; j < n && k < n; ++j, ++k) {
		}
	}

	print_3_dim_vector(dp);

	return 0;
}

void print_3_dim_vector(const vector<vector<vector<int> > > &v) {
	printf("\n");
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		print_2_dim_vector(*itr);
	}
}


void print_2_dim_vector(const vector<vector<int> > &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		print_vector(*itr);
	}
	printf("\n");
}

void print_vector(const vector<int> &v) {
	printf("[");
	for (int i = 0; i < v.size(); ++i) {
		printf("%d, ", v[i]);
	}
	printf("],\t\t\t");
}

void merge_vector(
