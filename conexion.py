from re import U
import psycopg2


def executeQuery(cursor, db, query, args, fetch=False):
    try:
        cursor.execute(query, args)

        if(fetch):
            return(cursor.fetchall())

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in transction. Reverting all other operations of a transction ", error)
        db.rollback()
        return False
