import sys

number = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

start_index = 0
end_index = number - 1

answer = abs(arr[start_index] + arr[end_index])
start_index_answer = start_index
end_index_answer = end_index

while start_index < end_index :
    now_answer = arr[start_index] + arr[end_index]

    if abs(now_answer) < answer:
        answer = now_answer
        start_index_answer = start_index
        end_index_answer = end_index
        if answer == 0:
            break
        
    if now_answer < 0:
        start_index_answer += 1

    else:
        end_index_answer -= 1

print(start_index_answer, end_index_answer)