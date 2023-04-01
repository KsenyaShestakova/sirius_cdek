def about_group_f(vk, group_id):
    """Ищет всё, что нужно записать в БД"""
    about_group = vk.groups.getById(
        group_id=group_id,
        fields=['city', 'contacts', 'counters',
                'country', 'description'])

    group_id, name, screen_name, is_closed, type_group = about_group[0].get('id'), about_group[0].get('name'), \
                                                         about_group[0].get('screen_name'), about_group[0].get(
        'is_closed'), about_group[0].get('type')

    contacts = [[user.get('user_id'), user.get('desc'), user.get('phone'), user.get('email')] for user in
                about_group[0].get('contacts')] if about_group[0].get('contacts') else None

    description = about_group[0].get('description')
    city = about_group[0].get('city').get('title') if about_group[0].get('city') else None
    country = about_group[0].get('country').get('title') if about_group[0].get('country') else None

    return group_id, name, screen_name, is_closed, type_group, city, country, description, contacts


def about_user_f(vk, user_id):
    about_user = vk.users.get(user_ids=user_id, fields=['about', 'city', 'contacts'])
    print(about_user)
    vk_id = about_user[0].get('id')
    name = about_user[0].get('first_name')
    surname = about_user[0].get('last_name')
    phone_number = about_user[0].get('mobile_phone')
    email = None
    city = about_user[0].get('city').get('title') if about_user[0].get('city') else None
    status = about_user[0].get('about')
    return vk_id, name, surname, phone_number, email, city, status
