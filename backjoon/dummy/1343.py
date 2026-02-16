board = input()

# 사전순으로 변환해야 하기 떄문에 먼저 AAAA로 변환한다.
board = board.replace("XXXX", "AAAA")
# 변환되지 못한 XX 들은 BB로 변환된다.
board = board.replace("XX", "BB")

# 만약 보드 안에 X가 남아있다면 그건 변환하지 못하는 경우의 수 이므로
if 'X' in board:
  print(-1) # -1 출력
else:
  print(board)