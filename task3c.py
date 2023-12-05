#A program that checks whether a word is palindrom or not
word=input("Enter a wordto check ")
def is_palindrome(word):
    length=len(word)
    for i in range(0,length//2):
        if word[i]!=word[length-i-1]:
          return False
    
    return True

print(is_palindrome(word))
    

