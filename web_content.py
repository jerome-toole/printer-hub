def get_web_content(url, lines=5):
    import requests
    import html2text

    from bs4 import BeautifulSoup

    # import random

    response = requests.get(url)
    content = response.content

    response = BeautifulSoup(content, 'html.parser')
    response = response.prettify()

    # lines = content.splitlines()
    # print(lines)

    # lines = str(lines)  # Convert lines to a string
    # random_lines = random.sample(lines, lines)

    return response
