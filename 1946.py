# https://www.acmicpc.net/problem/1946
# 신입사원

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = []
    answer = 1
    for __ in range(n):
        applicant = list(map(int, input().split()))
        applicants.append(applicant)

    applicants.sort()

    interview_grade_min = applicants[0][1]
    for _, interview_grade in applicants[1:]:
        if interview_grade > interview_grade_min:
            continue
        else :
            interview_grade_min = interview_grade
            answer += 1

    print(answer)
