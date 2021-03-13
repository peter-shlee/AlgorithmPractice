#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    long long exp;
    long long answer = 0;
    long long stone_num = 0;
    priority_queue<long long, vector<long long>, greater<long long> > pq;

    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%lld", &exp);
        pq.push(exp);
    }

    while (!pq.empty()) {
        answer += stone_num * (pq.top());
        pq.pop();
        if (stone_num < k){
            ++stone_num;
        }
    }

    printf("%lld\n", answer);

    return 0;
}