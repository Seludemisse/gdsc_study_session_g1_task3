char=input("Enter a character of u'r choice: ")
if char.lower() in ['a','e','i','o','u']:
      print("PLease enter the pattern to be printed")
      print("Vowels are not allowed in the input")
elif len(char)>1:
    print("PLease enter the pattern to be printed")
    print("The length of the character should be 1")
        
else:    

 for x in range(1,6):
    if x==1:
        print(char)
    elif x==2:
        print(char*2)
    elif x==3:
        print(char*3)
    elif x==4:
        print(char*4)
    elif x==5:
        print(char*5)
  

        