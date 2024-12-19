import itertools
import time
import sys

# Set recursion limit higher for deep recursion in branch-and-bound
sys.setrecursionlimit(10000)

# Sample distance matrix representing 10 cities
distances = [
    [0, 29, 20, 21, 16, 31, 100, 12, 4, 31],
    [29, 0, 15, 29, 28, 40, 72, 21, 29, 41],
    [20, 15, 0, 15, 14, 25, 81, 9, 23, 27],
    [21, 29, 15, 0, 4, 12, 92, 12, 25, 13],
    [16, 28, 14, 4, 0, 16, 94, 9, 20, 16],
    [31, 40, 25, 12, 16, 0, 98, 12, 18, 11],
    [100, 72, 81, 92, 94, 98, 0, 90, 101, 99],
    [12, 21, 9, 12, 9, 12, 90, 0, 15, 24],
    [4, 29, 23, 25, 20, 18, 101, 15, 0, 19],
    [31, 41, 27, 13, 16, 11, 99, 24, 19, 0]
]

n = len(distances)  # Number of cities
pruned_paths = 0   # Counter for pruned paths in branch-and-bound

# 1) Function to implement TSP using State Space Exploration (Brute-Force)
def tsp_brute_force(distances):
    cities = list(range(n))
    min_path_cost = float('inf')
    min_path = []
    for perm in itertools.permutations(cities[1:]):  # Exclude the first city to avoid duplicate cycles
        path = [0] + list(perm) + [0]
        cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < min_path_cost:
            min_path_cost = cost
            min_path = path
    return min_path, min_path_cost

# 2) Function to implement TSP using Branch and Bound
def tsp_branch_and_bound(distances):
    global pruned_paths
    min_cost = float('inf')
    best_path = []
    
    def dfs(city, visited, path, path_cost):
        nonlocal min_cost, best_path,pruned_paths
        if len(path) == n:
            total_cost = path_cost + distances[city][0]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [0]
            return
        
        for next_city in range(n):
            if next_city not in visited:
                new_cost = path_cost + distances[city][next_city]
                if new_cost < min_cost:
                    dfs(next_city, visited | {next_city}, path + [next_city], new_cost)
                else:
                    pruned_paths += 1  # Path is pruned if it exceeds min_cost

    dfs(0, {0}, [0], 0)
    return best_path, min_cost

# Running and timing both algorithms
start_time = time.time()
brute_force_path, brute_force_cost = tsp_brute_force(distances)
brute_force_time = time.time() - start_time

start_time = time.time()
branch_bound_path, branch_bound_cost = tsp_branch_and_bound(distances)
branch_bound_time = time.time() - start_time

# Output results
print("Brute Force TSP Solution:")
print("Path:", brute_force_path)
print("Cost:", brute_force_cost)
print("Running Time:", brute_force_time, "seconds\n")

print("Branch and Bound TSP Solution:")
print("Path:", branch_bound_path)
print("Cost:", branch_bound_cost)
print("Running Time:", branch_bound_time, "seconds")
print("Total pruned paths:", pruned_paths)