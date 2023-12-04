import re

# test = "foo | bar | baz|xyz".split(r"\s+|\s+")


test = re.split('\s*\|\s*', "foo | bar | baz|xyz")

print(test)

