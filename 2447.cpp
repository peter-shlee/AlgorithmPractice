#include <iostream>
#include <cstdlib>
using namespace std;

bool **map;
int currentX;
int currentY;

void setPattern(int n, int printSpaceFlag);
void printPattern(int n);

int main(void)
{
	int n;
	cin >> n;

	map = new bool *[n];
	for(int i = 0; i < n; ++i) {
		map[i] = new bool[n];
	}

	setPattern(n, 0);
	printPattern(n);

	for(int i = 0; i < n; ++i) {
		delete map[i];
	}
	delete map;

	return 0;
}

void setPattern(int n, int printSpaceFlag) {
	int i, j;
	int count = n / 3;

	if (n == 1) {
		if (printSpaceFlag)
			map[currentX][currentY] = false;
		else
			map[currentX][currentY] = true;

		return;
	}

	for (i = 0; i < 3; ++i) {
		currentX += i * count;
		for (j = 0; j < 3; ++j) {
			currentY += j * count;
			if (i * j == 1) {
				setPattern(n / 3, 1);
				currentY -= j * count;
				continue;
			}
			setPattern(n / 3, printSpaceFlag);
			currentY -= j * count;
		}
		currentX -= i * count;
	}

	return;
}

void printPattern(int n) {
	int i, j;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (map[i][j]) cout << '*';
			else cout << ' ';
		}
		cout << endl;
	}

	return;
}
