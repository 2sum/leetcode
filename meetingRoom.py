#https://leetcode.com/problems/meeting-rooms-ii/
class Solution(object):
    def minMeetingRooms(self,intervals):
        used_rooms=0
        s=sorted(i[0] for i in intervals)
        print(s)
        e=sorted(i[1] for i in intervals)
        print(e)
        l=len(intervals)
        sp=0
        ep=0
        while sp<l:
            if s[sp]>=e[ep]:
                used_rooms-=1
                ep+=1
            used_rooms+=1
            sp+=1
        return used_rooms
s=Solution()
intervals=[[0, 30],[5, 10],[15, 20]]
print(s.minMeetingRooms(intervals))
