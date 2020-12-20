#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

void getPrimeNumbers(int maxNumber);
void printVector(vector<int> *v);
void goldbach(int num);

vector<int> nums;
vector<int> primes;

int main() {
	int n;
	int i;
	int maxNumber;

	while (true) {
		scanf("%d", &n);
		if (n == 0) {
			break;
		} else {
			nums.push_back(n);
		}
	}
	maxNumber = *max_element(nums.begin(), nums.end());
	getPrimeNumbers(maxNumber);

	for (i = 0; i < nums.size(); ++i) {
		goldbach(nums[i]);
	}

	return 0;
}

void getPrimeNumbers(int maxNumber) {
	int i = 0, j = 0;
	bool primeFlag = false;

	for (i = 3; i <= maxNumber - 3; i += 2) { // 홀수만 체크하면 됨
		primeFlag = true;
		for (j = 3; j <= (int)sqrt(i); j += 2) {
			if (i % j == 0) {
				primeFlag = false;
				break;
			}
		}

		if (primeFlag) {
			primes.push_back(i);
		}
	}
	
	return;
}

void printVector(vector<int> *v) {
	int i = 0;
	printf("print vector :\n");
	for (i = 0; i < v->size(); ++i) {
		printf("%d\n", v->at(i));
	}

	return;
}

void goldbach(int num) {
	int i = 0, j = 0;
	int sum = 0;
	int a = 0, b = 0;
	for (i = 0; i < primes.size(); ++i) {
		for (j = 0; j < primes.size(); ++j) {
			if (b - a > primes[j] - primes[i]) {
				continue;
			}

			sum = primes[i] + primes[j];
			if (sum > num) {
				break;
			} else if (sum == num) {
				a = primes[i];
				b = primes[j];
			}
		}
	}

	printf("%d = %d + %d\n", num, a, b);
}
