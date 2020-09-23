import sqlite3

database = 'records_db.sqlite'

def main():
    create_table()
    menu_options = {
    '1': add_record,
    '2' : update_record,
    '3' : delete_record,
    '4' : search_records,
    '5' : view_all_records
       }

    while True:
        menu_ui()
        choice = input('Enter choice: ')
        if choice.lower() == 'q':
            break
        else:  
            menu_options.get(choice)()

def create_table():

    with sqlite3.connect(database) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (name text, country text, catches int)')
    conn.close()

def add_record():

    name = input('Enter name:')
    country = input('Enter country name: ')
    catches = input('Enter number of catches: ')

    try:
        with sqlite3.connect(database) as conn:
            conn.execute('INSERT INTO records VALUES (?,?,?)', (name,country,catches))
        conn.close()
    except Exception as e:
        print('Could not add ', e)


def update_record():

    name = input('Enter name of player you want to update the record for: ')
    catches = input('Enter new number of catches: ')
    
    with sqlite3.connect(database) as conn:
        conn.execute('UPDATE records SET catches = ? where name = ?', (catches,name))
    conn.close()

def delete_record():

    name = input('Enter name of record holder you want to delete: ')

    with sqlite3.connect(database) as conn:
        conn.execute('DELETE FROM records WHERE name = ?', (name,))
    conn.close()

def search_records():

    name = input('Enter name of record holder you want to search for: ')

    with sqlite3.connect(database) as conn:
        results = conn.execute('SELECT * FROM records WHERE name = ?', (name,))
        for r in results:
            print(r)
    conn.close()

def view_all_records():

    conn = sqlite3.connect(database)
    results = conn.execute('SELECT * FROM records')

    for r in results:
        print(r)
    conn.close()

def menu_ui():

    print('\n1:Add record')
    print('2:Update record')
    print('3:Delete record')
    print('4:Search records')
    print('5:View all records')
    print('Q:Quit\n')

main()