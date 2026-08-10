'''
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

conditions for palindrome:
1. even number of letters + each letter appears an even number of times
2. odd number of letters + only one letter with odd number of ocurrences
'''

def is_palindrome(text: str) -> bool:
    if len(text) == 0:
        return True
    
    let_freq = {}
    nr_of_odd = 0

    for char in text:
        let_freq[char] = 1 if char not in let_freq else let_freq[char] + 1

    for freq in let_freq.values():
        if freq % 2 == 1:
            nr_of_odd += 1
    
    if len(text) % 2 == 0 and nr_of_odd == 0:
        return True
    
    if len(text) % 2 == 1 and nr_of_odd == 1:
        return True
    
    return False

print(is_palindrome("carrace"))
print(is_palindrome("daily"))
print(is_palindrome("aabbccdd"))    
