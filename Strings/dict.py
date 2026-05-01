# FOR ACCESSING THE DICTIONARY IT'S IMPORTANT
class Solution:
    def romanToInt(s: str) -> int:
        map={  "I":             1,
               "V":            5,
               "X" :             10,
                "L" :            50,
                "C":          100,
                "D"  :          500,
                "M"   :         1000}
        num=0
        i=0
        while i < len(s):
            if s[i] in map:
                print("s[i]: ", s[i])
                if i + 1 == len(s) or map[s[i]]>=map[s[i+1]]:
                    num=num+ map[s[i]]
                    print("num: ", num)
                    i=i+1
                elif map[s[i]]<map[s[i+1]]:
                    int=map[s[i+1]]-map[s[i]]
                    num=num + int
                    print(num)
                    i=i+2
        return num

s="MCM"
print(Solution.romanToInt(s))