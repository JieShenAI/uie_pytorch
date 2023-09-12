from neo4j_lib.Neo4j import Neo4jLimit
from uie_predictor import UIEPredictor
from neo4j_lib.KgUtils import generate_limit_triple

text = []

# schema = {
# #     '区域': ['属于'],
# #     '领域': ['包括', '位于'],
# #     '任务': ['包括', '发生'],
# #     '时间': ['要求'],
# #     '定位': ['属于'],
# #     '事件': ['在'],
# #     '指标': ['属于'],
# # }

schema = {
    '区域': ['属于', '位于', '包括', '要求', '发生'],
    '领域': ['属于', '位于', '包括', '要求', '发生'],
    '时间': ['属于', '位于', '包括', '要求', '发生'],
    '事件': ['属于', '位于', '包括', '要求', '发生'],
    '定位': ['属于', '位于', '包括', '要求', '发生'],
    '任务': ['属于', '位于', '包括', '要求', '发生'],
}

# ie = UIEPredictor(model='uie-base', schema=schema, device='gpu')
limit_model_best = '.checkpoints/limit_model_best'
ie = UIEPredictor(model='uie-base', task_path=limit_model_best, schema=schema, device='gpu')
