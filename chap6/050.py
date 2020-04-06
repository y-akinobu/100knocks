# 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

import re # 正規表現で置き換え
with open('nlp.txt', encoding='utf-8') as NLP:
  for line in NLP:
    print(re.sub(r"(?P<group1>[.;:?!])(\s+)(?P<group3>[A-Z])", r"\1\2\n\3", line))
