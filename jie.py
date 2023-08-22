from typing import Union, Sequence, List, Dict, Set

data1 = [{'任务': [{'end': 60,
                    'probability': 0.75834656,
                    'start': 50,
                    'text': '优化提升首都核心功能'},
                   {'end': 277, 'probability': 0.3672101, 'start': 272, 'text': '水生态廊道'},
                   {'end': 108,
                    'probability': 0.6656096,
                    'start': 100,
                    'text': '城乡区域协调发展'},
                   {'end': 84, 'probability': 0.7402001, 'start': 76, 'text': '优化提升发展质量'},
                   {'end': 97, 'probability': 0.725045, 'start': 89, 'text': '城市内部功能重组'},
                   {'end': 72,
                    'probability': 0.45865548,
                    'start': 61,
                    'text': '以功能分区引导发展方向'},
                   {'end': 131, 'probability': 0.40047732, 'start': 129, 'text': '宜居'},
                   {'end': 285,
                    'probability': 0.3312067,
                    'relations': {'包含': [{'end': 365,
                                            'probability': 0.35071263,
                                            'start': 358,
                                            'text': '北运河湿地公园'},
                                           {'end': 350,
                                            'probability': 0.26023296,
                                            'start': 343,
                                            'text': '延芳淀湿地公园'}]},
                    'start': 278,
                    'text': '大尺度生态空间'},
                   {'end': 472, 'probability': 0.7814595, 'start': 468, 'text': '功能疏解'},
                   {'end': 128, 'probability': 0.39901432, 'start': 126, 'text': '绿色'},
                   {'end': 134, 'probability': 0.31925365, 'start': 132, 'text': '人文'},
                   {'end': 428,
                    'probability': 0.3654683,
                    'relations': {'属于': [{'end': 389,
                                            'probability': 0.5787516,
                                            'start': 369,
                                            'text': '配置教育、医疗、文化、体育等公共服务设施'}]},
                    'start': 420,
                    'text': '建设三甲综合医院'},
                   {'end': 467,
                    'probability': 0.79193133,
                    'start': 461,
                    'text': '城市更新改造'},
                   {'end': 478, 'probability': 0.79712385, 'start': 473, 'text': '城中村整治'},
                   {'end': 139, 'probability': 0.33442593, 'start': 135, 'text': '智慧发展'},
                   {'end': 457,
                    'probability': 0.2714158,
                    'relations': {'包含': [{'end': 443,
                                            'probability': 0.3671106,
                                            'start': 431,
                                            'text': '通州市民文化休闲活动中心'}]},
                    'start': 446,
                    'text': '综合性公共文化设施建设'},
                   {'end': 197, 'probability': 0.4344345, 'start': 193, 'text': '商务服务'}],
          '时间': [{'end': 206,
                    'probability': 0.9433726,
                    'start': 201,
                    'text': '2017年'}]}]


class OpenTriple:
    def __init__(self, subject="", object="", relation=""):
        self.subject = subject
        self.object = object
        self.relation = relation

    def __repr__(self):
        return f"Triple({self.subject} {self.relation} {self.object})"

    def __eq__(self, other):
        return self.subject == other.subject and self.object == other.object and \
            self.relation == other.relation

    def __hash__(self):
        return hash((self.subject, self.object, self.relation))

    def connect(self, other) -> Union["OpenTriple", None]:
        if self.object == other.object and self.relation == "" and other.subject == "":
            return OpenTriple(self.subject, self.object, other.relation)
        return None


def generate_open_triple(data: Union[Sequence, Dict]) -> Set[OpenTriple]:
    if isinstance(data, Sequence):
        data = data[0]
    triple_sub_obj = set()
    for subject in data.get("主语", []):
        sub_text = subject["text"]
        objects = subject["relations"].get("宾语", [])

        for obj in objects:
            triple_sub_obj.add(OpenTriple(sub_text, obj.get("text", "")))

    triple_obj_rel = set()
    for object in data.get("宾语", []):
        obj_text = object["text"]
        rels = object["relations"].get("关系", [])
        for rel in rels:
            triple_obj_rel.add(OpenTriple("", obj_text, rel.get("text", "")))

    ans: Set[OpenTriple] = set()
    while triple_obj_rel:
        item = triple_obj_rel.pop()
        for triple in triple_sub_obj:
            new_triple = triple.connect(item)
            if new_triple:
                ans.add(new_triple)
                break
        else:
            # 只有宾语-关系 没有主语
            ans.add(item)

    return ans


class EntityLimit:
    """
    限定域实体
    """

    def __init__(self, text="", type=""):
        self.text = text
        self.type = type

    def __repr__(self):
        return f"Entity({self.text}, {self.type})"

    def __eq__(self, other):
        return self.text == other.text and self.type == other.type

    def __hash__(self):
        return hash((self.text, self.type))


class TripleLimit:
    """
    限定域三元组
    """

    def __init__(self, subject: EntityLimit, object: EntityLimit, relation=""):
        self.subject = subject
        self.object = object
        self.relation = relation

    def __repr__(self):
        return f"Triple({self.subject} - {self.relation} - {self.object})"

    def __eq__(self, other):
        return self.subject == other.subject and self.object == other.object and \
            self.relation == other.relation

    def __hash__(self):
        return hash((self.subject, self.object, self.relation))


def generate_triple(data: Union[Sequence, Dict]) -> Set[OpenTriple]:
    if isinstance(data, Sequence):
        data = data[0]

    for subject_type, values in data.items():
        for value in values:
            text = value["text"]
            relations = value.get("relations", [])
            ent1 = EntityLimit(text, subject_type)
            if not relations:
                continue
            for rel_type, rel_values in relations.items():
                # rel_values: List[Dict]
                for obj in rel_values:
                    obj_text = obj["text"]
                    ent2 = EntityLimit(obj_text, "Object")
                    yield TripleLimit(ent1, ent2, rel_type)


if __name__ == '__main__':
    # print(data1)
    data = generate_triple(data1)
    for item in data:
        print(item)
        # print(type(item.subject), type(item.relation), type(item.object))
        # print(isinstance(item.subject, EntityLimit))
        # print(item)
