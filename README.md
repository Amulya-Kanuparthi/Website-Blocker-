# Website-Blocker-
The provided Python script performs the following tasks:

1. Database Setup:
   - Establishes a connection to a MySQL database using `mysql.connector`.
   - Creates a table named `block` if it does not already exist. This table stores the user's name and study times.

2. User Input:
   - Prompts the user to input a list of websites they want to block.
   - Allows the user to input their name and study times (start and end times in 24-hour format).

3. Database Operations:
   - Inserts the user's name and study times into the `block` table.
   - Retrieves and displays all records from the `block` table.

4. Hosts File Modificatio:
   - During the specified study hours, the script blocks the input websites by redirecting them to `127.0.0.1` in the system's hosts file.
   - Outside of the study hours, it removes these redirections from the hosts file.

5. Continuous Monitoring:
   - The script runs an infinite loop where it continuously checks the current time against the user's specified study hours every 5 seconds.
   - Depending on the time, it either blocks or unblocks the specified websites.

6. Cleanup:
   - Closes the database connection when the user chooses to exit the program.

This script is designed to help users stay focused by blocking distracting websites during their designated study times.
