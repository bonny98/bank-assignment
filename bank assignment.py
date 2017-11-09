import pymysql


def mainmenu():
    
    print('\n')
    print('1.Bank')
    print('2.Quit')
    choice2 = input('Enter your choice: ')

    while choice2 < 3:
        if choice2 == 1:
            bank()
            

        if choice2 == 2:
            exit(0)


def bank():
    
    print('\n')
    print('1.Bank1')
    print('2.Bank2')
    choice1 = input('Enter your choice: ')

    while choice1 <3:
        
        if choice1 == 1:
            bank = bank1()
            bank.person()
        
        if choice1 == 2:
            bankr = bank2()
            bankr.person()


class bank1():
    
    connection = pymysql.connect("localhost","root","","" )
    cursor = connection.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS bank1")
    cursor.close()
    connection.close()

    connection = pymysql.connect("localhost","root","","bank1" )
    cursor = connection.cursor()
    cursor.execute( "CREATE TABLE IF NOT EXISTS customer(customerId INT PRIMARY KEY ,name VARCHAR(30) NOT NULL, address VARCHAR(20) NOT NULL, phoneNo INT NOT NULL, acctNo INT NOT NULL)")
    cursor.execute( "CREATE TABLE IF NOT EXISTS teller(tellerId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL)")
    cursor.execute( "CREATE TABLE IF NOT EXISTS bank(bankId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL, Location VARCHAR(20) NOT NULL)")
    cursor.execute( "CREATE TABLE IF NOT EXISTS account(accountId INT PRIMARY KEY, status VARCHAR(30) NOT NULL, amount INT NOT NULL, customerId INT REFERENCES customer(customerId) )")
    cursor.execute( "CREATE TABLE IF NOT EXISTS loan(loanId INT PRIMARY KEY ,Type VARCHAR(30) NOT NULL,amount INT NOT NULL, accountId INT NOT NULL, customerId INT REFERENCES customer(customerId))")

    cursor.close()
    connection.close()
    
    def person(self):
        print('\n')
        print('1.Teller')
        print('2.Customer')
        choice1 = input('Enter your choice: ')

        while choice1 < 3:
            if choice1 == 1:
                teller(bank1)

            if choice1 == 2:
                Usermenu(bank1)


class bank2():
    
    connection = pymysql.connect("localhost","root","","" )
    cursor = connection.cursor()
    cursor.execute( "CREATE DATABASE IF NOT EXISTS bank2")
    cursor.close()
    connection.close()

    connection = pymysql.connect("localhost","root","","bank2" )
    cursor = connection.cursor()
    cursor.execute( "CREATE TABLE IF NOT EXISTS customer(customerId INT PRIMARY KEY ,name VARCHAR(30) NOT NULL, address VARCHAR(20) NOT NULL, phoneNo INT NOT NULL, acctNo INT NOT NULL)")
    cursor.execute( "CREATE TABLE IF NOT EXISTS teller(tellerId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL)")
    cursor.execute( "CREATE TABLE IF NOT EXISTS bank(bankId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL, Location VARCHAR(20) NOT NULL)")
    cursor.execute( "CREATE TABLE IF NOT EXISTS account(accountId INT PRIMARY KEY, status VARCHAR(30) NOT NULL, amount INT NOT NULL, customerId INT REFERENCES customer(customerId) )")
    cursor.execute( "CREATE TABLE IF NOT EXISTS loan(loanId INT PRIMARY KEY ,Type VARCHAR(30) NOT NULL, amount INT NOT NULL, accountId INT NOT NULL, customerId INT REFERENCES customer(customerId))")
    
    cursor.close()
    connection.close()
    
    
    def person(self):
        print('\n')
        print('1.Teller')
        print('2.Customer')
        choice1 = input('Enter your choice: ')

        while choice1 < 3:
            if choice1 == 1:
                teller1(bank2)

            if choice1 == 2:
                Usermenu1(bank2)

    
    
def Usermenu(bank):
    
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bank1',autocommit=True)
    cursor = connection.cursor()
    
    print('\n')
    print('1.Open Account For New Customer')
    print('2.Deposit Amount')  
    print('3.Withdraw Amount')
    print('4.Close Account')                              
    print('5.loan')
    print('6.loan repay')
    print('7.Logout')
    choice = input('Enter your choice: ')


    while choice < 8:
        
        if choice == 1:
            customerid = input('CustomerId: ')
            name = raw_input('Name: ')
            Address = raw_input('Address: ')
            phoneNo = input('PhoneNo: ')            
            acctNo = input('AccountNo: ')
            acctId = input('AccountId: ')
            acctType = raw_input('AccountType savings account or checking account: ')
            Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

            query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
            query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
            
            if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                    print('Thanks for creating a new account with us!')
                    Usermenu(bank)
                else:
                    print('amount not deposited')
                    Usermenu(bank)   
                                
        if choice == 2:
            name = raw_input('Name : ')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Amount :')
                        
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                        print('Your amount was deposited!')
                        Usermenu(bank)
                    else:
                        print('amount not deposited')
                        Usermenu(bank)
                                                                        
        if choice == 3:
                        
            Name = raw_input('Name : ')
            customerid = input('customerId : ')
            account_number = input('Account Number :')	
            amount1 = input('Amount :')
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount - %s WHERE customerId = %s ",(amount1,customerid))):
                                
                        print('Your amount was withdrawn!')
                        Usermenu(bank)
                    else:
                        print('amount not withdrawn')
                        
                        Usermenu(bank)

                        
        if choice == 4:
            Name = raw_input('Name : ')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                    print('Account Closed!')
                    Usermenu(bank)
                else:
                    print('Account not Closed')
                    Usermenu(bank)

        
        if choice == 5:
            
            loan_Id = input('Loan_Id:')
            loan_Type = raw_input('Loan_Type:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            account_Id = input('Account_Id:')
            LoanAmount = input('LoanAmount :')

            query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                
                        print('Loan processed!')
                        Usermenu(bank)
                    else:
                        print('Loan not processed')
                        
                        Usermenu(bank)

        if choice == 6:
            
            loan_Id = input('Loan_Id:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Loan Amount payment :')

           
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                        print('Loan processed!')
                        Usermenu(bank)
                    else:
                        print('Loan not processed')
                        
                        Usermenu(bank)

        if choice == 7:
            mainmenu()
            break
        
        else:
            print('Invalid option!')
            Usermenu(bank)

    cursor.close()
    connection.close()

def teller(bank):
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bank1',autocommit=True)
    cursor = connection.cursor()

    def teller_operations(bank):

        connection = pymysql.connect(host='localhost',user='root',passwd='',db='bank1',autocommit=True)
        cursor = connection.cursor()
        
        print('\n')
        print('1.Open Account For New Customer')
        print('2.Collect & Deposit money')                                                 
        print('3.Close Account')
        print('4.process Loan')
        print('5.Logout')
        
        choice = input('Enter your choice: ')

        while choice <7:
            
            if choice == 1:
                customerid = input('CustomerId: ')
                name = raw_input('Name: ')
                Address = raw_input('Address: ')
                phoneNo = input('PhoneNo: ')            
                acctNo = input('AccountNo: ')
                acctId = input('AccountId: ')
                acctType = raw_input('AccountType savings account or checking account: ')
                Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

                query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
                query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
                
                if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                    if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                        print('Thanks for creating a new account with us!')
                        teller_operations(bank)
                    else:
                        print('amount not deposited')
                        teller_operations(bank)

            if choice == 2:
                name = raw_input('Name : ')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Amount :')
                            
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                            print('Your amount was deposited!')
                            teller_operations(bank)
                        else:
                            print('amount not deposited')
                            teller_operations(bank)
                                    

            if choice == 3:
                Name = raw_input('Name : ')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                        print('Account Closed!')
                        teller_operations(bank)
                    else:
                        print('Account not Closed')
                        teller_operations(bank)

                        
            if choice == 4:
            
                loan_Id = input('Loan_Id:')
                loan_Type = raw_input('Loan_Type:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                account_Id = input('Account_Id:')
                LoanAmount = input('LoanAmount :')

                query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
                
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                    
                            print('Loan processed!')
                            teller_operations(bank)
                        else:
                            print('Loan not processed')
                            
                            teller_operations(bank)
                            
            if choice == 5:
                loan_Id = input('Loan_Id:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Loan Amount payment :')

                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                            print('Loan processed!')
                            teller_operations(bank)
                        else:
                            print('Loan not processed')
                            
                            teller_operations(bank)

            
            if choice == 6:
                mainmenu()
                break
            else:
                print('Invalid option!')
                teller_operations(bank)

        cursor.close()
        connection.close()
        
    name = raw_input('Name : ')
    tellerid = input('tellerId : ')

    if(cursor.execute( "SELECT * FROM teller WHERE tellerId = %s AND Name = %s",(tellerid,name))):
        teller_operations(bank)

def Usermenu1(bank):
    
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bank2',autocommit=True)
    cursor = connection.cursor()
    
    print('\n')
    print('1.Open Account For New Customer')
    print('2.Deposit Amount')  
    print('3.Withdraw Amount')
    print('4.Close Account')                              
    print('5.loan')
    print('6.loan repay')
    print('7.Logout')
    choice = input('Enter your choice: ')


    while choice < 8:
        
        if choice == 1:
            customerid = input('CustomerId: ')
            name = raw_input('Name: ')
            Address = raw_input('Address: ')
            phoneNo = input('PhoneNo: ')            
            acctNo = input('AccountNo: ')
            acctId = input('AccountId: ')
            acctType = raw_input('AccountType: savings or checking: ')
            Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

            query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
            query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
            
            if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                    print('Thanks for creating a new account with us!')
                    Usermenu1(bank)
                else:
                    print('amount not deposited')
                    Usermenu1(bank)   
                                
        if choice == 2:
            name = raw_input('Name : ')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Amount :')
                        
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                        print('Your amount was deposited!')
                        Usermenu1(bank)
                    else:
                        print('amount not deposited')
                        Usermenu1(bank)
                                                                        
        if choice == 3:
                        
            Name = raw_input('Name : ')
            customerid = input('customerId : ')
            account_number = input('Account Number :')	
            amount1 = input('Amount :')
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount - %s WHERE customerId = %s ",(amount1,customerid))):
                                
                        print('Your amount was withdrawn!')
                        Usermenu1(bank)
                    else:
                        print('amount not withdrawn')
                        
                        Usermenu1(bank)

                        
        if choice == 4:
            Name = raw_input('Name : ')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                    print('Account Closed!')
                    Usermenu1(bank)
                else:
                    print('Account not Closed')
                    Usermenu1(bank)

        
        if choice == 5:
            
            loan_Id = input('Loan_Id:')
            loan_Type = raw_input('Loan_Type:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            account_Id = input('Account_Id:')
            LoanAmount = input('LoanAmount :')

            query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                
                        print('Loan processed!')
                        Usermenu1(bank)
                    else:
                        print('Loan not processed')
                        
                        Usermenu1(bank)

        if choice == 6:
            
            loan_Id = input('Loan_Id:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Loan Amount payment :')

           
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                        print('Loan processed!')
                        Usermenu1(bank)
                    else:
                        print('Loan not processed')
                        
                        Usermenu1(bank)

        if choice == 7:
            mainmenu()
            break
        
        else:
            print('Invalid option!')
            Usermenu1(bank)

    cursor.close()
    connection.close()

def teller1(bank):
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bank2',autocommit=True)
    cursor = connection.cursor()

    def teller_operations1(bank):

        connection = pymysql.connect(host='localhost',user='root',passwd='',db='bank2',autocommit=True)
        cursor = connection.cursor()
        
        print('\n')
        print('1.Open Account For New Customer')
        print('2.Collect & Deposit money')                                                 
        print('3.Close Account')
        print('4.process Loan')
        print('5.Logout')
        
        choice = input('Enter your choice: ')

        while choice <7:
            
            if choice == 1:
                customerid = input('CustomerId: ')
                name = raw_input('Name: ')
                Address = raw_input('Address: ')
                phoneNo = input('PhoneNo: ')            
                acctNo = input('AccountNo: ')
                acctId = input('AccountId: ')
                acctType = raw_input('AccountType savings account or checking account: ')
                Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

                query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
                query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
                
                if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                    if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                        print('Thanks for creating a new account with us!')
                        teller_operations1(bank)
                    else:
                        print('amount not deposited')
                        teller_operations1(bank)

            if choice == 2:
                name = raw_input('Name : ')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Amount :')
                            
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                            print('Your amount was deposited!')
                            teller_operations1(bank)
                        else:
                            print('amount not deposited')
                            teller_operations1(bank)
                                    

            if choice == 3:
                Name = raw_input('Name : ')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                        print('Account Closed!')
                        teller_operations1(bank)
                    else:
                        print('Account not Closed')
                        teller_operations1(bank)

                        
            if choice == 4:
            
                loan_Id = input('Loan_Id:')
                loan_Type = raw_input('Loan_Type:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                account_Id = input('Account_Id:')
                LoanAmount = input('LoanAmount :')

                query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
                
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                    
                            print('Loan processed!')
                            teller_operations1(bank)
                        else:
                            print('Loan not processed')
                            
                            teller_operations1(bank)
                            
            if choice == 5:
                loan_Id = input('Loan_Id:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Loan Amount payment :')

                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                            print('Loan processed!')
                            teller_operations1(bank)
                        else:
                            print('Loan not processed')
                            
                            teller_operations1(bank)

            
            if choice == 6:
                mainmenu()
                break
            else:
                print('Invalid option!')
                teller_operations1(bank)

        cursor.close()
        connection.close()
        
    name = raw_input('Name : ')
    tellerid = input('tellerId : ')

    if(cursor.execute( "SELECT * FROM teller WHERE tellerId = %s AND Name = %s",(tellerid,name))):
        teller_operations1(bank)
     
mainmenu()
