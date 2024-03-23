class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        xm, ym = target
        my_distance = abs(xm) + abs(ym)
        for xg, yg in ghosts:
            ghost_distance = abs(xm - xg) + abs(ym- yg)
            if ghost_distance <= my_distance:
                return False
        return True
