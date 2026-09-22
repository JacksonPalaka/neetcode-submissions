class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max_len = 0

        while l<r:
            maxV = min(heights[l],heights[r]) * (r-l)
            max_len = max(max_len,maxV)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_len