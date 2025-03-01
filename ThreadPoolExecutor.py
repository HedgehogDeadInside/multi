import concurrent.futures,  urllib, urllib.request


def get_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


links = open('links.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(get_url, url, 60): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as e:
            print(url, e)