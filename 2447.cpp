#include <iostream>
using namespace std;

void printPattern(int n, int printSpaceFlag);

int main(void)
{
	int n;
	cin >> n;

	printPattern(n, 0);

	return 0;
}

void printPattern(int n, int printSpaceFlag) {
	int i, j;

	if (n == 1) {
		char c;
		if(printSpaceFlag) c = ' ';
		else c = '*';

		cout << c;
		return;
	}

	for (i = 0; i < 3; ++i) {
		for (j = 0; j < 3; ++j) {
			if (i * j == 1) {
				printPattern(n / 3, 1);
				continue;
			}
			printPattern(n / 3, 0);
		}
		cout << endl;
	}

	return;
}
