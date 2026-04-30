class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            cur_min_dist = min(dist_left, dist_right)
            max_radius = max(max_radius, cur_min_dist)
            
        return max_radius