
def answ():
  N = int(input())
  apts = list(map(int, input().split()))

  cnt = 0
  for apt in range(2, len(apts) - 2):
    if (
        apts[apt] > apts[apt - 2]
        and apts[apt] > apts[apt - 1]
        and apts[apt] > apts[apt + 1]
        and apts[apt] > apts[apt + 2]
    ):
        first_view = min(
            apts[apt] - apts[apt - 2],
            apts[apt] - apts[apt - 1],
            apts[apt] - apts[apt + 1],
            apts[apt] - apts[apt + 2],
        )
        cnt += first_view
  return cnt

for tc in range(1, 11):
    res = answ()
    print(f"#{tc} {res}")

