class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord: tuple):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)
    
    def __contains__(self, coord: tuple):
        return coord in self.limits
    
if __name__ == "__main__":
    grid_bound = Grid(10, 10)
    grid = [[0 for _ in range(10)] for _ in range(10)]

    my_favorite_loc = [(1, 3), (3, 5), (3, 3)]

    for x, y in my_favorite_loc:
        if (x, y) in grid_bound:
            grid[x][y] = 'visited'

    for i in grid:
        print(i)

    


    