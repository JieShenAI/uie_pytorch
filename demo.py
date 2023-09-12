from uie_predictor import UIEPredictor
from pprint import pprint

# schema = ['时间', '选手', '赛事名称']  # Define the schema for entity extraction
schema = {
    "丈夫": "老婆",
}
# schema = ["儿子"]
ie = UIEPredictor(model='uie-base', schema=schema, device='gpu')
# ie = UIEPredictor(model='uie-base', schema=schema)
# pprint(
#     ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！")
# )  # Better print results using pprint

pprint(
    ie("张三的老婆是李四。王五的老婆是赵六。")
)

"""
[{'时间': [{'end': 6,
          'probability': 0.9857378532924486,
          'start': 0,
          'text': '2月8日上午'}],
  '赛事名称': [{'end': 23,
            'probability': 0.8503089953268272,
            'start': 6,
            'text': '北京冬奥会自由式滑雪女子大跳台决赛'}],
  '选手': [{'end': 31,
          'probability': 0.8981548639781138,
          'start': 28,
          'text': '谷爱凌'}]}]
"""
"""
python doccano.py \
    --doccano_file ./data/all.jsonl \
    --task_type ext \
    --save_dir ./data \
    --splits 0.8 0.2 0
"""

"""
python doccano.py --doccano_file ./data/all.jsonl --task_type ext --save_dir ./data --splits 0.8 0.2 0
"""