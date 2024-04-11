import os

QUERIES = dict()

for root, _, files in os.walk("sql_templates"):
    for file in files:
        filename, ext = os.path.splitext(file)
        if ext == ".sql":
            with open(os.path.join(root, file), "r") as openfile:
                QUERIES[filename] = openfile.read()
