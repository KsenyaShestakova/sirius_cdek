import vk_api
from auth import authorisation
from other_functions.search_by_id import about_group_f
from other_functions.to_db import to_database_group


def groups_parser(vk):
    words = ['магазин', 'shop']
    for word in words:
        try:
            groups = vk.groups.search(q=word, count=100, market=1)
            for group in groups['items']:
                group_id, name, screen_name, is_closed, \
                type_group, city, country, description, \
                contacts = about_group_f(vk, group['id'])

                to_database_group(group_id, name, screen_name,
                                  is_closed, type_group, city,
                                  country, description, contacts)

        except (vk_api.VkApiError, vk_api.ApiError) as error_msg:
            print(error_msg)


if __name__ == '__main__':
    groups_parser(authorisation())
