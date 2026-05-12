import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for i in piles:
                totalTime+= math.ceil(i/speed)

            if totalTime<= h:
                return speed
            speed+=1
        return speed