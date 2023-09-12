with open('data/new.txt', 'r', encoding='utf-8') as f:
    # data = f.readlines()
    # data = [i.strip() for i in data]
    # print(data)
    data = f.read()
    print(data)
    print(len(data))