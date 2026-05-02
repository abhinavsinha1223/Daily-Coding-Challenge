# Extract digits from a number and count them
num=1123
list=[]
while num>0:
    num1=num%10
    print(num1)
    list.append(num1)
    num=int(num/10)

print(len(list))

"""
    Counts the number of "good" integers in the range [1, n].
    
    A good integer is one where rotating each digit 180 degrees results in a valid,
    different number. Valid rotations are:
    - 0, 1, 8 -> themselves
    - 2 <-> 5
    - 6 <-> 9
    - Other digits (3, 4, 7) are invalid after rotation.
    
    Each digit must be rotated; leaving any digit unchanged makes the number invalid.
    
    Args:
        n (int): The upper limit of the range (inclusive).
    
    Returns:
        int: The count of good integers from 1 to n.
        """

n = 857

change = {2, 5, 6, 9}
invalid = {3, 4, 7}

count = 0

for i in range(1, n + 1):
    num = i
    good = False
    valid = True

    while num > 0:
        digit = num % 10

        if digit in invalid:
            valid = False
            break

        if digit in change:
            good = True

        num //= 10

    if valid and good:
        count += 1

print(count)


