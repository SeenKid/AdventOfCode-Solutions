# %%
import numpy as np
from time import perf_counter
 
t1 = perf_counter()
with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
 
# %%
data = np.array([[int(i) for i in d.split(',')] for d in data])
# %%
# find smallest and largest voxel positions in data
dim_mins = np.amin(data, axis=0)
dim_maxs = np.amax(data, axis=0)
# %%
# create grid with padding according to maximum values of voxel positions
grid = np.zeros(dim_maxs+2, dtype=np.int32)
grid[data[:, 0], data[:, 1], data[:, 2]] = 1
 
 
# %%
# define a shift function that shifts the whole array by value val along
# axis axis and pads the other side with zeros to keep array size
# uses np.roll for speed
def shift(arr: np.ndarray, axis: int, val: int) -> np.ndarray:
    if val == 0:
        return arr
    t = np.roll(arr, val, axis)
    if axis == 0:
        if val > 0:
            t[:val, :, :] = 0
            return t
        elif val < 0:
            t[val:, :, :] = 0
            return t
        else:
            raise TypeError
    elif axis == 1:
        if val > 0:
            t[:, :val, :] = 0
            return t
        elif val < 0:
            t[:, val:, :] = 0
            return t
        else:
            raise TypeError
    elif axis == 2:
        if val > 0:
            t[:, :, :val] = 0
            return t
        elif val < 0:
            t[:, :, val:] = 0
            return t
        else:
            raise TypeError
    else:
        raise IndexError
 
 
# %%
# ------ PUZZLE 18-01 ------
 
# neighbor from left:
t = grid + shift(grid, 0, 1)
left = np.zeros(t.shape, dtype=grid.dtype)
left[t == 2] = 1
 
# neighbor from right:
t = grid + shift(grid, 0, -1)
right = np.zeros(t.shape, dtype=grid.dtype)
right[t == 2] = 1
 
# neighbor from behind:
t = grid + shift(grid, 1, 1)
behind = np.zeros(t.shape, dtype=grid.dtype)
behind[t == 2] = 1
 
# neighbor from front:
t = grid + shift(grid, 1, -1)
front = np.zeros(t.shape, dtype=grid.dtype)
front[t == 2] = 1
 
# neighbor from below:
t = grid + shift(grid, 2, 1)
below = np.zeros(t.shape, dtype=grid.dtype)
below[t == 2] = 1
 
# neighbor from top:
t = grid + shift(grid, 2, -1)
top = np.zeros(t.shape, dtype=grid.dtype)
top[t == 2] = 1
# %%
# calculate all faces
faces = np.zeros(grid.shape, dtype=grid.dtype)
faces[grid != 0] = 6  # every cube has 6 faces
 
# subtract faces that are facing other cubes from any direction
faces -= top
faces -= below
faces -= left
faces -= right
faces -= front
faces -= behind
t2 = perf_counter()
print("Surface Area Puzzle 1:", np.sum(faces[faces != 0]), t2-t1)
 
 
# %%
# ------ PUZZLE 18-02 ------
t3 = perf_counter()
 
 
# find outside by recursively propagating the "outside"
# returns a np.ndarray of same size as arr with value 2
# meaning outside, value 1 meaning droplets of the grid
# value 0 meaning inside
def propagate_outside(arr: np.ndarray) -> np.ndarray:
    arr = arr.copy()
    old_arr = arr.copy()
    arr[0, 0, 0] = 2
    t01 = shift(arr, 0, 1)
    t0n1 = shift(arr, 0, -1)
    t11 = shift(arr, 1, 1)
    t1n1 = shift(arr, 1, -1)
    t21 = shift(arr, 2, 1)
    t2n1 = shift(arr, 2, -1)
    arr[(t01 == 2) & (arr != 1)] = 2
    arr[(t0n1 == 2) & (arr != 1)] = 2
    arr[(t11 == 2) & (arr != 1)] = 2
    arr[(t1n1 == 2) & (arr != 1)] = 2
    arr[(t21 == 2) & (arr != 1)] = 2
    arr[(t2n1 == 2) & (arr != 1)] = 2
    if np.all(old_arr == arr):
        return arr
    else:
        return propagate_outside(arr)
 
 
# %%
outside = propagate_outside(grid)  # outside: 2, cubes: 1, inside: 0
 
is_inside = np.zeros(outside.shape, dtype=grid.dtype)
is_inside[outside == 0] = 1
# %%
# subtract inside faces from cube faces left after Puzzle 1
faces -= shift(is_inside, 0, 1)  # left
faces -= shift(is_inside, 0, -1)  # right
faces -= shift(is_inside, 1, 1)  # behind
faces -= shift(is_inside, 1, -1)  # front
faces -= shift(is_inside, 2, 1)  # bottom
faces -= shift(is_inside, 2, -1)  # top
 
t4 = perf_counter()
# only sum the faces > 0 because all interior values without cubes will
# accumulate negative vals
print("Exterior Surface Area:", np.sum(faces[faces > 0]), t4-t3)