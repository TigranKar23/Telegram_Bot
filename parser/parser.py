import requests
from bs4 import BeautifulSoup
def parser():
    def get_html(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred: {err}')  # Вывод ошибки HTTP
        except Exception as err:
            print(f'An error occurred: {err}')  # Вывод любой другой ошибки
        # Создаем экземпляр BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')


    def parse_khl_page(html):
        soup = BeautifulSoup(html, 'html.parser')

        # Поиск всех блоков с информацией об игроках
        players_data = soup.find_all('div', class_='leaders-item')

        results = []

        for player in players_data:
            player_info = {}
            
            # Имя игрока
            name = player.find('p', class_='leaders-person__name-text')
            if name:
                player_info['name'] = name.text.strip()

            # Статистика
            stats = player.find_all('div', class_='stat-hover__item')
            for stat in stats:
                key = stat.find('p', class_='stat-hover__item-text').text.strip()
                value = stat.find('p', class_='stat-hover__item-num').text.strip()
                player_info[key] = value

            results.append(player_info)

        return results

    url = 'https://www.khl.ru/'
    html_content = get_html(url)
    return parse_khl_page(html_content)
