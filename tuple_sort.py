tup = (45, 26, 19, 3, 22, 11, 67)


def is_sorted():
    for index, item in enumerate(tup):
        try:
            if item > tup[index + 1]:
                return False
        except IndexError:
            return True


results = is_sorted()
print(results)

if not results:
    new_tuple = sorted(tup)
    print(new_tuple)