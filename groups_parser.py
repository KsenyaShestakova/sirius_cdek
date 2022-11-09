import sqlite3
from password_login import LOGIN, PASSWORD
import vk_api


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    return vk


def groups_parser(vk):
    con = sqlite3.connect('new_file.db')
    alph = ''.join([chr(el) for el in range(1072, 1104)])
    words = ['магазин', 'shop']
    for word in words:
        try:
            groups = vk.groups.search(q=word, count=30, market=1)
            for group in groups['items']:
                about_group = vk.groups.getById(group_id=group['id'],
                                                fields=['city', 'contacts', 'counters', 'country', 'description'])

                group_id, name, screen_name, is_closed, type_group = group['id'], group['name'], group['screen_name'], \
                                                                     group['is_closed'], group['type']
                contacts = [[user.get('user_id'), user.get('desc'), user.get('phone'), user.get('email')] for user in
                            about_group[0].get('contacts')] if about_group[0].get('contacts') else None
                description = about_group[0].get('description') if about_group[0].get('description') else None
                city = about_group[0].get('city').get('title') if about_group[0].get('city') else None
                country = about_group[0].get('country').get('title') if about_group[0].get('country') else None

            try:
                con.cursor().execute(f'''INSERT INTO groups(group_id, name,
                     screen_name, is_closed, type_group, city, country,
                      description, contacts) VALUES({group_id}, "{name}",
                       "{screen_name}", {is_closed}, "{type_group}",
                        "{city}", "{country}", "{description}", "{contacts}")''')
            except (sqlite3.OperationalError, sqlite3.IntegrityError) as error:
                print(error)
        except (vk_api.VkApiError, vk_api.ApiError) as error_msg:
            print(error_msg)
    con.commit()


if __name__ == '__main__':
    groups_parser(main())
