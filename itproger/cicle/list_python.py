l = []
lis = [1, 56, 'x', 34, 2.34, ['S', 'T', 'R', 'O', 'K', 'A']]
print (lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print (a)


l.append(23)
l.append(24)
l.append(25)
l.append(34)

b = [ 24, 27]

l.extend(b)
l.insert(2, 107)
l.append(34)


l.remove(107)
l.pop(0)

print (l.index(34))
print (l.count(34))
l.sort()
l.reverse()

print (l)
