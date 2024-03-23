import re

text = """href="/trainings/resources/92740/python-january-2024/4379" target="_blank"><i class="fa fa fa-file-word-o lecture-details-resources-list-item-icon"></i>Regular Expressions - Exercise</a>
<a href="/trainings/resources/92740/python" target="_blank"><i class="fa fa fa-file-word-o lecture-details-resources-list-item-icon"></i>Regular Expressions - Exercise</a>
<a href="/trainings/resources/92740/python-" target="_blank"><i class="fa fa fa-file-word-o lecture-details-resources-list-item-icon"></i>Regular Expressions - Exercise</a>"""

pattern = r'(href=)"([^"]+)"'
#pattern = r'aloalo'

results = re.finditer(pattern, text)
for result in results:
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    print()


results_1 = re.findall(pattern, text)
print(results_1)
for result_1 in results_1:
    print(result_1)
    print(result_1[0])
    print(result_1[1])

print()
if re.search(pattern, text):
    print("Found in text")
else:
    print("NOT found in text")

print()
is_matching = re.match(pattern, text)
if is_matching:
    print("Found in text")
    print(is_matching.groups())
else:
    print("NOT found in text")
