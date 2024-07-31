'''
🍪문제 번호 :
10장 실전문제 - 커리큘럼

🍈문제 정의 :
N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각가 출력하기.   
(모든 강의는 1~N번으로 번호를 가지고 동시에 여러 강의를 들을 수 있다.)   
- 입력 : N(강의의 총수), 1번부터 N번까지 강의 시간(100000이하)과 선행강의 번호   
??각 줄은 -1로 끝난다?? --> 선행 강의가 여러개일 경우가 있어서 -1로 끝맺음 구분
- 출력 : 각 강의를 수강하기까지 최소 시간을 한줄로 출력

🍊풀이 시간 :
20분

🍒풀이 방법 :
딕셔너리를 사용하여 풀이
해설지랑 너무 다른데 이게 맞나?

'''

class Solution :
    
    def curriculum(self):
        # 입력
        N = int(input("강의 갯수(N) : "))
        
        lecture = {}

        for i in range(N):
            time, *tmp = map(int,input().split())
            prev_time = 0
            
            for prev in tmp :
                if prev == -1 :
                    break
                prev_time = max(lecture[prev],prev_time)
            
            time +=prev_time
            lecture[i+1] = time
        
        print("=== result  ===")
        print([time for time in lecture.values()])
            
        return 
    
test = Solution()
test.curriculum()


# soluteion
'''
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()
'''