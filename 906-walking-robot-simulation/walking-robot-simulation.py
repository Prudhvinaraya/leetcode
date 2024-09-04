class Direction:
    def __init__(self,dx=0, dy=0, left=None, right=None):
        self.dx = dx
        self.dy = dy
        self.left = left
        self.right = right
    
    def next(self, x, y):
        return (x+self.dx, y+self.dy)


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        north = Direction(dy=1)
        east = Direction(dx=1, left=north)
        south = Direction(dy=-1, left=east)
        west = Direction(dx=-1, left=south, right=north)
        north.left = west
        north.right = east
        east.right = south
        south.right = west
        cur_x = 0
        cur_y = 0
        direction = north
        max_so_far = 0
        obstacles = set((x,y) for x,y in obstacles)
        
        for command in commands:
            if command == -2:
                direction = direction.left
                continue
            if command == -1:
                direction = direction.right
                continue
            max_so_far = max(max_so_far, cur_x**2 + cur_y**2)
            for _ in range(command):
                next_step = direction.next(cur_x, cur_y)
                if next_step in obstacles:
                    max_so_far = max(max_so_far, cur_x**2 + cur_y**2)
                    continue
                cur_x, cur_y = next_step
        max_so_far = max(max_so_far, cur_x**2 + cur_y**2)
        return max_so_far