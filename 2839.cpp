#include <cstdio>

int count = 987654321;

void getCnt(int n, int currentCnt);

int main(void)
{
	int n;
	scanf("%d", &n);

	getCnt(n, 0);
	if (count == 987654321) count = -1;
	printf("%d\n", count);

	return 0;
}

void getCnt(int n, int currentCnt){
	if ((n / 5) + 1 + currentCnt >= count) return;

	if (n == 0) {
		count = currentCnt;
		return;
	}

	if (n - 5 >= 0 && currentCnt + 1 < count)
		getCnt(n - 5, currentCnt + 1);
	if (n - 3 >= 0 && currentCnt + 1 < count)
		getCnt(n - 3, currentCnt + 1);

	return;
}
