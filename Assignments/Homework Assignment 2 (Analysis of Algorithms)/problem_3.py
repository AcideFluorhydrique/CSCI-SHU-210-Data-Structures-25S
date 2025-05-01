def lengthOfLongestSubstring(s):
    # TODO: Please write your code here
    if s == '': return 0
    appear = set(

    )
    l = 0 # 左指针
    output = 0
    slist = list(s)

    for r in range(len(slist)): # 右指针
        while slist[r] in appear: # 还是O(n)
            appear.remove(slist[l])
            l += 1
        appear.add(slist[r])
        output = max(output, 1 + r - l)

    return output # pass

# Do not change or remove the code below this point
def main():
    s = "abcabcbb"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 3, Length of the substring “abc”

    # Example 2
    s = "bbbbb"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 1, Length of the substring “b”


    # a = "pwwkew"
    # res = lengthOfLongestSubstring(a)
    # print(res)


if __name__ == '__main__':
    main()
