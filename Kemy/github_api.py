from urllib import request
def buscar_avatar(usuario):
    """Busca o avatar de um usuario no GitHub
    
    :param usuario: str com o nome do usuario no githun
    :return: str com o link do avatar
    """
    url = f'https://api.githun.com/users/{usuario}'
    resp = request.get(url)
    return resp.json()['avatar_url']
if __name__ == '__main__':
    print(buscar_avatar('luiz3231'))
    