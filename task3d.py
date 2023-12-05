''''
 A program to find and print the sum of all the even numbers from 
 1 to 50 (inclusive). Additionally, for each even number,  if it is a multiple of 3, print "Three" instead of the number;
if it is a multiple of 5, print "Five" instead of the number.
 Finally, print the total sum and the count of numbers replaced with 
 "Three" or "Five."
 '''
sum=0
count=0
for i in range(51):
   if i%2==0:
    sum+=i
   
   
    if  i % 3 == 0:
        print( 'Three')
        count+=1

    elif i% 5==0:
        print ('Five')
        count+=1
    else:
        print(i)
        
   
print("The total sum is ",sum)
print("The count  is ",count)