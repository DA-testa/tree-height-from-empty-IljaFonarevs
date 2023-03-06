import sys
import threading

def compute_augstums(n, parents):
    augstums = [0] * n
    max_augstums = 0
    
    for i in range(n):

        node_weight = i
        depth = 0

        while not node_weight == -1:
            if augstums[node_weight] == 0:
                depth += 1
                node_weight = parents[node_weight]
            else:
                depth += augstums[node_weight]
                break
            
        max_augstums = max_augstums if max_augstums > depth else depth
        
        node_weight = i
        while not node_weight == -1:
            if augstums[node_weight] == 0:
                augstums[node_weight] = depth
                depth -= 1
                node_weight = parents[node_weight]
            else: 
                break

    
    return max_augstums

def main():
    type = input().strip()

    if type == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
    elif type == 'F':
        filename = input().strip()

        with open('test/' + filename, 'r') as File:
            n = int(File.readline())
            parents_raw = File.readline().split()
            parents = []
            for i in range(len(parents_raw)):
                parents.append(int(parents_raw[i]))
        File.close()

    augstums = compute_augstums(n, parents)
    print(augstums)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
