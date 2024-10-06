s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))  #common values from both sets
print(s1 - s2)
print(s2 - s1)

print({1, 78}.issubset(s2))
print(s2.issuperset({8, 1}))