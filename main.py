from neo4j_lib.Neo4j import Neo4jLimit
from uie_predictor import UIEPredictor
from neo4j_lib.KgUtils import generate_limit_triple

text = []
schema = {
    '区域': ['属于'],
    '领域': ['包括', '位于'],
    '任务': ['包括', '发生'],
    '时间': ['要求'],
    '定位': ['属于'],
    '事件': ['在'],
    '指标': ['属于'],
}

# ie = UIEPredictor(model='uie-base', schema=schema, device='gpu')
limit_model_best = '.checkpoints/limit_model_best'
# ie = UIEPredictor(model='uie-base', task_path=limit_model_best, schema=schema, device='gpu')
# ie = UIEPredictor(model='uie-base', task_path=limit_model_best, schema=schema)
file = "data/new1.txt"
with open(file, 'r', encoding='utf-8') as f:
    data = f.read()

for i in range(0, len(data), 50):
    ie = UIEPredictor(model='uie-base', task_path=limit_model_best, schema=schema, device='gpu')
    text = data[i:i + 200]
    print("text_len:", len(text))
    result = ie(
        text
    )
    del ie
    # print(result)
    # out = generate_limit_triple(result)

    # neo = Neo4jLimit()
    # for item in out:
    #     neo.create_triple(item)
