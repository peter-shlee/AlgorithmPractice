# https://www.acmicpc.net/problem/15947
# 아기 석환 뚜루루 뚜루

song = """baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan"""

words_in_song = song.split()

N = int(input()) - 1 # 인덱스 조정

num_of_times = N // len(words_in_song) # 노래 완곡 횟수
N_word = words_in_song[N % len(words_in_song)] # N번째 단어 구함
if N_word.find("turu") != -1: # "turu"가 포함된 단어라면
    N_word += "ru" * num_of_times # 노래 완곡 횟수만큼 "ru"를 덧붙임

ru_count = N_word.count("ru")
if ru_count >= 5: # "ru"가 5번 이상 반복된다면
    N_word = f"tu+ru*{ru_count}" # “tu+ru*k”와 같이 출력 (k는 "ru"의 반복 횟수)

print(N_word)