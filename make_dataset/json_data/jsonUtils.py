def make_big_json(file, cnt):
    with open(file, 'a', encoding='utf8') as f:
        text = f.read()
        for i in range(cnt):
            f.write(text)

