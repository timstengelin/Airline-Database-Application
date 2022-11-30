import datetime

user = ''



def runApp():
    mainMenu()


def mainMenu():
    while (True):
        print('\n********************\n>> MAIN MENU')
        x = input('\n1 > register as customer\n2 > login as customer\n3 > login as airline\nSELECTION >>> ')
        if x == '1':
            registerAsCustomer()
        elif x == '2':
            loginAsCustomer()
        elif x == '3':
            loginAsAirline()


def registerAsCustomer():
    print('\n********************\n>> MAIN MENU\n   > register as customer')
    registerAsCustomer_username = input('\nusername\nSPECIFICATION >> ')
    registerAsCustomer_firstName = input('\nfirst name\nSPECIFICATION >> ')
    registerAsCustomer_lastName = input('\nlast name\nSPECIFICATION >> ')
    year, month, day = map(int, input('\nbirth date (YYYY-MM-DD)\nSPECIFICATION >> ').split('-'))
    registerAsCustomer_birthDate = datetime.date(year, month, day)
    registerAsCustomer_numberOfMobileNumbers = input('\nnumber of mobile numers\nSPECIFICATION >> ')
    # TODO


def loginAsCustomer():
    print('loginAsCustomer')


def loginAsAirline():
    print('loginAsAirline')


def customerMenu():
    print('TODO')


def airlineMenu():
    print('TODO')
