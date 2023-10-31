#Assignment 1-Python (Banking Application)
#Name: Shreya Dasoju
#Student Number: 501166279
'''
This program allows staff members to check their account balances (chequing and savings), transfer amounts between the two
accounts, and e-transfer amounts to other people from either their chequing or savings accounts.
The program will first validate if the login information entered, matches with that of the database, and then will let them
proceed to the next steps.
'''
#Set of usernames and passwords within the database
#The username in any index of the username list, will correspond to the password in the same index of the password list.
StaffUserName = ["13579","12345","24680","31976","15200","23456","34567","56789","45678"]
StaffPassword = ["Sarah123","Shreya234","Omar345","Sally456","Rachael567","Bob678","Chris789","Anjali890","Ramesh100"]
chequing,savings,transfer,transChoice,counter,userName,passWord,CheqOrSav,LoginSuccess=17500,500650,0,0,0,"","","",False

# Function that provides users the opportunity to select what actions they want to take with their current balance.
# Takes input from the user to select from the 3 options provided
def transferFunds():
    '''
    For the sake of using the following variables in this function and other ones as well, and being able to actually
    update the value, the variable has to be changed to global instead of the default local variable.
    '''
    global chequing,savings,transfer,CheqOrSav,transChoice
    #Provides the next set of steps to the user to select, and prompts them to select from the numbers 1-3.
    print("To transfer from chequing to savings, enter '1'")
    print("To transfer from savings to chequing, enter '2'")
    print("To e-transfer money to someone, enter '3'\n")
    print("Balance in chequing: $"+str(chequing))
    print("Balance in savings: $"+str(savings))
    transChoice = int(input("\nEnter 1, 2 or 3: "))
    transfer = int(input("How much money would you like to transfer?"))
    '''
    Depending on the user's selection, the program will take the amount from chequings and move it to savings, or vice versa
    If the user selected option 3, they will be asked what account they want to move it from, and who the amount 
    should be sent to.
    '''
    #Calls the function validFunds in order to validate whether the user has enough money to actually proceed with the transaction
    #that they requested
    #Based on the selection they chose, the code will apply the changes to their balance in each account, and return the new balance
    #in both their chequing and savings accounts.
    if transChoice == 1:
        validFunds()
        chequing -= transfer
        savings += transfer
        print("*** Balance in chequing: $" + str(chequing))
        print("*** Balance in savings: $" + str(savings))
    if transChoice == 2:
        validFunds()
        chequing += transfer
        savings -= transfer
        print("*** Balance in chequing: $" + str(chequing))
        print("*** Balance in savings: $" + str(savings))
    if transChoice == 3:
        CheqOrSav = input("Would you like to transfer from your chequing account or your savings account: ")
        Recepient = input("Enter the email of the person you would like to transfer this amount to: ")
        #validFunds is called again here because unlike option 1 and 2, option 3 did not know to deduct from chequing
        #or savings until the last two lines.
        validFunds()
        if CheqOrSav == "chequing":
            chequing -= transfer
            if transfer>0:
                print("You have successfully transferred $" + str(transfer), "to", Recepient)
                print("Your current balance in your chequing account is now $" + str(chequing))
        elif CheqOrSav == "savings":
            savings -= transfer
            if transfer>0:
                print("You have successfully transferred $" + str(transfer), "to", Recepient)
            print("Your current balance in your savings account is now $" + str(savings))

    #Provides the user with the chance to continue to make from transfers or transactions in case they missed something or would
    #like to do something new.
    print("Would you like to continue to make any new transfers or transactions?")
    Continue = input("Enter 'Y' to continue or 'N' to exit:")
    if Continue == "Y":
        transferFunds()

def validFunds():
    #Purpose of this function is to ensure that the transaction will not result in a negative balance. It will stop the
    #transaction from happening if the balance will go into the negatives.
    global transfer,transChoice,chequing,savings,CheqOrSav
    if transChoice==1 and transfer>chequing:
        #transfer value is set to 0 for all the options, because no money should be deducted if it will provide the user with a negative balance.
        transfer=0
        print("Insufficent funds in chequing. Cannot transfer amount.")
    elif transChoice==2 and transfer>savings:
        transfer=0
        print("Insufficent funds in savings. Cannot transfer amount")
    elif transChoice==3:
        if CheqOrSav=="chequing" and transfer>chequing:
            transfer=0
            print("E-transfer failed. Insufficient funds.")
        elif CheqOrSav=="savings" and transfer>savings:
            transfer=0
            print("E-transfer failed. Inusfficient funds.")

def ValidStaffAccount():
    global LoginSuccess, counter, userName, passWord
    userName = input("Username: ")
    passWord = input("Password: ")
    '''
    Checks if the username that the user entered is within the list of usernames that have already been stored in the program.
    If there is a match, the variable Num will store the index of that username in the list. As mentioned in the program's description,
    the username and password with the same index in both lists, are a pair. Using the Num value, the program checks if the 
    password the user entered, matches with the password in that index. If there's a match, LoginSuccess is changed from False to 
    True.      
    '''
    if (userName in StaffUserName):
        Num = StaffUserName.index(userName)
        if (StaffPassword[Num]==passWord):
            LoginSuccess=True
    #If the username didn't have a match in the list of usernames, the counter will be increased by 1. The purpose of the counter
    #is to ensure that the program only lets the user try to login 4 times. Once the counter is greather than or equal to
    #4, it will tell the user that they've used an invalid login too many times, and to try another time.
    #If they are still within the 4 attempts, it will tell them to try again.
    else:
        counter += 1
        if counter < 4:
            print("Either the username or password you entered is incorrect. Please try again.")
        else:
            print("You've reached your maximum number of uncessful attempts. Please try again another time. Goodbye!")
    #Checks the Truth value for LoginSuccess. If it's true, your login was a success. Otherwise, the value will still remain False.
    if LoginSuccess == True:
        print("\nWelcome! Choose your next step: ")

#main program
if __name__ == "__main__":
    print("Welcome to the staff banking account! Please enter your username and password: ")
    '''
    The for loop is needed to let the user attempt to login a maximum of 4 times, as long as their login was uncessful.
    If the login was successful, it will exit the loop, and present the next steps. 
    '''
    for i in range(4):
        '''
        Initially checks if userName and passWord are even in the list of usernames and passwords. If they do not exist in
        the lists, ask the user to continue to attemp to login
        '''
        while (userName not in StaffUserName) or (passWord not in StaffPassword):
            '''
            This function is called for the final verification of the login's validity. Although the username and password may
            be valid as they exist in the lists created, they may not actually be a proper pair. This function verifies if the 
            inputted values do in fact belong to each other. 
            '''
            ValidStaffAccount()
            #breaks so that the user is not able to try to login with an incorrect username/password more than 4 times.
            break
    #If LoginSuccess is now True, proceed to the next steps upon logging in.
    if LoginSuccess == True:
        transferFunds()
