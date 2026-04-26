class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) # Everyone is their own parent
        self.rank = [0] * n # all trees have a height of 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]