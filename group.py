#This function takes a list[int] as its only parameter. This function will group the elements of
#the input list into groups of three values (i.e., the first three consecutive values form a group,
#the second three form a group, etc.). This function must return a list[list[int]] where each
# sublist (excluding, perhaps, the last) is a group of three values.
def groups_of_3(lst: list[int]) -> list[list[int]]:
    final = []
    end = ((len(lst) // 3) * 3 + 1)
    for i in range(0, end - 3, 3):
        new = []
        for j in range(i, i+3):
            new.append(lst[j])
        final.append(new)
    new = []
    if end != len(lst)+1:
        for i in range(end, len(lst)+1):
            new.append(i)
        final.append(new)
    return final


