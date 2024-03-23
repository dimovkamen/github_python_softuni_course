import re

pattern = r"(www\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

line = input()

while line:
    url_link = re.search(pattern, line)

    if url_link:
        print(url_link.group(1))

    line = input()
