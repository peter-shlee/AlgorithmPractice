#include <stdio.h>

int main() {
	int a, b;
	int big, small;
	int lcm, gcd;
	int i;
	scanf("%d%d", &a, &b);

	if (a > b) {
		big = a;
		small = b;
	} else {
		big = b;
		small = a;
	}

	i = 1;
	while (i <= small) {
		gcd = small / i;
		if (small % i++ != 0) {
			continue;
		}

		if (big % gcd == 0) {
			break;
		}
	}



	i = 0;
	while (1) {
		lcm = ++i * big;
		if (lcm % small == 0) {
			break;
		}
	}

	printf("%d\n%d\n", gcd, lcm);


	return 0;
}
