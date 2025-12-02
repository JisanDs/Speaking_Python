
lst = [5, 6, 7, 9]
exp = 6
for i, n in enumerate(lst):
    if n == exp:
        lst.pop(i)
print(lst)
