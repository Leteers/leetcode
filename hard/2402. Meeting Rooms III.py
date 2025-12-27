#http://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2025-10-20

from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        n_time = [0 for i in range(n)]
        n_cnt = [0 for i in range(n)]
        meetings = list(sorted(meetings))
        for i in meetings:
            for index,time in enumerate(n_time):
                if i[0] >= time:
                    n_time[index] = i[1]
                    n_cnt[index] +=1
                    break
            else:
                index = n_time.index(min(n_time))
                n_cnt[index] +=1
                n_time[index] += i[1] - i[0]
        return n_cnt.index(max(n_cnt))

if __name__ == '__main__':
    s = Solution()
    print(s.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))
    print(s.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))
    print(s.mostBooked(n = 4, meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]))