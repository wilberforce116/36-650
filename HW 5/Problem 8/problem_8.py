### Problem 8

import psycopg2

def connect_to_postgres():
        connection = psycopg2.connect(host="0.0.0.0", 
                            port="5432", 
                            user="calebpena", 
                            password="test", 
                            database="calebpena"
                        )
        return(connection)


def print_random_records():
    conn = connect_to_postgres()
    cur = conn.cursor()

    cur.execute("""SELECT * FROM employees
                    ORDER BY random()
                    LIMIT 10;""")

    for row in cur:
        print(row)
    
    cur.close()
    conn.close()

print_random_records()


