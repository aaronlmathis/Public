class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity                        # capacity = Number of buckets in element
        self.size = 0                                   # size = number of elements in HashMap
        self.buckets = [[] for _ in range(capacity)]    # buckets = holds bucket that holds items
    
    # O(1) - constant time

    def __len__(self):
        return self.size
    
    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function

    def __contains__(self, key) -> bool:
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False
    
    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1
    
    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError('Key not found')
    
    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('Key not found')

    # O(n) - linear()

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]
    
    # O(n) - linear()

    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]
    
    # O(n) - linear()

    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # Average: O(k) - linear in key length
    # Practically: O(1)

    def _hash(self, key):
        key_string = str(key)
        hash_result = 0
        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        
        return hash_result

if __name__ == '__main__':
    import uuidimport matplotlib.pyplot as plt

    hash_map = HashMap(32)

    hash_map.put('name', 'Mike')
    hash_map.put('age', 30)
    hash_map.put('job', 'Programmer')

    print(hash_map.items())
    print(hash_map.buckets)
