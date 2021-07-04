# 팀 프로젝트
# https://www.acmicpc.net/problem/9466

import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    insider = defaultdict(lambda: 0)
    outsider = defaultdict(lambda: 0) ######
    count = 0

    for i in range(len(s)):
        if insider[i] != 0 or outsider[i] != 0: ##### 팀이 있는것을 알아낸 학생, 팀이 없는 것을 알아낸 학생을 확인하고 pass한다
            continue
        team = defaultdict(lambda: 0)
        team2 = []
        current_student = i
        team_flag = False

        while True:
            team[current_student] = 1
            team2.append(current_student)
            current_student = s[current_student] - 1

            if current_student < i:
                break

            if insider[current_student] != 0:
                break

            if current_student == i:
                team_flag = True
                break
            elif team[current_student] != 0: ##### 여기서 발견된 loop를 버리지 말고 기록해 둬야 한다
                idx = team2.index(current_student)
                for student in team2[idx:]:
                    insider[student] = 1
                count += len(team2) - idx

                for student in team2[:idx]: ##### 팀을 이루지 못한 학생들도 기록해둬야 한다
                    outsider[student] = 1
                break

        if team_flag:
            for student in team.keys():
                insider[student] = 1
            count += len(team)

    print(len(s) - count)
