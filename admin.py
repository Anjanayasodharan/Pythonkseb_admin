import mysql.connector
import sys
try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'admindb')
    mycursor = mydb.cursor()
except mysql.connector.Error as e:
        sys.exit("view data error")
mycursor=mydb.cursor()
        
while True:
    print("select an option from the menu")
    print("1 add consumer")
    print("2 search consumer ")  
    print("3 delete consumer")
    print("4 update consumer")    
    print("5 view all consumer")
    print("6 generate bill")
    print("7 view bill")
    print("8 exit")
    choice = int(input('enter an option:'))
    if(choice==1):
        print('add consumer ')
        code=input("enter the consumer code")
        name=input("enter the name ")
        address=input("enter the address")
        phno=input("enter the phone number")
        email=input("enter the email id")
        try:
            sql="INSERT INTO `consumer`(`code`, `name`, `address`, `phno`, `email`) VALUES (%s,%s,%s,%s,%s)"
            data=(code,name,address,phno,email)
            mycursor.execute(sql , data)
            mydb.commit()
            print("value inserted succesfully")
        except mysql.connector.Error as e:
            sys.exit("view data error")

        break
    elif(choice==2):
        print('search consumer selected')
        break
    elif(choice==3):
        print('delete consumer selected')
        break
    elif(choice==4):
        print('update consumer selected')
        break
    elif(choice==5):
        print('view all consumer selected')
        break
    elif(choice==6):
        print('generate bill selected')
        break
    elif(choice==7):
        print('view bill selected')
        break
    elif(choice==8):
        break
