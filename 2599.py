# https://www.acmicpc.net/problem/2599
# 짝 정하기

from enum import IntEnum
import copy

class Gender(IntEnum):
    M = 0
    F = 1

class School(IntEnum):
    A = 0
    B = 1
    C = 2

class Combination(IntEnum):
    AB = 0
    AC = 1
    BA = 2
    BC = 3
    CA = 4
    CB = 5

answer = False
n = int(input())
students = []
pairs = [0] * len(Combination)

for i in range(0, 3):
    students.append(list(map(int, input().split())))
    
for i in range(students[School.A][Gender.M] + 1):
	students_copy = copy.deepcopy(students)

	# A학교 남학생과 B학교 여학생 
	if i > students[School.B][Gender.F]:
		break
	pairs[Combination.AB] = i
	students_copy[School.A][Gender.M] -= i
	students_copy[School.B][Gender.F] -= i

	# A학교 남학생과 C학교 여학생 - 여기서 남은 A학교 남학생들이 모두 짝지어 져야 함.
	if students_copy[School.A][Gender.M] > students_copy[School.C][Gender.F]:
		continue
	pairs[Combination.AC] = students_copy[School.A][Gender.M]
	students_copy[School.C][Gender.F] -= students_copy[School.A][Gender.M]
	students_copy[School.A][Gender.M] = 0

	# B학교 남학생과 C학교 여학생 - 여기서 남은 C학교 여학생들이 모두 짝지어 져야 함.
	if students_copy[School.B][Gender.M] < students_copy[School.C][Gender.F]:
		continue
	pairs[Combination.BC] = students_copy[School.C][Gender.F]
	students_copy[School.B][Gender.M] -= students_copy[School.C][Gender.F]
	students_copy[School.C][Gender.F] = 0

	# B학교 남학생과 A학교 여학생 - 여기서 남은 B학교 남학생들이 모두 짝지어 져야 함.
	if students_copy[School.B][Gender.M] > students_copy[School.A][Gender.F]:
		continue
	pairs[Combination.BA] = students_copy[School.B][Gender.M]
	students_copy[School.A][Gender.F] -= students_copy[School.B][Gender.M]
	students_copy[School.B][Gender.M] = 0
	
	# C학교 남학생과 A학교 여학생 - 여기서 남은 A학교 여학생들이 모두 짝지어 져야 함.
	if students_copy[School.C][Gender.M] < students_copy[School.A][Gender.F]:
		continue
	pairs[Combination.CA] = students_copy[School.A][Gender.F]
	students_copy[School.C][Gender.M] -= students_copy[School.A][Gender.F]
	students_copy[School.A][Gender.F] = 0

	# C학교 남학생과 B학교 여학생 - 여기서 남은 C학교 남학생과 B학교 여학생들이 모두 짝지어지면 정답.
	if students_copy[School.B][Gender.F] == students_copy[School.C][Gender.M]:
		pairs[Combination.CB] = students_copy[School.B][Gender.F]
		answer = True
		break


if answer == True:
    print(1)
    print("{} {}".format(pairs[Combination.AB], pairs[Combination.AC]))
    print("{} {}".format(pairs[Combination.BA], pairs[Combination.BC]))
    print("{} {}".format(pairs[Combination.CA], pairs[Combination.CB]))
else:
    print(0)
