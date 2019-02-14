l1=[x for x in range(100000)]
print(l1.__sizeof__())
# for j in l1:
#     print(j)

l2=(x for x in range(100000))
print(l2.__sizeof__())
# for i in l2:
#     print(i)