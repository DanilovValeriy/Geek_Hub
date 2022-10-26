def generator(first):
    while True:
        if not first:
            yield first 
        else:
            for el in first:
                yield el


for el in generator({1, 2, 3}):
    print(el)