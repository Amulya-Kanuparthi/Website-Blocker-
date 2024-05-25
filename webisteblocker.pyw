import time
from datetime import datetime as dt
import mysql.connector as sqltor

def user(a, b, c):
    query = "INSERT INTO block (name, starting_time, ending_time) VALUES (%s, %s, %s)"
    cursor.execute(query, (a, b, c))
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
        y = int(input("Enter time to start studying (in 24-hour format, e.g., 13 for 1 PM): "))
        z = int(input("Enter time to end studying (in 24-hour format, e.g., 15 for 3 PM): "))

        user(x, y, z)

        query = "SELECT * FROM block"
        cursor.execute(query)
        data = cursor.fetchall()
        for record in data:
            print(record)
        
        while True: 
            current_time = dt.now()
            start_time = dt(current_time.year, current_time.month, current_time.day, y)
            end_time = dt(current_time.year, current_time.month, current_time.day, z)

            if start_time < current_time < end_time:
                print("Study hours")
                with open(hosts_path, 'r+') as file:
                    content = file.read()
                    for website in website_list:
                        if website not in content:
                            file.write(redirect + " " + website + "\n")
            else:
                with open(hosts_path, 'r+') as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
                print("Fun hours")

            time.sleep(5)
            # Breaking out of inner loop after one cycle
            break

    if choice == 2:
        break

# Close the database connection
mycon.close()
