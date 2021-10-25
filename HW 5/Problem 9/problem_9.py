### Problem 9

def check_palindrome(word):
    if not isinstance(word, str):
        return("Argument not a string")
    
    # Base Case
    if len(word) in [0,1]:
        return(True)
    
    # Recursive Case
    if word[0] == word[-1]:
        return(check_palindrome(word[1:-1]))
    else:
        return(False)




check_palindrome("kayak")
check_palindrome("hello")

