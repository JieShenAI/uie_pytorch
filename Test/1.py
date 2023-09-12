import os
from copy import deepcopy
from typing import Union, Sequence

# from dotenv import load_dotenv, find_dotenv
#
# _ = load_dotenv(find_dotenv())  # read local .env file
# print(_)
# print(os.environ["age"])
# print(os.environ["name"])




import re

text = "fa— ３４ —fa"
# 从text 匹配到 — ３４ —
pattern = re.findall(r'—.*?—', text)
t = re.sub(r'—.*?—', '', text)
print(t)
