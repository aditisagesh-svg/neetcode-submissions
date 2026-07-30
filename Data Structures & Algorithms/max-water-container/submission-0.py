class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        ans=0

        while left<right:
            width = right - left
            height=min(heights[left],heights[right])
            area = width * height
        
            ans = max(ans,area)

            if heights[left]<heights[right]:
                left +=1
            else:
                right -=1
        return ans

        