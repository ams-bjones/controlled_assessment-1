#http://stackoverflow.com/questions/20398017/showing-decimal-places-python-2-7-and-decimal-datatype#
#setup the decimal data type (including number of decimal places)
import decimal

#get the current value and type from the user
currencyAmount = decimal.Decimal(raw_input('please enter the amount: '))
currencyType = int(raw_input('please enter the type or if you want to change the rates (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))

#set the exchange rates (based on sterling)
euro = decimal.Decimal('1.2')
dollar = decimal.Decimal('1.6')
yen = decimal.Decimal('200')

#convert the currency into pound sterling
if (currencyType == 2):
    currencyAmount = currencyAmount / euro
elif (currencyType == 3):
    currencyAmount = currencyAmount / dollar
elif (currencyType == 4):
    currencyAmount = currencyAmount / yen

#ask the user what currency they want it converted into
currencyConvert = int(raw_input('please enter the currency you would like to convert to (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))

#convert the currency into the new format (pound already done in previous steps)
if (currencyConvert == 2):
    currencyAmount = currencyAmount * euro
elif (currencyConvert == 3):
    currencyAmount = currencyAmount * dollar
elif (currencyConvert == 4):
    currencyAmount = currencyAmount * yen

#show the amount of money converted to user
print 'the result of the currency conversion was ',  currencyAmount.quantize(decimal.Decimal('0.00'))

# This was the first code for the convert
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