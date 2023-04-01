import sqlite3


def to_database_group(group_id, name,
                      screen_name, is_closed, type_group, city, country,
                      description, contacts):
    con = sqlite3.connect('../new_file.db')

    try:
        con.cursor().execute('''INSERT INTO groups(group_id, name,
         screen_name, is_closed, type_group, city, country,
         description, contacts)
         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (group_id, name,
                                                screen_name, is_closed, str(type_group), str(city), str(country),
                                                str(description), str(contacts)))
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as error:
        print(error)

    con.commit()


def to_database_user(vk_id, name, surname, phone_number, email, city, status):
    con = sqlite3.connect('../new_file.db')

    try:
        con.cursor().execute('''INSERT INTO users(vk_id, name, surname, phone_number, email, city, status)
             VALUES(?, ?, ?, ?, ?, ?, ?)''', (vk_id, name, surname, str(phone_number), email, city, status))
    except (sqlite3.OperationalError, sqlite3.IntegrityError) as error:
        print(error)

    con.commit()
