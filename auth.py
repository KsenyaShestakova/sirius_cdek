import vk_api
from constants import VK_LOGIN, VK_PASSWORD


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device


def authorisation():
    login, password = VK_LOGIN, VK_PASSWORD
    vk_session = vk_api.VkApi(login, password,
                              auth_handler=auth_handler)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    return vk
