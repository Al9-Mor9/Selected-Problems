import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(r, c):
    if p[r][c] != (r, c):
        nr, nc = p[r][c]
        p[r][c] = find(nr, nc)
    return p[r][c]


def solution(commands):

    global p

    ans = []
    table = [[0] * 51 for _ in range(51)]
    p = [[(r, c) for c in range(51)] for r in range(51)]

    for command in commands:
        ql = list(command.split())
        query = ql[0]

        if query == 'UPDATE':
            if len(ql) == 4:
                r, c, v = int(ql[1]), int(ql[2]), ql[3]
                root = find(r, c)

                for i in range(51):
                    for j in range(51):
                        if find(i, j) == root:
                            table[i][j] = v

            else:
                v1, v2 = ql[1:]
                for i in range(51):
                    for j in range(51):
                        r, c = find(i, j)

                        if table[r][c] == v1:
                            table[r][c] = v2

        elif query == 'MERGE':
            r1, c1, r2, c2 = map(int, ql[1:])

            r1 ,c1 = find(r1, c1)
            r2 ,c2 = find(r2, c2)

            if [r1 ,c1] == [r2 ,c2]: continue # 이미 같은 유니온이면 넘어간다.

            p[r2][c2] = (r1, c1) # 임의로 r2, c2의 부모를 r1, c1으로 넘겨주자.
            v = table[r1][c1] if table[r1][c1] else table[r2][c2] # 합치고 남길 값 설정.

            for i in range(51):
                for j in range(51):
                    if find(i, j) == (r1, c1):
                        table[i][j] = v

        elif query == 'UNMERGE':
            r, c = map(int, ql[1:])
            root = find(r, c)
            v = table[root[0]][root[1]]

            for i in range(51):
                for j in range(51):
                    if find(i, j) == root:
                        p[i][j] = (i, j)
                        if (i, j) != (r, c):
                            table[i][j] = 0 
            table[r][c] = v

        elif query == "PRINT":
            r, c = map(int, ql[1:])
            r1, c1 = find(r, c)
            v = table[r1][c1]
            ans.append('EMPTY' if not v else v)

    return ans

co = ["UPDATE 1 1 menu", 
      "UPDATE 1 2 category", 
      "UPDATE 2 1 bibimbap", 
      "UPDATE 2 2 korean", 
      "UPDATE 2 3 rice", 
      "UPDATE 3 1 ramyeon", 
      "UPDATE 3 2 korean", 
      "UPDATE 3 3 noodle", 
      "UPDATE 3 4 instant", 
      "UPDATE 4 1 pasta", 
      "UPDATE 4 2 italian", 
      "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", 
      "UPDATE korean hansik", 
      "UPDATE 1 3 group", 
      "UNMERGE 1 4", 
      "PRINT 1 3", "PRINT 1 4"]


ans = solution(co)
print(ans)
