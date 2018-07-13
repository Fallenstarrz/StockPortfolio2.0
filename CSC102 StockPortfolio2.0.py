#########################################################################################################################################################################
#                                                                                                                                                                       #
# In this assignment you will build the second part of a stock portfolio manager.                                                                                       #
#                                                                                                                                                                       #
# First, you will need to add the following function:                                                                                                                   #
#    1. GetSale - Finds the maximum expected value of selling a stock. The expected sale value of a stock is the current profit minus the future value of the stock:    #
#           Expected Sale value = ( ( Current Price - Buy Price ) - Risk * CurrentPrice ) * Shares                                                                      #
#           The GetSale function should calculate this value for each stock in the portfolio, and return the stock symbol with the highest expected sale value.         #
#    2. Main - Change/update/add the main function. This should take no arguments, but present a menu item consisting of:                                               #
#           "1. Add Stock", "2. Recommend Sale" and "3. Exit".                                                                                                          #
#           If the user selects '1,' the Add Stock function is called, and when it is complete, the menu is presented again.                                            #
#           If the user selects '2,' the Symbol of the stock corresponding to the highest expected value (returned by GetSale) should be displayed,                     #
#           and the menu presented after completion. If the user selects '3', the program should end.                                                                   #
#                                                                                                                                                                       #
# Be sure to use comments for both structure of the program and documentation of the code.                                                                              #
# All code must completely be your own individual work product.                                                                                                         #
#                                                                                                                                                                       #
#########################################################################################################################################################################

NAMES = {}                                                                                                              # Globally defines NAMES as a dictionary
PRICES = {}                                                                                                             # Globally defines PRICES as a dictionary
EXPOSURE = {}                                                                                                           # Globally defines EXPOSURE as a dictionary

def validMenu(y):                                                                                                       # This checks to see that the menu option is valid
    while True:                                                                                                         # Always start this loop
        if (str.isdigit(y)):                                                                                            # if passed variable is a digit
            y = int(y)                                                                                                  # make passed variable into an int
            if y >= 1 and y <= 5:                                                                                       # if passed variable is between (to include) 1 and 5
                return (y)                                                                                              # return the passed variable
            else:                                                                                                       # otherwise
                y = input('Please select a valid option\n')                                                             # get a valid number from user
        else:                                                                                                           # otherwise
            y = input('Please select a valid option\n')                                                                 # get a valid number from user
    
def validInput(x):                                                                                                      # Checks to see that the input is a number and turns it into an int                                                        
    while True:                                                                                                         # Always start this loop
        if (str.isdigit(x)):                                                                                            # if passed variable is digit
            x = int(x)                                                                                                  # make passed variable into an int
            return (x)                                                                                                  # return the passed variable
        else:                                                                                                           # otherwise
            x = input('Please select a valid integer\n')                                                                # get a valid number from user
      
def validFInput(z):                                                                                                     # This checks to see that the float is valid
    while True:                                                                                                         # Always start this loop
        if(z.replace('.', '', 1).isdecimal()):                                                                          # if passed variable is a number replacing the decimal with nothing
            z = float(z)                                                                                                # make passed variable a floating point number
            return(z)                                                                                                   # return the passed variable
        else:                                                                                                           # otherwise
            z = input('Please select a valid floating point value')                                                     # get a valid number from user

def makeMoney(b):                                                                                                       # Make and format an input into American currency
    b = '${:,.2f}'.format(b)                                                                                            # format the passed variable into 2 decimal places in the form of US currency
    return(b)                                                                                                           # return the passed variable

def makePercent(a):                                                                                                     # Make and format an input into a percentage
    a = '{:,.0%}'.format(a)                                                                                             # format the passed variable into a real percentage
    return(a)                                                                                                           # return the passed variable

def mainMenu(x):                                                                                                        # This is the main menu
    print()                                                                                                             # Print an empty Line
    print('Stock Portfolio')                                                                                            # Print Stock Portfolio
    print('---------------')                                                                                            # Print a placement line for cosmetics
    print('1. Search Stocks')                                                                                           # Display option 1: Search Stocks
    print('2. Create New Stock')                                                                                        # Display option 2: Create New Stock
    print('3. Edit Stock in Portfolio')                                                                                 # Display option 3: Edit Stock in Portfolio
    print('4. Recommend Sale in Portfolio')                                                                             # Display option 4: Recommend Sale in Portfolio
    print('5. Close Program')                                                                                           # Display option 5: Close Program
    print()                                                                                                             # Print an empty line for cosmetics                                                        
    x = input('What would you like to do? ')                                                                            # get menu option from user
    x = validMenu(x)                                                                                                    # validate menu option from user by passing it to a validate function
    return(x)                                                                                                           # return the users choice

def editMenu(x):                                                                                                        # This is the edit menu
    print()                                                                                                             # Print an empty line
    print('Edit Portfolio')                                                                                             # Print Edit Portfolio
    print('---------------')                                                                                            # Print a cosmetic line
    print('1. Return to previous menu')                                                                                 # Display option 1: Return to previous menu
    print('2. Edit Company Name or Company Symbol')                                                                     # Display option 2: edit company name or company symbol
    print('3. Edit Buy and Sell Price')                                                                                 # Display option 3: edit buy and sell prices
    print('4. Edit Risk or Number of shares owned')                                                                     # Display option 4: edit risk or number of shares owned
    print()                                                                                                             # print an empty line for cosmetics
    x = input ('What would you like to do?')                                                                            # get menu option from user
    x = validMenu(x)                                                                                                    # pass user option to a validate menu
    if x > 5:                                                                                                           # if option isn't in menu
        x = input('Please Select a valid option')                                                                       # make user select a valid option
    return(x)                                                                                                           # return the users choice

def searchMenu(NAMES):                                                                                                  # This is the search menu. This will generate a menu
    num = 1                                                                                                             # that will grow as you add more companies to your dictionary
    print()                                                                                                             # make a variable to store numbers in
    print('Search Portfolio')                                                                                           # Print Search Menu
    print('---------------')                                                                                            # Print a cosmetic line
    print('0. Previous Menu')                                                                                           # Print option 0: Previous Menu
    for i in NAMES:                                                                                                     # for keys in Names
        print(num,'. ', i, sep='')                                                                                      # Print a decending list of the keys to the user
        num += 1                                                                                                        # add 1 to num variable to be used in formatting the list
    x = input ('Which Stock would you like to explore? ')                                                               # ask user which stock he would like to look at
    x = validInput(x)                                                                                                   # validate user input
    while ((x > num) or (x < 0)):                                                                                       # while the user input is greater than the number of items displayed or less than 0
        x = input('Please select a valid company in your portfolio.')                                                   # prompt user to select a valid menu option
        x = validInput(x)                                                                                               # validate user input
    return(x)                                                                                                           # return menu option

def addName(NAMES):                                                                                                     # Adds Names to your dictionary list
    stockSymbol = input('Please input the company symbol. ')                                                            # stockSymbol is defined as an input
    stockName = input('Please input the company name. ')                                                                # stockName is defined as an input
    NAMES[stockSymbol] = [stockName]                                                                                    # Stocksymbol is placed as the key to the dictionary and stockName is the value
    PRICES[stockSymbol] = None                                                                                          # Prices is assigned the stockSymbol
    EXPOSURE[stockSymbol] = None                                                                                        # Exposure is assigned the stockSymbol
    return(NAMES)                                                                                                       # return NAMES
    
def addPrices(PRICES):                                                                                                  # Adds prices to stock symbols
    while True:                                                                                                         # Always run this loop
        stockSymbol = input('Please input the company symbol. ')                                                        # get a symbol in which to store these values in
        if stockSymbol in PRICES:                                                                                       # if stockSymbol is in the PRICES dictionary
            buyPrice = input('How much does this stock cost to purchase? ')                                             # ask user how much the stock costs to purchase and assign it buyPrice variable
            buyPrice = validFInput(buyPrice)                                                                            # validate the price
            buyPrice = makeMoney(buyPrice)                                                                              # change the price into american standard currency
            sellPrice = input('How much does this stock sell for? ')                                                    # ask user how much the stock sells for and assign it sellPrice variable
            sellPrice = validFInput(sellPrice)                                                                          # validate the price
            sellPrice = makeMoney(sellPrice)                                                                            # change the price into american standard currency
            PRICES[stockSymbol] = [buyPrice, sellPrice]                                                                 # dictionary PRICES is assigned the buyprice and sellprice as values
            return (PRICES)                                                                                             # return the dictionary
        else:                                                                                                           # otherwise
            print('This symbol does not exist.')                                                                        # let user know that the symbol doesn't exist and restart the loop

def addExposure(EXPOSURE):                                                                                              # Adds risk and shared owned to stock symbols
    while True:                                                                                                         # always run this loop
        stockSymbol = input('Plese input the company symbol. ')                                                         # get a symbol in which to store these values in
        if stockSymbol in EXPOSURE:                                                                                     # if symbol is in EXPOSURE
            ownedShares = input('How many shares do you own? ')                                                         # ask user how many shares they own and store their input in ownedShares
            ownedShares = validFInput(ownedShares)                                                                      # validate user input
            risk = input('What is the risk of owning this share? ')                                                     # ask user what the risk of owning this share is
            risk = validFInput(risk)                                                                                    # validate the user input
            risk = makePercent(risk)                                                                                    # format the user input to a percentage
            EXPOSURE[stockSymbol] = [ownedShares, risk]                                                                 # dictionary EXPOSURE is assigned the ownedShares and risk as values
            return(EXPOSURE)                                                                                            # return EXPOSURE
        else:                                                                                                           # otherwise
            print('This symbol does not exist.')                                                                        # let user know that the symbol doesn't exist and restart the loop

def addStock(NAMES, PRICES, EXPOSURE):                                                                                  # Calls the three add functions to create a stock in your stock portfolio
    NAMES = (addName(NAMES))                                                                                            # NAMES dictionary is given the return of the addNames function and NAMES is passed as the variable
    PRICES = (addPrices(PRICES))                                                                                        # PRICES dictionary is given the return of the addPrices function and PRICES is passed as the variable
    EXPOSURE = (addExposure(EXPOSURE))                                                                                  # EXPOSURE dictionary is given the return of the addExposure function and EXPOSURE is passed as the variable
    print('Successfully Placed Stock in Portfolio')                                                                     # let user know their stock was successfully placed into the portfolio
    return(NAMES, PRICES, EXPOSURE)                                                                                     # return all 3 dictionaries

def searchPortfolio(NAMES, PRICES, EXPOSURE):                                                                           # This Searches through the company symbol keys and will return all of
    while True:                                                                                                         # elements belonging to that stock symbol. Always start this loop.
        explore = searchMenu(NAMES)                                                                                     # explore is stored as the return of the searchMenu function and NAMES is passed as the variable
        search = list(NAMES.keys())                                                                                     # search is assigned as a list of keys in the dictionary NAMES
        search.insert(0, 'Previous Menu')                                                                               # search has previous menu assigned to the 0 slot in the list and everything else is moved to the right
        if explore == 0:                                                                                                # if explore is 0
            return()                                                                                                    # return to previous menu
        else:                                                                                                           # otherwise
            print(NAMES.get(search[explore]))                                                                           # print the values in NAMES using the menu option as the key 
            print(PRICES.get(search[explore]))                                                                          # print the values in PRICES using the menu option as the key 
            print(EXPOSURE.get(search[explore]))                                                                        # print the values in EXPOSURE using the menu option as the key 

def editPortfolio(NAMES, PRICES, EXPOSURE):                                                                             # This will let you hop into a stock symbol and the values of it's elements
    previous = 1                                                                                                        # previous is assigned 1 as value
    editNames = 2                                                                                                       # editNames is assigned 2 as value
    editPrices = 3                                                                                                      # editPrices is assigned 3 as value
    editRisk = 4                                                                                                        # editRisk is assigned 4 as value
                                                                                                                        
    decision = 0                                                                                                        # decision is initially assigned 0, so we can hop into the below loop
                                                                                                                        # The above variables are used as menu options
    while decision != previous:                                                                                         # while users decision is not previous manu (a.k.a. "1")
        decision = editMenu(decision)                                                                                   # Call the editMenu function and pass decision as the argument. Use the return of this function as the decision
        if decision == previous:                                                                                        # if decision is '1', Previous Menu
            return()                                                                                                    # return from this function to previous menu
        elif decision == editNames:                                                                                     # if decision is '2', edit names
            addStock(NAMES, PRICES, EXPOSURE)                                                                           # call addStock function, so if user makes a change to the key somehow they can input all other variables as well
        elif decision == editPrices:                                                                                    # if decision is '3', edit prices
            addPrices(PRICES)                                                                                           # call addprices function, so user can change prices in the chosen key
        elif decision == editRisk:                                                                                      # if decision is '4', edit exposure
            addExposure(EXPOSURE)                                                                                       # call addexposure function, so user can change the exposures in the chosen key
    return(NAMES, PRICES, EXPOSURE)                                                                                     # return the three dictionaries to the main function

def getSale(NAMES, PRICES, EXPOSURE):                                                                                   # This is the assignment for next week
    names = []                                                                                                          # makes an empty list called names
    prices = []                                                                                                         # makes an empty list called prices
    exposure = []                                                                                                       # makes an empty list called exposure
    bestSale = []                                                                                                       # makes an empty list called bestSale
    
    stockName = 0                                                                                                       # creates a variable called stockName
    buyPrice = 0                                                                                                        # creates a variable called buyPrice
    sellPrice = 0                                                                                                       # creates a variable called sellPrice
    risk = 0                                                                                                            # creates a variable called risk
    ownedShares = 0                                                                                                     # creates a variable called ownedShares
    expectedValue = 0                                                                                                   # creates a variable called expectedValue

    for key in NAMES:                                                                                                   # For each item in Names
        names += [NAMES.get(key)]                                                                                       # assign the value of that key to a new slot in the prices list
        prices = PRICES.get(key)                                                                                        # look at the key, used in the for loop, and store the values of that key from PRICES to the prices list
        buyPrice = float(prices[0].lstrip('$'))                                                                         # look at the prices list slot 0, remove the dollar sign and make it a float, then assign the outcome to buyPrice
        sellPrice = float(prices[1].lstrip('$'))                                                                        # look at the prices list slot 1, remove the dollar sign and make it a float, then assign the outcome to sellPrice
        exposure = EXPOSURE.get(key)                                                                                    # look at the values assigned to the key used in the for look and temporarily assign them to the exposure list
        ownedShares = float(exposure[0])                                                                                # look at the first number in the exposure list, make it a float, and give this value to ownedShares
        risk = float(exposure[1].strip('%'))                                                                            # lok at the second item in the exposure list, take away the % sign, and make it a float. Give this value to risk
        risk = risk/100                                                                                                 # divide the value of risk by 100, to properly format it into a numerical percentage
        expectedValue = ((sellPrice - buyPrice) - risk * sellPrice) * ownedShares                                       # expectedValue is given (sellPrice - buyPrice)-(risk * sellPrice)*ownedShares
        bestSale += [expectedValue]                                                                                     # add the expected value to the bestSale list as its own section or the list
    if len(bestSale)!= 0:                                                                                               # if length of bestSale doesn't equal 0
        maxValue = max(bestSale)                                                                                        # maxValue is the maximum value in the bestSale list
        maxIndex = bestSale.index(maxValue)                                                                             # maxIndex is given the index that the maxValue of bestSale is in
        maxValue = makeMoney(maxValue)                                                                                  # format maxValue into american currency
        print('We recommend you sell', names[maxIndex], 'for a', maxValue, 'profit.')                                   # let user know what will give them the most money for selling now
    return()                                                                                                            # return to main menu

def main():                                                                                                             # This is the main program/Loop
    searchStocks = 1                                                                                                    # This is a variable for menu options
    newStock = 2                                                                                                        # This is a variable for menu options
    editStock = 3                                                                                                       # This is a variable for menu options
    recommendSale = 4                                                                                                   # This is a variable for menu options
    leaveProgram = 5                                                                                                    # This is a variable for menu options

    choice = 0                                                                                                          # set choice variable to 0, so we can enter the main game loop.
    
    while choice != leaveProgram:                                                                                       # While choice doesn't equal leaveProgram or '5'
        choice = mainMenu(choice)                                                                                       # Calls the main menu, returns the choice, and assigns it the choice variable
        if choice == searchStocks:                                                                                      # if choice == 1 'a.k.a. searchStocks'
            searchPortfolio(NAMES, PRICES, EXPOSURE)                                                                    # Calls searchPortfolio function to search for items in your portfolio
        elif choice == newStock:                                                                                        # if choice == 2 'a.k.a. newStock'
            addStock(NAMES, PRICES, EXPOSURE)                                                                           # calls addStock function to add new stocks to your portfolio
        elif choice == editStock:                                                                                       # if choice == 3 'a.k.a. editStock'
            editPortfolio(NAMES, PRICES, EXPOSURE)                                                                      # calls the editPortfolio function to edit stocks in your portfolio
        elif choice == recommendSale:                                                                                   # if choice == 4 'a.k.a. recommendSale'
            getSale(NAMES, PRICES, EXPOSURE)                                                                            # calls the getSale function passing the 3 dictionaries as arguments.
    input('Press ENTER to Close Portfolio')                                                                             # Prompt user the press ENTER to close the program

main()                                                                                                                  # calls the main function, to run the program.
