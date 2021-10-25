### Problem 6

import psycopg2

def connect_to_postgres():
        connection = psycopg2.connect(host="0.0.0.0", 
                            port="5432", 
                            user="calebpena", 
                            password="test", 
                            database="calebpena"
                        )
        return(connection)


def create_table_psql():
    conn = connect_to_postgres()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE employees (
        id serial,
        fname varchar(10),
        lname varchar (10)
        );""")

    conn.commit()
    cur.close()
    conn.close()

create_table_psql()




cur.execute("DROP TABLE employees;")


cur.execute("select * from employees")




cur.execute("select * from employees;")

print("Unformatted Results:")
print (cur.description)

print("\n\n Formatted Results:")
for row in cur:
    print (row)
    
cur.close()
conn.close()

