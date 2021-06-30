#include <stdio.h>

int main() {
	int test_case_count;
	int j;

	scanf("%d", &test_case_count);

	for (j = 0; j < test_case_count; ++j) {
		int A, B;
		int big, small;
		int gcd;
		int i;

		scanf("%d%d", &A, &B);

		if (A > B) {
			big = A;
			small = B;
		} else {
			big = B;
			small = A;
		}

		i = 1;
		while (i <= small) {
			gcd = small / i;
			if (small % i++ == 0) {
				if (big % gcd == 0) {
					break;
				}
			}
		}

		printf("%d\n", gcd);
	}


	return 0;
}
