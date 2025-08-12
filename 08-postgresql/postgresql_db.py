
import psycopg2

# Setting as 'None' in case connection statement doesn't succeed.
conn = None

try: 
    with psycopg2.connect(
        database='Python DB',
        user='postgres',
        password='admin123',
        host='localhost',
        port='5432'
    ) as conn:

        with conn.cursor() as cur: 

            cur.execute('DROP TABLE IF EXISTS Employees;')

            # Creating Table
            create_script = """
            CREATE TABLE Employees (
            id SERIAL PRIMARY KEY,
            f_name varchar(30),
            l_name varchar(30),
            salary int,
            dept varchar(30)
            );
            """

            cur.execute(create_script)

            # CREATE - Data Insertion
            insert_script = """
            INSERT INTO Employees (f_name, l_name, salary, dept) 
            VALUES (%s, %s, %s, %s);
            """

            insert_values = [
            ('Amal', 'Basit', 50000, 'HR'),
            ('Ali', 'Raza', 52000, 'Finance'),
            ('Sara', 'Khan', 55000, 'Marketing'),
            ('Ahmed', 'Malik', 53000, 'IT'),
            ('Zainab', 'Shah', 51000, 'Sales'),
            ('Hassan', 'Javed', 57000, 'IT'),
            ('Maria', 'Siddiqui', 56000, 'Marketing'),
            ('Tariq', 'Mehmood', 54000, 'Finance'),
            ('Nadia', 'Farooq', 50000, 'HR'),
            ('Bilal', 'Aslam', 60000, 'IT'),
            ('Fahad', 'Nadeem', 53000, 'Sales'),
            ('Ayesha', 'Imran', 51000, 'Marketing'),
            ('Usman', 'Chaudhry', 62000, 'Finance'),
            ('Hina', 'Qureshi', 58000, 'HR'),
            ('Kamran', 'Saeed', 57000, 'Sales'),
            ('Samina', 'Babar', 54000, 'IT'),
            ('Ibrahim', 'Ali', 56000, 'Finance'),
            ('Anam', 'Jamil', 50000, 'Marketing'),
            ('Waleed', 'Shafiq', 61000, 'IT'),
            ('Shazia', 'Hassan', 52000, 'HR'),
            ('Imran', 'Yousaf', 53000, 'Finance'),
            ('Mehwish', 'Naseer', 55000, 'Sales'),
            ('Noman', 'Iqbal', 57000, 'IT'),
            ('Beenish', 'Rafiq', 60000, 'Marketing'),
            ('Zoya', 'Mir', 54000, 'Finance'),
            ('Adeel', 'Bhatti', 52000, 'Sales'),
            ('Noor', 'Hameed', 53000, 'IT'),
            ('Talha', 'Aziz', 51000, 'HR'),
            ('Kiran', 'Akhtar', 50000, 'Marketing'),
            ('Rehan', 'Zafar', 56000, 'Finance'),
            ('Iqra', 'Nawaz', 58000, 'Sales'),
            ('Danish', 'Tariq', 60000, 'IT'),
            ('Hoor', 'Amjad', 52000, 'HR'),
            ('Asim', 'Rashid', 59000, 'Marketing'),
            ('Lubna', 'Munir', 51000, 'Sales')
            ]

            for data in insert_values:
                cur.execute(insert_script, data)


            # READ DATA - Data Retrieval  

            # Display all Data
            cur.execute("SELECT * FROM EMPLOYEES;") 
            print("All Employee Records:\n")
            for result in cur.fetchall():
                print(result)
            print('\n')

            # Display Employees Not in Finance or Marketing Department
            cur.execute(
                """
                SELECT f_name, l_name, dept
                FROM Employees
                WHERE dept NOT IN ('Finance', 'Marketing');
                """
            )
            print("Employees NOT in Finance or Marketing Department:\n")
            for result in cur.fetchall():
                print(result)
            print('\n')

            # Count how many employees have Salary < 56,000 and l_name starting with A.
            cur.execute(
                """
                SELECT COUNT(*) 
                FROM Employees
                WHERE Salary < 56000 AND l_name LIKE 'A%';
                """
            )

            print("Count of Employees with salary < 56000 and last name starting with 'A':")
            print(cur.fetchone()[0])
            print('\n')

            # Find the average salary for each department
            cur.execute(
                """
                    SELECT dept, AVG(salary)
                    FROM Employees
                    GROUP BY dept;
                """
            )
            
            print("Average Salary by Department:\n")
            for dept, salary in cur.fetchall():
                print(f"{dept}      {salary:.2f}")
            print('\n')


            # UPDATE - Modifying Existing Records

            # Update f_name and dept of an employee
            cur.execute(
                """
                    UPDATE Employees
                    SET f_name = 'Sahar', dept = 'IT'
                    WHERE id = 1;
                """
            )
            cur.execute(
                """
                    SELECT *
                    FROM Employees
                    WHERE id = 1;
                """
            )
            print("Updated record for Employee with id = 1:\n")
            print(cur.fetchall()[0], '\n')

            # Update dept as 'Admin' for all whose salary is < 50000
            cur.execute(
                """
                    UPDATE Employees
                    SET dept = 'Admin'
                    WHERE salary < 52000;
                """
            )
            cur.execute(
                """
                    SELECT f_name, l_name, salary
                    FROM Employees
                    WHERE dept = 'Admin';
                """
            )

            print("Employees moved to 'Admin' department (salary < 52000):\n")
            for result in cur.fetchall():
                print(result)
            print("\n")

            # DELETE - Remove Existing Records

            # Delete Employees with Salary >= 60,000
            cur.execute(
                """
                    DELETE FROM Employees
                    WHERE salary >= 60000
                """
            )

            cur.execute(
                """
                    SELECT f_name, l_name
                    FROM Employees
                    WHERE salary >= 60000
                """
            )
            
            rows = cur.fetchall()

            if not rows:
                print("All employees with salary >= 60000 have been deleted.\n")
            else:
                for row in rows:
                    print(row)

            # Delete employees whose last names start with the letter 'Z'.

            cur.execute(
                """
                    DELETE FROM Employees
                    WHERE l_name LIKE 'Z%'
                """
            )

            cur.execute(
                """
                    SELECT f_name, l_name
                    FROM Employees
                    WHERE l_name LIKE 'Z%'
                """
            )
            
            rows = cur.fetchall()

            if not rows:
                print("All employees with last name beginning with 'Z' have been deleted.\n")
            else:
                for row in rows:
                    print(row) 

            # Order by 'id' in ascending order

            cur.execute(
                '''
                    SELECT *
                    FROM Employees
                    ORDER BY id ASC
                '''
            )

            print("Final Employee List (Ordered by ID Ascending):\n")
            for data in cur.fetchall():
                print(data)
            print('\n')

            # No need to commit, as conn context manager handles that once exited


except Exception as e:
    print("An error occurred: ", e)

finally:
    if conn is not None:
        conn.close()