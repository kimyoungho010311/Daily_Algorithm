T = int(input())

for tc in range(1, T+1):
  N = int(input())
  scores = list(map(int, input().split()))
  unique_score = list(set(scores))
  
  # print(unique_score)
  # print(scores.count("8"))

  max_cnt = 0
  max_num = 0
  for i in range(len(unique_score)):
    if max_cnt < scores.count(unique_score[i]):
      max_cnt = scores.count(unique_score[i])
      max_num = unique_score[i]
    elif max_cnt == scores.count(unique_score[i]):
      max_num = max(unique_score[i], max_num)
  print(f"#{tc} {max_num}")


# for tc in range(1, T_1):
#   N = int(input())
#   score_list = [0] * 101
#   scores = list(map(int, input().split()))

#   for score in range(len(scores)):
#     score_list[scores[score]] += 1
#   res = score_list.index(max(score_list))

#   print(f"#{N} {res}")