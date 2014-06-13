curency=["GBP", "USD", "JPY", "EUR"]
rates = [1,2,3,4]
print ("Welcome to the Currency converter")
def ask(direction):
    print ("##################################")
    print ("Please pick a currency to convert {0}".format(direction))
    print ("##################################")
    
        
    print("Pound", rates[0])
    print("Dollar", rates[1])
    print("Yen", rates[2])
    print("Euro", rates[3])
    choice = int(input("Enter choice(1/2/3/4):"))
    return (choice)

cfrom=ask("from")-1
cto=ask("to")-1

def tell(change):
    print ("##################################")
    print ("Or you can change your currency amount")
    convert = int(input("Enter change to do so:"))

entry=float(input("You have selected {0}. Now please enter a sum of money:".format(curency[cfrom])))
answer= (entry/rates[cfrom])*rates[cto]
print ("{0:.2f}".format(answer))

# if choice == rates[0]:
#     entry= input("You have selected Pounds. Now please enter a sum of money:")
#     answer = (entry*rates[0])
#     print(answer)
    
# if choice == rates[1]:
#     entry= input("You have selected Dollar. Now please enter a sum of money:")
#     answer = (entry*rates[1])
#     print(answer)
    
# if choice == rates[2]:
#     entry= input("You have selected Yen. Now please enter a sum of money:")
#     answer = (entry*rates[2])
#     print(answer)
    
# if choice == rates[3]:
#     entry= input("You have selected Euro. Now please enter a sum of money:")
#     answer = (entry*rates[3])
#     print(answer)