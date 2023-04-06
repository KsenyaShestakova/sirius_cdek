import vk_api
from other_functions.search_by_id import about_group_f, about_user_f
from other_functions.to_db import to_database_group, to_database_user


def comments_parser(vk, owner_id, post_id, type):
    """Ищет в комментариях постов с ключевыми словами ['онлайн магазин', 'online shop']"""
    key_words = ['online shop', 'online store', 'онлайн магазин', 'изготавливаю', 'произвожу',
                 'создаю', 'на заказ']
    owner_id = -1 * owner_id if type == 'group' else owner_id
    post_id = post_id
    try:
        comments = vk.wall.getComments(owner_id=owner_id, post_id=post_id)
        if comments['count'] != 0:
            for comm in comments['items']:
                for word in key_words:
                    if word in comm['text']:
                        if int(comm['from_id']) < 0:
                            group_id, name, screen_name, is_closed, type_group, \
                            city, country, description, contacts = about_group_f(vk, int(comm['from_id']))

                            to_database_group(group_id, name, screen_name,
                                              is_closed, type_group, city,
                                              country, description, contacts)
                        else:
                            vk_id, name, surname, phone_number, email, city, status = about_user_f(vk, int(comm['from_id']))

                            to_database_user(vk_id, name, surname, phone_number, email, city, status)

                    if comm['thread']['count'] != 0:
                        for ans in comm['thread']['items']:
                            if word in ans['text']:
                                if int(ans['from_id']) < 0:
                                    group_id, name, screen_name, is_closed, type_group, \
                                    city, country, description, contacts = about_group_f(vk, int(comm['from_id']))

                                    to_database_group(group_id, name, screen_name,
                                                      is_closed, type_group, city,
                                                      country, description, contacts)
                                else:
                                    vk_id, name, surname, phone_number, email, city, status = about_user_f(vk, int(
                                        ans['from_id']))

                                    to_database_user(vk_id, name, surname, phone_number, email, city, status)

    except (vk_api.VkApiError, vk_api.ApiError) as error_msg:
        print(error_msg)
