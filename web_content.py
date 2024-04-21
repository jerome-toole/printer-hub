def get_web_content(url, lines=5):
    import requests
    import html2text

    # import random

    response = requests.get(url)
    content = response.text

    html2text = html2text.HTML2Text()

    print(html2text)

    response = html2text.handle(content)

    # lines = content.splitlines()
    # print(lines)

    # lines = str(lines)  # Convert lines to a string
    # random_lines = random.sample(lines, lines)

    return response.handle
