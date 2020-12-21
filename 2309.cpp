#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

bool calc(int count, int current_sum, int i);

vector<int> heights;

int main() {
	int height;

	for (int i = 0; i < 9; ++i) {
		scanf("%d", &height);
		heights.push_back(height);
	}
	sort(heights.begin(), heights.end(), greater<int>());

	calc(0, 0, 0);

	return 0;
}

bool calc(int count, int current_sum, int i) {
	
	if (count == 7) {
		if (current_sum == 100) {
			return true;
		} else {
			return false;
		}
	}

	if (current_sum > 100 || i >= 9) return false;

	if (calc(count, current_sum, i + 1)) {
		return true;
	}

	if (calc(count + 1, current_sum + heights[i], i + 1)) {
		printf("%d\n", heights[i]);
		return true;
	}

	return false;
}
