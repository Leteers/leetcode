#https://leetcode.com/problems/find-all-people-with-secret/description/
from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dicton = {}
        knows = [True if i in [0,firstPerson] else False for i in range(n)]
        for m in meetings:
            if m[2] in dicton.keys():
                dicton[m[2]].append((m[0],m[1]))
            else:
                dicton[m[2]] = [(m[0],m[1])]
        dicton = dict(sorted(dicton.items()))
        for key in dicton.keys():
            graph = defaultdict(list)
            participants = set()
            for x,y in dicton[key]:
                graph[x].append(y)
                graph[y].append(x)
                participants.add(x)
                participants.add(y)
            
            start = []
            visited = []

            for par in participants:
                if knows[par]:
                    start.append(par)
                    visited.append(par)

            while start:
                x = start.pop(0)
                for y in graph[x]:
                    if y not in visited:
                        visited.append(y)
                        start.append(y)
            for i in visited:
                knows[i] = True
        return[i for i in range(len(knows)) if knows[i] == True]
            
        #     i = 0
        #     flag = False
        #     while i < len(dicton[key])+1:
        #         if flag == True:
        #             i = 0
        #             flag = False
        #         if i == len(dicton[key]):
        #             break
        #         k = [knows[dicton[key][i][0]],knows[dicton[key][i][1]]]
        #         if any(k) and not all(k):
        #             knows[dicton[key][i][0]] = True
        #             knows[dicton[key][i][1]] = True
        #             flag = True
        #         i+=1
        # return[i for i in range(len(knows)) if knows[i] == True]


# from collections import defaultdict, deque
# from typing import List

# class Solution:
#     def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
#         # People who know the secret
#         knows = set([0, firstPerson])

#         # Group meetings by time
#         time_map = defaultdict(list)
#         for x, y, t in meetings:
#             time_map[t].append((x, y))

#         # Process meetings in chronological order
#         for t in sorted(time_map.keys()):
#             graph = defaultdict(list)
#             participants = set()

#             # Build graph for this time
#             for x, y in time_map[t]:
#                 graph[x].append(y)
#                 graph[y].append(x)
#                 participants.add(x)
#                 participants.add(y)

#             # BFS from participants who already know
#             queue = deque()
#             visited = set()

#             for p in participants:
#                 if p in knows:
#                     queue.append(p)
#                     visited.add(p)

#             while queue:
#                 person = queue.popleft()
#                 for nei in graph[person]:
#                     if nei not in visited:
#                         visited.add(nei)
#                         queue.append(nei)

#             # Everyone reached now knows the secret
#             knows.update(visited)

#         return list(knows)


if __name__ == '__main__':
    s = Solution()
    print(s.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1))#[0,1,2,3,5]
    print(s.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3))#[0,1,3]
    print(s.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1))
    print(s.findAllPeople(n = 5, meetings= [[1,4,3],[0,4,3]], firstPerson= 3))