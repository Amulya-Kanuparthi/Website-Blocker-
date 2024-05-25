def user(a,b,c):
        while True:
                query="insert into block values('{}','{}','{}')".format(a,b,c)
                cursor.execute(query)
                mycon.commit( )
                print("rows affected",cursor.rowcount)
                print("****")
                return query

import time
from datetime import datetime as dt
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="root",database="abc")
cursor=mycon.cursor( )
cursor.execute("create table block(name varchar(30),starting_time varchar(30),ending_time varchar(200))")
print("table block created successfully")
# change hosts path according to your OS 
hosts_path ="C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"

# websites That you want to block
website_list=[]
l=int(input("the no of websites you wanna block"))
for i in range(l):
        a=input("enter the address of the website you want to block")
        website_list.append(a)
while True:
        print("choose 1 to input")
        print("choose 2 to continue")
        choice = int(input("enter your choice")) 
        if choice == 1:
                x =input("enter your name:")
                y = int(input("enter time to start studying"))
                z = int(input("enter time to end studying"))
                
                user(x,y,z)
                import mysql.connector as sqltor
                mycon=sqltor.connect(host='localhost',user="root",password="root",database="abc")
                cursor=mycon.cursor()
                query="select * from block"
                cursor.execute(query)
                data=cursor.fetchall()
                for i in data:
                        print(i)
                mycon.close()
       
         
                while True: 

                        # time of your work 
                        if dt(dt.now().year, dt.now().month, dt.now().day,y)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,z): 
                                print("Study hours") 
                                with open(hosts_path, 'r+') as file: 
                                        content = file.read() 
                                        for website in website_list: 
                                                if website in content: 
                                                        pass
                                                else: 
                                                        # mapping hostnames to your localhost IP address 
                                                        file.write(redirect + " " + website + "\n") 
                        else: 
                                with open(hosts_path, 'r+') as file: 
                                        content=file.readlines() 
                                        file.seek(0) 
                                        for line in content: 
                                                if not any(website in line for website in website_list): 
                                                        file.write(line) 

                                        # removing hostnmes from host file 
                                        file.truncate() 

                                print("fun hours") 
                        time.sleep(5)
                

                   
        if choice == 2:
                break
