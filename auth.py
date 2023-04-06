import vk_api
from constants import VK_TOKEN


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device


def authorisation():
    token = VK_TOKEN
    vk_session = vk_api.VkApi(token=token)  # Для остальных
    vk = vk_session.get_api()

    return vk
