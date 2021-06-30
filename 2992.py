# https://www.acmicpc.net/problem/2992
# 크면서 작은 수

from collections import Counter

def is_same_counter(a: Counter, b: Counter): # 두 Counter의 값이 동일한지 확인하는 함수
    if not isinstance(a, Counter) or not isinstance(b, Counter): # 두 매개변수중 Counter가 아닌 것이 있다면 False 리턴
        return False

    if len(a) != len(b): # 두 Counter의 element 개수가 다르다면 False 리턴
        return False

    for k, v in dict(a).items():
        if b[k] != v:
            return False

    return True
    

input_num = input()
input_num_counter = Counter(input_num)
answer = 0

digit = sum(dict(input_num_counter).values())

cur_check_num = int(input_num) + 1 # 확인할 숫자 생성 (입력된 값부터 1씩 증가시키며 모두 확인)
cur_check_num_counter = Counter(str(cur_check_num)) # 확인할 숫자의 Counter 생성
while (sum(dict(cur_check_num_counter).values())) == digit: # 입력된 수와 확인하는 수가 같은 자릿수일 동안 반복
    if is_same_counter(cur_check_num_counter, input_num_counter): # 두 수의 Counter가 동일한지 확인. 동일하다면 정답임
        answer = cur_check_num # 동일하다면 현재 숫자 저장
        break
    cur_check_num += 1 # 1 증가시켜 다음에 확인할 수로 만듦
    cur_check_num_counter = Counter(str(cur_check_num)) # 다음 확인할 숫자로 Counter 갱신

print(answer)
