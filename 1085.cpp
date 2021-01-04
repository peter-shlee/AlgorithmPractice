#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int x, y, w, h;
	int answer = 987654321;
	scanf("%d%d%d%d", &x, &y, &w, &h);

	answer = min(x, y);
	answer = min(answer, w - x);
	answer = min(answer, h - y);

	printf("%d", answer);

	return 0;
}
