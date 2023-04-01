import sqlite3
import datetime
import vk_api

from parsers import comments_parser
from auth import authorisation
from other_functions.search_by_id import about_group_f, about_user_f
from other_functions.to_db import to_database_group, to_database_user


def posts_parser(vk):
    con = sqlite3.connect('../new_file.db')
    words = ['онлайн магазин', 'online shop']  # слова, по которым ведётся поиск постов
    time_start_search = datetime.datetime.now()  # дата, время начала поиска
    start_time = int(datetime.datetime.timestamp(
        time_start_search - datetime.timedelta(days=2)))  # дата, с которой мы будем брать посты

    for word in words:

        try:
            posts = vk.newsfeed.search(q=word, extended=1, count=200, start_time=start_time)
            for post in posts.get('items'):
                owner_id = int(post.get('owner_id'))
                type = 'group' if owner_id < 0 else 'people'
                owner_id = owner_id * -1 if type == 'group' else owner_id
                print(post)
                if type == 'group':
                    group_id, name, screen_name, is_closed, type_group,\
                     city, country, description, contacts = about_group_f(vk, owner_id)

                    to_database_group(group_id, name, screen_name,
                                      is_closed, type_group, city,
                                      country, description, contacts)

                else:
                    vk_id, name, surname, phone_number, email, city, status = about_user_f(vk, owner_id)

                    to_database_user(vk_id, name, surname, phone_number, email, city, status)

                # comments_parser.comments_parser(vk, owner_id, type)

        except (vk_api.VkApiError, vk_api.ApiError) as error_msg:
            print(error_msg)
    con.commit()


if __name__ == '__main__':
    posts_parser(authorisation())
