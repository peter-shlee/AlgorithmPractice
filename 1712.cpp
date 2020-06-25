#include <cstdio>

int main(void)
{
	int a, b, c;
	int result;
	scanf("%d%d%d", &a, &b, &c);

	if (c == b) result = -1;
	else {
		result = a / (c - b) + 1;
		if (result < 0) result = -1;
	}
	printf("%d\n", result);

	return 0;
}
