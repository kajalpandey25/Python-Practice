l = [11,45,1,2,4,6,1,1]
print(l)
l.append(7)
l.sort()
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m =  l.copy()
m[0] = 0
l.insert(2,899)
m = [900, 1000, 1100]
l.extend(m)
m = [900, 1000, 1100]
k = l + m
print(k)
print(l)