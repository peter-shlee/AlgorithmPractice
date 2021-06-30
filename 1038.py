# https://www.acmicpc.net/problem/1038
# 감소하는 수

def get_duplicate_digit_index(num: int):
    """중복된 자릿수들 중 뒤에있는 수의 인덱스 리턴하는 함수

    Args:
        num (int): 중복되는 자릿수가 있는지 체크할 수
                여기에 전달되는 숫자는 중복된 자릿수가 한 쌍 밖에 없음이 보장됨
                ex) 1231 (1 두 개가 중복), 16232 (2 두 개가 중복)

    Returns:
        int: 중복된 수 중 뒤에있는 수의 인덱스 리턴
            중복된 수가 없을 경우엔 -1 리턴

    Examples:
        >>> get_duplicate_digit_index(1)
        -1
        >>> get_duplicate_digit_index(11)
        1
        >>> get_duplicate_digit_index(121)
        2
        >>> get_duplicate_digit_index(4321)
        -1
    """     
    digits = list(str(num)) # num의 각 자릿수를 원소로 하는 list 생성
    digit_count = [0] * 10 # 중복된 수가 있는지 확인하는데 사용할 list
    duplitcate_digit_index = -1

    for i, digit in enumerate(digits): # 첫번째 자릿수부터 마지막 자릿수까지 확인
        if digit_count[int(digit)]: # 해당 자릿수의 숫자가 이미 앞에서 나왔던 수라면 (중복된 자릿수라면)
            duplitcate_digit_index = i # index 저장하고
            break # 반복 종료
        else: # 중복 아니라면
            digit_count[int(digit)] += 1 # count + 1

    return duplitcate_digit_index

n = int(input())

if n == 0: # n이 0인 경우는 여기서 따로 처리
    print(0)
    exit()

answer = 1

while True:
    if answer > 9876543210: # 9876543210보다 큰 감소하는 수는 없음
        answer = -1
        break

    i = get_duplicate_digit_index(answer) # 자릿수들 중 중복되는 수가 있는지 확인함
    if i != -1: # 자릿수들 중 중복되는 수가 있다면 -> 감소하는 수가 아니라면
        # 다음으로 확인할 수를 만듦
        digits = list(map(int, str(answer)))
        digits[i] = 0
        digits[i - 1] = digits[i - 1] + 1
        answer = int("".join(list(map(str, digits))))
    else: # 감소하는 수가 맞는 경우
        n -= 1
        if n == 0: # n이 0이면 구하려던 수를 찾은것임
            break
        answer += 1

print(answer)
