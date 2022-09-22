from os import path
import torch
from hashlib import md5

MAZEFILE = 'maze.pt'
abs_path = path.join(path.dirname(__file__), MAZEFILE)

class Maze(torch.nn.Module):
    pass

model = torch.load(abs_path)
# print(model)

maze = model.maze.weight.data
# print(maze)
height, width = maze.size()
start = None

for y, row in enumerate(maze):
    found = False
    for x, num in enumerate(row):
        if num.item() == 2:
            found = True
            break
    if found:
        start = (y, x)
        break

search = [(start, [])]
found_points = [None]
while search:
    (y, x), path = search.pop(0)
    if maze[y][x].item() == 3:
        print(md5((''.join(path)).encode()).hexdigest())
        break
    if (y, x) in found_points:
        continue
    found_points.append((y, x))

    up = (y-1, x) if y > 0 else None
    if up not in found_points and maze[up[0]][up[1]].item() != 1:
        path_copy = path[:]
        path_copy.append('W')
        search.append((up, path_copy))
    right = (y, x+1) if x < width - 1 else None
    if right not in found_points and maze[right[0]][right[1]].item() != 1:
        path_copy = path[:]
        path_copy.append('D')
        search.append((right, path_copy))
    down = (y+1, x) if y < height - 1 else None
    if down not in found_points and maze[down[0]][down[1]].item() != 1:
        path_copy = path[:]
        path_copy.append('S')
        search.append((down, path_copy))
    left = (y, x-1) if x > 0 else None
    if left not in found_points and maze[left[0]][left[1]].item() != 1:
        path_copy = path[:]
        path_copy.append('A')
        search.append((left, path_copy))
# print('\n'.join(''.join(map(lambda x: '#' if x == 1 else '-', map(int, row))) for row in maze.tolist()))