###############WELCOME TO HOTEL PANDA#############
##############DESIGNED BY SWASTIK PANDA###########
import mysql.connector
#ESTABLISHING MYSQL CONNECTION
uname=input('Enter Login Id:')
password=input('Enter Password:')
if uname=='root':
   mycon=mysql.connector.connect(host='localhost', username=uname, passwd=password)
   cursor=mycon.cursor()
   cursor.execute("CREATE DATABASE IF NOT EXISTS PANDA")
   cursor.execute("COMMIT")
   cursor.close()
   if mycon.is_connected():
      print("Login Sucessful")
else:
    print('Invalid Login Credentials!')
   
#ENTERING CUSTOMER DETAILS
def customerEntry():
  global cid
  cursor=mycon.cursor()
  cursor.execute('USE PANDA')
  createTable='CREATE TABLE IF NOT EXISTS C_Details(CID INT, NAME VARCHAR(30), ADDRESS VARCHAR(30), AGE INT, PHONENO INT)'
  cursor.execute(createTable)
  cid = input("Enter Customer Identification Number : ")
  name = input("Enter Customer Name : ")
  address = input("Enter Customer Address : ")
  age= input("Enter Customer Age : ")
  phoneno= input("Enter Customer Contact Number : ")
  print('New Customer Entered In The System Successfully !')
  sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s)"
  values= (cid,name,address,age,phoneno)
  cursor.execute(sql,values)
  cursor.execute("COMMIT")
  cursor.close()

#BOOKING DETAILS
def bookingdetails():
    global cid
    cursor=mycon.cursor()
    createTable ="CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE)"
    cursor.execute('USE PANDA')
    cursor.execute(createTable)
    cid = input("Enter Customer Identification Number : ")
    checkin=input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
    checkout=input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
    sql= "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
    values= (cid,checkin,checkout)
    cursor.execute(sql,values)
    cursor.execute("COMMIT")
    print("\nBOOKING DETAILS ENTERED SUCCESSFULLY !")
    cursor.close()
#ROOM DETAILS
def roomRent():
 global cid
 global roomrent
 cursor=mycon.cursor()
 cursor.execute('USE PANDA')
 createTable ='CREATE TABLE IF NOT EXISTS ROOM(CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)'
 cursor.execute(createTable)
 cid = input("Enter Customer Identification Number : ")
 print ("\n ##### We have The Following Rooms For You #####")
 print (" 1. SUPER DELUXE ----> 3000 Rs.")
 print (" 2. DELUXE ----> 2000 Rs. ")
 print (" 3. SUITE----> 1500 Rs. ")
 print (" 4. ECONOMY ----> 1000 Rs")
 roomchoice=int(input("Enter Your Option : "))
 roomno=int(input("Enter Customer Room No : "))
 noofdays=int(input("Enter No. Of Days : "))
 if roomchoice==1:
  roomrent = noofdays * 3000
  print("\nULTRA DELUXE ROOM RENT : ",roomrent)
 elif roomchoice==2:
  roomrent = noofdays * 2000
  print("\nDELUXE ROOOM RENT : ",roomrent)
 elif roomchoice==3:
  roomrent = noofdays * 1500
  print("\nSUITE ROOM RENT : ",roomrent)
 elif roomchoice==4:
  roomrent = noofdays * 1000
  print("\nECONOMY ROOM RENT : ",roomrent)
 else:
   print('YOU HAVE ENTERED WRONG INPUT! TRY AGAIN')
 sql= "INSERT INTO ROOM VALUES(%s,%s,%s,%s,%s)"
 values= (cid,roomchoice,noofdays,roomno,roomrent)
 cursor.execute(sql,values)
 cursor.execute("COMMIT")
 print("Thank You , Your Room Has Been Booked For : ",noofdays , "Days" )
 print("Your Total Room Rent is : Rs. ",roomrent)
 cursor.close()
 return roomrent
#TOTAL BILL
def totalamount():
 global cid
 global grandTotal
 global roomrent
 cursor=mycon.cursor()
 cursor.execute('USE PANDA')
 createTable ="CREATE TABLE IF NOT EXISTS BILL(CID VARCHAR(20),C_NAME VARCHAR(30),ROOMRENT INT ,TOTALAMOUNT INT)"
 cursor.execute(createTable)
 sql= "INSERT INTO BILL VALUES(%s,%s,%s,%s)"
 name = input("Enter Customer Name : ")
 cid = input("Enter Customer Identification Number : ")
 grandTotal=r
 values= (cid,name,r,grandTotal)
 cursor.execute(sql,values)
 cursor.execute("COMMIT")
 cursor.close()
 print("\n **** HOTEL PANDA****CUSTOMER BILL****")
 print("\n CUSTOMER NAME : " ,name)
 print("\nROOM RENT : Rs. ",r)
 print("___________________________________________________")
 print("\nTOTAL AMOUNT : Rs. ",grandTotal)


#SEARCHING CUSTOMER DETAILS
def search():
  global cid
  b=int(input('Enter Customer Identification Number :'))
  a=(b,)
  print('You Have The Following Choices', '1-----> CUSTOMER DETAILS', '2---->BOOKING RECORD','3---->ROOM TYPE', '4-----> TOTAL BILL')
  choice=int(input('Enter Your Choice:'))
  cursor=mycon.cursor()
  cursor.execute('USE PANDA')
  if choice==1:
   cursor=mycon.cursor()
   cursor.execute('SELECT * FROM C_DETAILS WHERE CID=%s', a)
   t=cursor.fetchone()
   if t==None:
       print('No Records Found')
   else:
    print('Customer Details Are')
    print(t)
  elif choice==2:
    cursor=mycon.cursor()
    cursor.execute('SELECT * FROM BOOKING_RECORD WHERE CID=%s', a)
    r=cursor.fetchone()
    if r==None:
        print('No Records Found')
    else:
      print('Customer\'s Booking Details Are:')
      print(r)
  elif choice==3:
    cursor=mycon.cursor()
    cursor.execute('SELECT * FROM ROOM WHERE CID=%s', a)
    s=cursor.fetchone()
    if s==None:
        print('No Records Found')
    else:
     print('Customer\'s Room Details Are')
     print(s)
  elif choice==4:
     cursor=mycon.cursor()
     cursor.execute('SELECT * FROM BILL WHERE CID=%s', a)
     p=cursor.fetchone()
     if p==None:
        print('No Records Found')
     else: 
      print('Customer\'s Bill Details are')
      print(p)  
#UPDATING AND DELETING CUSTOMER DETAILS
def modify():
  global cid
  cursor=mycon.cursor()
  cursor.execute('USE PANDA')
  b=input('Enter CID Number:')
  a=(b,)
  print('You Have The Following Choices')
  print('1---->UPDATE')
  print('2----->DELETE')
  d=int(input('Enter your choice:'))

  if d==1:
     print('Fields are 1.NAME,2.AGE,3.PHONENO,4.ADDRESS') 
     c=int(input('Choose Field To Update:'))
     if c==1:
          f=input('Enter New Name:')
          e="UPDATE C_DETAILS SET NAME ='{}' WHERE CID = {}".format(f,b)
          cursor.execute(e)
          cursor.execute("COMMIT")
          print('Record Updated Sucessfully')
     elif c==2:
          h=input('Enter New Age:')
          k="UPDATE C_DETAILS SET AGE ={} WHERE CID = {}".format(h,b)
          cursor.execute(k)
          cursor.execute("COMMIT")
          print('Record Updated Sucessfully')
     elif c==3:
          o=input('Enter New Phoneno:')
          u="UPDATE C_DETAILS SET PHONENO ={} WHERE CID = {}".format(o,b)
          cursor.execute(u)
          cursor.execute("COMMIT")
          print('Record Updated Sucessfully')
     elif c==4:
          l=input('Enter New Address:')
          p="UPDATE C_DETAILS SET ADDRESS ='{}' WHERE CID = {}".format(l,b)
          cursor.execute(p)
          cursor.execute("COMMIT")
          print('Record Updated Sucessfully')
    
  elif d==2:
          print('Record deleted successfully')
          e='DELETE FROM C_DETAILS WHERE CID = %s'
          cursor.execute(e,a)
          cursor.execute("COMMIT")
     
 
#MAIN PROGRAM
if uname=='root':
    print('WELCOME TO HOTEL PANDA')
    print("""
1--->Enter Customer Details
2--->Booking Record
3--->Calculate Room Rent
4--->Display Customer Details
5--->Generate Total Bill
6--->Modify
    """)
    ans='y'
    while ans=='y':
      choice = int(input("Enter Your Choice:"))
      if choice == 1:
         customerEntry()
         ans=input("Do you want to continue(y/n)?")
      elif choice ==2:
         bookingdetails()
         ans=input("Do you want to continue(y/n)?")
      elif choice ==3:
         r=roomRent()
         ans=input("Do you want to continue(y/n)?")
      elif choice ==5:
         totalamount()
         ans=input("Do you want to continue(y/n)?")
      elif choice==4:
        search()
        ans=input("Do you want to continue(y/n)?")
      elif choice==6:
        modify()
        ans=input("Do you want to continue(y/n)?")
      else:
         print("Please Enter Valid Choice")
         ans='y'
    else:
      print("Thank You")


    
#THE PROGRAM ENDS HERE
#THANK YOU
