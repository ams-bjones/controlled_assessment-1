#Tells the user to choose between starting or ending the programme
decision = str(input(""" What would you like to do?; 
1) Convert a 10 digit number to an ISBN number(1) 
2) Quit and end the programme(2)""")) 

#Ends the programme
if decision == "2": 
    quit()
    print("Good Bye!") 
    
#Asks the user to input a 10 digit number
elif decision == "1": 
    (ISBN)=raw_input("Enter a 10 digit number") 
    
#If the number isnt 10 it will loop round and ask the user to re-input the number
while len(ISBN)!= 10: 

#Informs the user the number that has been given to the computer isnt 10 digits
    print('you have not entered a 10 digit number!!!') 
    ISBN=int(input('Please enter a 10 digit number ')) 
    continue

#This is the math side of things. its pretty much just the ISBN.
else: 

    Di1=int(ISBN[0])*11
    Di2=int(ISBN[1])*10
    Di3=int(ISBN[2])*9
    Di4=int(ISBN[3])*8
    Di5=int(ISBN[4])*7
    Di6=int(ISBN[5])*6
    Di7=int(ISBN[6])*5
    Di8=int(ISBN[7])*4
    Di9=int(ISBN[8])*3
    Di10=int(ISBN[9])*2

sum=(Di1+Di2+Di3+Di4+Di5+Di6+Di7+Di8+Di9+Di10) 

num=sum%11
Di11=11-num 
if Di11==10: 
    Di11='X'
ISBNNumber=str(ISBN)+str(Di11) 
#Shows the user what number has been output by the computer thus being the ISBN number
print('The ISBN number is -->    ' + ISBNNumber) 