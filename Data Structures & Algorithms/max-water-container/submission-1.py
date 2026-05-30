class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        max_v = 0

        while s < e:
            c_v = (e-s) * min(heights[e],heights[s])
            max_v = max(c_v,max_v)

            if heights[s] < heights[e]:
                s +=1
            else:
                e-=1

        return max_v