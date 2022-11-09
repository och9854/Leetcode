# def find_subset( s: str ) -> int:
#     left = ans = 0
#     # repeat len(s)
#     for right in range(len(s)):
#         if s[right] == '1':
#             ans += 1
        
#         while s[right] == '0':
#             ans -= 1
#             left += 1
        
#         ans = max(ans, right - left + 1)

#     return ans

# print(find_subset("1101100111"))

# answer
'''
def find_length(s):
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans
'''
