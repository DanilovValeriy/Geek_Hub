# print(super_weird_sum(5)())           -> 5
# print(super_weird_sum(5)(3)())        -> 8
# print(super_weird_sum(5)(4)(-10)())   -> -1

def a(n):
    def b(f=0):
        return f + n

    f = f + n

    return b


print(a(9)())
