import math
import os
import random
import re
import sys
import collections

MOD = 1000000000

def countPaths(n, edges):
    graph = collections.defaultdict(list)

    for i, j in edges:
        graph[i - 1].append(j - 1)

    start = 0
    end = n - 1

    memo = [0] * n
    cycle_nodes = set()
    path_nodes = set()

    path = []
    seen = [False] * n

    def update_path_nodes(inc):
        for cur in path:
            path_nodes.add(cur)
            memo[cur] += inc
            memo[cur] %= MOD

    def update_cycle_nodes(cycle_start):
        k = len(path) - 1
        while path[k] != cycle_start:
            cycle_nodes.add(path[k])
            k -= 1
        cycle_nodes.add(cycle_start)

    def dfs(node):
        path.append(node)
        seen[node] = True

        if node == n - 1:
            update_path_nodes(1)
        else:
            for next_node in graph[node]:
                if seen[next_node]:
                    update_cycle_nodes(next_node)
                else:
                    if memo[next_node] > 0:
                        update_path_nodes(memo[next_node])
                    if memo[next_node] == 0:
                        dfs(next_node)

        if memo[node] == 0:
            memo[node] = -1

        seen[node] = False
        path.pop()

    dfs(start)
    if len(cycle_nodes.intersection(path_nodes)) > 1:
        return 'INFINITE PATHS'
    else:
        return memo[start]

# Directory paths
input_folder = "inputs"
output_folder = "outputs"

# Define function to check if output matches the content of output files
def check_output(nodes, edges, output_file):
    result = countPaths(nodes, edges)
    # Open the output file and compare its content with the computed output
    with open(output_file, 'r') as file:
        expected_output = file.read().strip()
    return str(result) == expected_output

# Iterate through input files
for i in range(1, 9):
    input_file = os.path.join(input_folder, f"input{i}.txt")
    output_file = os.path.join(output_folder, f"output{i}.txt")

    # Read input from file
    nodes = 0
    edges = []
    with open(input_file, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            if nodes == 0:
                nodes = x
            else:
                edges.append([x, y])

    # Execute the code and compare output with content of output files
    if os.path.exists(output_file):
        match = check_output(nodes, edges, output_file)
        print(match)
    else:
        print("False")  # If output file doesn't exist, it's automatically False
