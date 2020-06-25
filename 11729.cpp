#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

void moveHanoiTower(int height, int src, int dst);

int main(void)
{
	int n;
	scanf("%d", &n);
	//cin >> n;

	printf("%d\n", (int)pow(2, n) - 1);
	//cout << pow(2, n) - 1 << endl;
	moveHanoiTower(n, 1, 3);

	return 0;
}

void moveHanoiTower(int height, int src, int dst) {
	int nextDst;

	if (height < 1) return;

	if (src == 1) {
		if (dst == 2) {
			nextDst = 3;
		} else if (dst == 3) {
			nextDst = 2;
		} else {
			return;
		}
	} else if (src == 2) {
		if (dst == 1) {
			nextDst = 3;
		} else if (dst == 3) {
			nextDst = 1;
		} else {
			return;
		}
	} else if (src == 3) {
		if (dst == 1) {
			nextDst = 2;
		} else if (dst == 2) {
			nextDst = 1;
		} else {
			return;
		}
	} else {
		return;
	}

	moveHanoiTower(height - 1, src, nextDst);
	printf("%d %d\n", src, dst);
	//cout << src << ' ' << dst << endl;
	moveHanoiTower(height - 1, nextDst, dst);

	return;
}
