'''
    Write a function that takes two sets as input
    and returns a new set containing the common elements.
'''

def common_elements(set1, set2):
    return set1.intersection(set2) # ._.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = common_elements(set1, set2)

print(common_elements(set1, set2))