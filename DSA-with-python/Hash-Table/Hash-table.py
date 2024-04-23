stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
stock_prices
[['march 6', 310.0],
 ['march 7', 340.0],
 ['march 8', 380.0],
 ['march 9', 302.0],
 ['march 10', 297.0],
 ['march 11', 323.0]]


stock_prices[0]

['march 6', 310.0]

# Find stock price on March 9
for element in stock_prices:
    if element[0] == 'march 9':
        print(element[1])

# Complexity of search using a list is O(n)        
# Complexity of search using a list is O(n) 

stock_prices = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
stock_prices
{'march 6': 310.0,
 'march 7': 340.0,
 'march 8': 380.0,
 'march 9': 302.0,
 'march 10': 297.0,
 'march 11': 323.0}

# Find stock price on March 9

stock_prices['march 9']
302.0

# Complexity of search using dictionary is O(1)
# Implement Hash Table
def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100
get_hash('march 6')
9


class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None       