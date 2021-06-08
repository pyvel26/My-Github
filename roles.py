import psycopg2 
from psycopg2 import sql
import getpass
from getpass import getpass 


# I started my coding with creating a function prompt to receive the user name. This code will querry the Postgresql database and check
# to see if the username provided is already in the table. If this is true, we will see "User already exists" If not, the username is returned.

def prompt_username(con):
    cur = con.cursor()
    while True:
        username = input("Enter User Name : ")
        cur.execute("SELECT COUNT(*) FROM pg_catalog.pg_roles WHERE pg_roles.rolname = %s", [username])
        n, = cur.fetchone()
        if n == 0:
            return username
        print("User already exists.")


#Next I created a function to create the user and we start by opening a connection with psycopg2.
# I used getpass to scramble the password on the file. 
#The username retrieved from above

def userCreation():
    con = psycopg2.connect(
        user='postgres',
        host='localhost',
        port='5432',
        password = getpass('Enter password:'),
    )

    username = prompt_username(con)
    password = getpass(f"Enter Password for {username} : ")
    query = sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1}").format(
        sql.Identifier(username),
        sql.Literal(password),
    )
    cur = con.cursor()
    cur.execute(query.as_string(con))

    query = sql.SQL("GRANT pg_monitor").format(
        sql.Identifier(username)),
    #cur.execute('''GRANT pg_monitor TO "Dreadpoet";''')
    cur.execute("COMMIT")
    print("Permission granted successfully")

#--PERMISSIONS----------
#pg_execute_server_program
#pg_monitor
#pg_read_all_settings
#pg_read_all_stats
#pg_read_server_files
#pg_signal_backend
#pg_stat_scan_tables
#pg_write_server_files   


if __name__ == '__main__':
    userCreation()


