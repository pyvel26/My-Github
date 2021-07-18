import psycopg2 
from psycopg2 import sql
import getpass
from getpass import getpass 




def prompt_username(con):
    cur = con.cursor()
    while True:
        username = input("Enter User Name : ")
        cur.execute("SELECT COUNT(*) FROM pg_catalog.pg_roles WHERE pg_roles.rolname = %s", [username])
        n, = cur.fetchone()
        if n == 0:
            return username
        print("User already exists.")


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
    cur.execute("COMMIT")


    permission = input("Enter permission:")
    query1 = sql.SQL("GRANT {0} To {1} ").format(
        sql.Identifier(permission),
        sql.Identifier(username),)

    cur = con.cursor()
    cur.execute(query1.as_string(con))
    cur.execute("COMMIT")
    print("Permission granted successfully")



#--AVAILABLE_PERMISSIONS----------
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
