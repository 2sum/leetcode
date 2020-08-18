class Solution(object):
    def trap(self, height):
        res=0
        
        for i in range(len(height)):
            left_max=0
            right_max=0
            for j in range(i,-1,-1):
                left_max=max(left_max,height[j])
            for k in range(i,len(height),1):
                right_max=max(right_max,height[k])
            res+=min(left_max,right_max)-height[i]
        return res
            

s=Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))
