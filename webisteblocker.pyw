import time
from datetime import datetime as dt
import mysql.connector as sqltor

def user(a, b, c):
    while True:
        query = "INSERT INTO block (name, starting_time, ending_time) VALUES ('{}', '{}', '{}')".format(a, b, c)
        cursor.execute(query)
        mycon.commit()
        print("Rows affected:", cursor.rowcount)
        return query

# Establishing the connection
mycon = sqltor.connect(host="localhost", user="root", password="root", database="abc")
cursor = mycon.cursor()

# Creating the table
cursor.execute("CREATE TABLE IF NOT EXISTS block (name VARCHAR(30), starting_time VARCHAR(30), ending_time VARCHAR(30))")
print("Table block created successfully")

# Path to the hosts file
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

# Localhost's IP
redirect = "127.0.0.1"

# Websites to block
website_list = []
l = int(input("Enter the number of websites you want to block: "))
for i in range(l):
    a = input("Enter the address of the website you want to block: ")
    website_list.append(a)

while True:
    print("Choose 1 to input")
    print("Choose 2 to continue")
    choice = int(input("Enter your choice: ")) 
    if choice == 1:
        x = input("Enter your name: ")
        y = int(input("Enter time to start studying (in 24-hour format): "))
        z = int(input("Enter time to end studying (in 24-hour format): "))
        
        user(x, y, z)
        
        query = "SELECT * FROM block"
        cursor.execute(query)
        data = cursor.fetchall()
        for record in data:
            print(record)
        
        while True: 
            # Time of your work
            if dt(dt.now().year, dt.now().month, dt.now().day, y) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, z): 
                print("Study hours")
                with open(hosts_path, 'r+') as file: 
                    content = file.read()
                    for website in website_list: 
                        if website not in content:
                            # Mapping hostnames to your localhost IP address
                            file.write(redirect + " " + website + "\n")
            else: 
                with open(hosts_path, 'r+') as file: 
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    # Removing hostnames from host file
                    file.truncate()
                print("Fun hours")
            time.sleep(5)
                
    if choice == 2:
        break

# Close the database connection
mycon.close()
