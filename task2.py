# surnames = {
#     "Jackson": ["Samantha Jackson", "2 Heather Row", "Basingstoke", "RG21 3SD", "01256 135434",	"23/04/1973", "sam.jackson@hotmail.com"]
#     "VickersJ": ["Jonathan",	"18 Saville Gardens", "Reading", "RG3 5FH",	"01196 678254",	"04/02/1965", "the_man@btinternet.com"]
#     "Morris": ["Sally", "The Old Lodge", "Hook", "RG23 5RD", "01256 728443", "19/02/1975", "smorris@fgh.co.uk"]
#     "Cobbly": ["Harry", "345 The High Street", "Guildford", "GU2 4KJ", "01458 288763", "30/03/1960", "harry.cobbly@somewhere.org.uk"]
#     "Khan": ["Jasmine", "36 Hever Avenue", "Edenbridge", "TN34 4FG", "01569 276524", "28/02/1980", "jas.khan@hotmail.com"]
#     "VickersH": ["Harriet", "45 Sage Gardens", "Brighton", "BN3 2FG", "01675 662554", "04/04/1968", "harriet.vickers@btinternet.com"]
#     }
#Loads up the address file to the code so it can find them
addressses = []
def getAddrs():
    with open('addressbook.csv')as book:
        data = book.read()
        for line in data.split('\r\n'):
            address = line.split(',')
            addressses.append(address)
#This welcomes the user and asks the user to select two choices
getAddrs()
print("Welcome to the Address Book!")
answer = None
while answer not in ["1", "2"]:
   answer = raw_input("Are You Adding An Address (Press 1) \nOr finding an address? (Press 2) ") 



 

#Creating a file into the address book and saving it for later
if answer == "1" : 
    print (" You have selected to create an entry.")

#Now it asks the user info on the person so it is easier to find them
    lastname = raw_input("What is the persons last name? ")
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What is the persons phone number? ")
    email = raw_input("What is the persons email address? ")
    address = raw_input("What is the persons address? ")

    #This line tells the computer to open/create a file

    tempfile = open("datafile.txt","a")
    
    #adds the first name, last name, phone, email and address to the address book
    tempfile.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
    tempfile.write("\n")
    tempfile.close()
    quit()

#If searching for a file already created

if answer == "2":
    choice = raw_input("you have selected to search for an entry. Would you like to search by surnames [Press 1] \n Or by month of birth [Press 2]")
    
#asks the user to input the lastname of someone. once done it then searchs the system for anyone with the last name
#after that it then gives you the list of people with that last name along with their info
if choice == "1":
    surname_search = raw_input("What surname are you searching for?: ")
    for address in addressses:
        if surname_search == address[0]:
            print address
            
#Pretty much the same as the choice 1 but you're looking for the birth month
if choice == "2":
    month_search = raw_input("What month are you searching for? \n(in numbers E.G 01=january)")
    for address in addressses:
        if len(address)>6:
            dd,mm,yy = address[6].split('/')
            if month_search == mm:
                print address
                
else:
   print("Incorrect entry, please restart the programme, and try again.")