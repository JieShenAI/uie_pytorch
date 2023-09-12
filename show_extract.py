"""
将一整篇文章的信息抽取出来，展示给数据标注人员看
    * 前面是模型输入的文本
    * 后面是模型抽取出来的三元组
"""
from UIE_settings import ie
from neo4j_lib.KgUtils import generate_limit_triple
import torch

def cut_line(line):
    """
    (在数据处理阶段，保证每一行都是完整的句子)
    在信息抽取时，一行一行进行信息抽取，若一行的字符数超过500字
        每400字进行一次抽取，但是下标只移动300字，保证尽量不会漏掉信息
    """
    for i in range(0, len(line), 50):
        yield line[i: i + 100]


data_file = "./make_dataset/wps/data/1_clean.txt"

with open(data_file, 'r', encoding='utf-8') as f:
    data = f.readlines()
    # 禁止多线程
    for line in data:
        if len(line) < 100:
            result = ie(line)
            print(result)
            # out = generate_limit_triple(result)
            # # 释放out在GPU上的显存空间
            # for item in out:
            #     print(item)
            # 释放显存空间
            torch.cuda.empty_cache()

        else:
            for text in cut_line(line):
                result = ie(line)
                print(result)
                # out = generate_limit_triple(result)
                # for item in out:
                #     print(item)
                torch.cuda.empty_cache()
