import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database=""
)

cursor = db.cursor()


def show_tables():
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    for table in tables:
        print(table)


def get_sizes(unit, system, size):
    query_system = 'mens_sizes' if system == 'm' else 'womens_sizes'
    query = f'SELECT * FROM {query_system} WHERE {unit} = {size}'

    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    results = str(list(result)[0]).split(",")

    print(results)

    data = f'US: {str(results[0]).strip("()")}\nUK: {str(results[1])}\nEU: {str(results[2])}\nIN: {str(results[3])}\n' \
            f'CM: {str(results[4]).strip("()")}'


    print(data)
    return data
