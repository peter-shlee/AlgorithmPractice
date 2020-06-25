#include <cstdio>

int main(void)
{
	int n;
	int nn;
	int count = 0;
	scanf("%d", &n);
	nn = n;

	count += nn / 5;
	nn %= 5;

	count += nn / 3;
	nn %= 3;

	if (!nn) {
		printf("%d\n", count);
	} else {
		count = 0;
		count += n / 3;
		n %= 3;
		if (!n) {
			printf("%d\n", count);
		} else {
			printf("%d\n", -1);
		}
	}

	return 0;
}
