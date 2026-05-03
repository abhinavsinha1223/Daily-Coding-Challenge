#BRITE SOLUTION WITH TIME COMPLEXITY O(n^2) 
s="abcde"
goal="dehce"

for i in range(len(s)):
    i=0
    temp=s[i]
    print(temp)
    s=s[i+1:]
    s=s+temp
    if (s==goal):
        flag=True
        break
    print(s)
    i=i+1

else:
    flag=False

print(flag)


#OTHER WAY WITH TIME COMPLEXITY O(n)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are different
        if len(s) != len(goal):
            return False

        # Create a new string by concatenating 's' with itself
        doubled_string = s + s

        # Use find to search for 'goal' in 'doubledString'
        # If find returns an index that is not -1
        # then 'goal' is a substring
        # eg abcdeabcde now we can easily find the goal if it exists or not
        return doubled_string.find(goal) != -1
