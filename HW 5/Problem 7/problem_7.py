### Problem 7

import psycopg2

def connect_to_postgres():
        connection = psycopg2.connect(host="0.0.0.0", 
                            port="5432", 
                            user="calebpena", 
                            password="test", 
                            database="calebpena"
                        )
        return(connection)


def insert_records():
    conn = connect_to_postgres()
    cur = conn.cursor()

    cur.execute("""INSERT INTO employees
                (SELECT generate_series(1,500) as id,
                        ('{Caleb, Bhoomika, Zach, Kevin, Dan, Alana, WeiYu, Woochan}'::text[])[ceil(random()*8)] AS fname,
                        ('{Pena, Moorjani, Ohl, Yang, Nason, Willis, Tseng, Lee}'::text[])[ceil(random()*8)] AS lname);""")

    conn.commit()
    cur.close()
    conn.close()

insert_records()


