// https://www.acmicpc.net/problem/1946
// 신입사원

#include <vector>
#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;

bool compare(const pair<int, int> &a, const pair<int, int> &b) {
	return a.first < b.first;
}

int main() {
    int t, n;
    int document_grade, interview_grade;
	int answer;
    vector<pair<int, int> > applicants;

    scanf("%d", &t);

    for (int i = 0; i < t; ++i){ // test case 수만큼 반복
        scanf("%d", &n);
		applicants.clear(); // 지원자 등수 저장할 vector를 비운다
		answer = 1; // 합격자가 최소 1명 이상이므로 1로 초기화
        for (int j = 0; j < n; ++j){
            scanf("%d%d", &document_grade, &interview_grade); // 각 지원자 등수 입력받음
			applicants.push_back(make_pair(document_grade, interview_grade));
        }

//		for (int j = 0; j < applicants.size(); ++j) {
//			printf("%d, %d\n", applicants[j].first, applicants[j].second);
//		}

		sort(applicants.begin(), applicants.end(), compare); // 서류 심사 등수 기준으로 sorting

		int min_interview_score = applicants[0].second; // 지금까지 나왔던 면접 등수 중 가장 높은 등수 저장
		for (int j = 1; j < applicants.size(); ++j) {
			if (min_interview_score < applicants[j].second) { // 지금까지 나왔던 등수보다 더 높은 등수여야만 합격 가능
				continue;
			} else {
				min_interview_score = applicants[j].second; // 면접 최고 등수 갱신
				++answer; // 합격자수 + 1
			}
		}

		printf("%d\n", answer); // 이번 test case의 답 출력
    }
}
