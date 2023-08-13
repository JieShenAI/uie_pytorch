# 信息抽取结果的处理
from typing import Dict, Union, Sequence, List

from uie_predictor import UIEPredictor

data = [{'丈夫': [{'end': 11,
                   'probability': 0.7874021,
                   'relations': {'老婆': [{'end': 17,
                                           'probability': 0.9967891,
                                           'start': 15,
                                           'text': '赵六'}]},
                   'start': 9,
                   'text': '王五'},
                  {'end': 2,
                   'probability': 0.8342766,
                   'relations': {'老婆': [{'end': 8,
                                           'probability': 0.9590847,
                                           'start': 6,
                                           'text': '李四'}]},
                   'start': 0,
                   'text': '张三'}]}]

ent_cnt = 0
relation = 0


# {"id":307,"label":"数据","start_offset":0,"end_offset":6}
class Entity:
    id = 0

    def __init__(self, label, start_offset, end_offset):
        self.id = Entity.id
        self.label = label
        self.start_offset = start_offset
        self.end_offset = end_offset

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(cls)

    def __eq__(self, other: Union["Entity", Sequence]):
        if isinstance(other, Entity):
            return self.label == other.label and self.start_offset == other.start_offset and self.end_offset == other.end_offset
        else:
            if len(other) == 3:
                return self.label == other[0] and self.start_offset == other[1] and self.end_offset == other[2]
        return False

    def __hash__(self):
        return hash((self.label, self.start_offset, self.end_offset))

    def __repr__(self):
        return f"Entity({self.id} {self.label} {self.start_offset} {self.end_offset})"


# {"id":130,"from_id":332,"to_id":333,"type":"link"}
class Relation:
    # id = 0

    def __init__(self, from_id, to_id, type):
        # self.id = Relation.id
        self.from_id = from_id
        self.to_id = to_id
        self.type = type

    # def __new__(cls, *args, **kwargs):
    #     cls.id += 1
    #     return super().__new__(cls)

    def __eq__(self, other: Union["Relation", Sequence]):
        if isinstance(other, Relation):
            return self.from_id == other.from_id and self.to_id == other.to_id and self.type == other.type
        else:
            if len(other) == 3:
                return self.from_id == other[0] and self.to_id == other[1] and self.type == other[2]
        return False

    def __hash__(self):
        return hash((self.from_id, self.to_id, self.type))

    def __repr__(self):
        return f"Relation({self.from_id} {self.to_id} {self.type})"


def _res2doccano(result: List[Dict]):
    ents = set()
    rels = set()
    for data in result:
        for key, value in data.items():
            ent_class = key
            for item in value:
                e = (ent_class, item['start'], item['end'])
                for ent in ents:
                    if ent == e:
                        ent1 = ent
                        break
                else:
                    ent1 = Entity(ent_class, item['start'], item['end'])
                    ents.add(ent1)
                if not item.get('relations', []):
                    continue
                for rel_name, items in item['relations'].items():
                    if rel_name == '定语':
                        obj_name = "修饰词"
                    elif rel_name == '宾语':
                        obj_name = "Object"
                    elif rel_name == '谓语':
                        obj_name = "Relation"
                    else:
                        obj_name = "Other"

                    for d in items:
                        v = (obj_name, d["start"], d["end"])
                        for ent in ents:
                            if ent == v:
                                ent2 = ent
                                break
                        else:
                            ent2 = Entity(obj_name, d['start'], d['end'])
                            ents.add(ent2)

                        # 创建关系
                        r = (ent1.id, ent2.id, rel_name)
                        for rel in rels:
                            if r == rel:
                                break
                        else:
                            rel = Relation(ent1.id, ent2.id, rel_name)
                            rels.add(rel)

    return ents, rels


class Doccano:
    # id = 0

    def __init__(self, text, entities, relations, Comments=[]):
        # self.id = Doccano.id
        self.text = text
        self.entities = entities
        self.relations = relations
        self.Comments = Comments

    # def __new__(cls, *args, **kwargs):
    #     cls.id += 1
    #     return super().__new__(cls)

    def __repr__(self):
        return f"Doccano({self.text} {self.entities} {self.relations} {self.Comments})"


def generate_label_from_text(text: str, ie, output_file: str = "./auto_labels.jsonl"):
    # 模型预测结果
    result = ie(text)
    ents, rels = _res2doccano(result)
    data = Doccano(
        text,
        [ent.__dict__ for ent in ents],
        [rel.__dict__ for rel in rels]
    ).__dict__
    import json

    with open(output_file, "a+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        f.write("\n")


if __name__ == '__main__':
    schema = {
        "Subject": "定语",
        "Object": "定语",
        "Subject": "谓语",
        "Relation": "宾语",
    }

    ie = UIEPredictor(model='uie-base', schema=schema, device='gpu')
    text = "推动部门间物流安检互认、数据互通共享，减少不必要的重复安检"
    generate_label_from_text(text, ie)
