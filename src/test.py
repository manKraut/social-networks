import v_star_sets
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

i = 1
nodelist1 = []
nodelist2 = []
N = len(a) + len(b)

for line in a:
    nodelist1.append(line)

for line in b:
    nodelist2.append(line)

v_star_set = set(nodelist1) & set(nodelist2)

print(v_star_set)
