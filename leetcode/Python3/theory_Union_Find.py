"""
Union Find:

1. find() - find the parent of the group set
2. join() - join two groups / sets

Parent = [] where Parent[i] is equal to the parent of i.
Initialize with Parent[i] = i


"""
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))


    def find(self, x: int) -> int:
        """
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def join(self, x: int, y: int) -> None:
        self.parent[self.find(y)] = self.find(x)


class DisjointUnion:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]    
    
    def unionSets(self, x: int, y: int) -> None:
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return
        
        # Union by rank
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1    