#include <stdio.h>

int main() {
	int test_case_count;
	int j;

	scanf("%d", &test_case_count);

	for (j = 0; j < test_case_count; ++j) {
		int A, B;
		int big, small;
		int lcm;
		int i;

		scanf("%d%d", &A, &B);

		if (A > B) {
			big = A;
			small = B;
		} else {
			big = B;
			small = A;
		}

		i = 0;
		while (1) {
			lcm = big * ++i;
			if (lcm % small == 0) {
				break;
			}
		}

		printf("%d\n", lcm);
	}


	return 0;
}
