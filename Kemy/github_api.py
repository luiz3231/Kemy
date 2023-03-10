from urllib.request import Request


def buscar_avatar(usuario):
    """Busca o avatar de um usuario no GitHub
    
    :param usuario: str com o nome do usuario no githun
    :return: str com o link do avatar
    """
    url = f'https://api.githun.com/users/{usuario}'
    Request
    