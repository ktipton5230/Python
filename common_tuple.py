tup1 = (23, 45, 67, 77, 89, 1003, 234, 1, 33, 78, 2, 65)
tup2 = (33, 65, 22, 89, 1005, 234, 2, 23, 45, 989, 34, 6)


def get_common_elements(tup1, tup2):
    result = ()
    found_common = False

    for element in tup1:
        if element in tup2:
            result += (element, )
            found_common = True


    if found_common :
        print("Found the common numbers\n")
    else:
        print("No common number found between the lists, sorry.")
    return result


print(get_common_elements(tup1,tup2))

