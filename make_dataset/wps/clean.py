def clean_(file, out_file):
    """
    从文本中去除换行符，若一行末尾为 '。\n' 则保留，否则去除换行符
    """
    with open(file, encoding='utf8') as f:
        data = f.readlines()
        print(data)
        ans = ''
        for line in data:
            text = line
            if len(line) > 2 and line[-2:] == '。\n':
                pass
            else:
                text = line.rstrip()
            ans += text

        with open(out_file, 'w', encoding='utf8') as f:
            f.write(ans)


if __name__ == '__main__':
    # in_file = "data/1.txt"
    # out_file = "data/1_clean.txt"
    # clean_(in_file, out_file)

    text = """
    　　一、加强规划实施的法治保障　　加强法治顶层设计，出台一批地方性法规规章，做好立、改、废、释工作，完善规划实施的法律基础，用法律手段保障规划的实施，提升规划目标任务的约束力和权威性，推进规划实施的法治化。
    　　二、加强实施计划　　将行动计划、年度计划作为实施本规划纲要的重要支撑。按照本规划纲要确定的重点任务研究制定相关专项行动计划，以一批重大举措保障规划实施。按照本规划纲要的总体安排部署，编制国民经济和社会发展年度计划，分年度落实规划提出的目标和任务，对约束性指标和重大项目设置年度目标，年度计划报告要分析本规划纲要的实施进展情况，报告约束性指标的完成情况。
    　　三、加强项目落地　　坚持以规划确定项目、以项目落实规划，发挥好重大项目对规划落实的支撑作用。健全重点项目储备库制度，有计划实施一批关系全局和长远发展的重大项目。建立健全重大项目推进机制，强化项目实施管理。
    　　四、加强政策和资源要素供给　　围绕规划目标任务，完善人口、土地、环保、财政、价格等相关配套政策，加强各项政策协调配合，根据宏观环境变化和发展实际，加强政策储备，为规划实施提供有力的政策支撑。统筹优化财政支出结构和政府投资结构，优先安排涉及生态环保、民生保障、城市管理等领域的投入，提高政府投资的引导力和带动力，鼓励社会投资投向规划重点领域，为规划实施提供资金保障。健全战略资源的激励和约束机制，统筹推进人才队伍建设管理，科学调控土地供应，加强对能源、水资源利用的科学管理，加强环境容量控制，有效引导社会资源合理配置。
    第三章　落实规划监督考评　　完善规划实施监督评估制度，强化规划分解落实与考核评价，扩大公众参与，落实规划目标任务。
    　　一、加强考核评价　　分解本规划纲要确定的发展目标和主要任务，明确牵头单位和工作责任，加大绩效考核力度。约束性指标是政府必须履行的重要责任，要分解落实到各区和有关部门，并纳入综合评价和绩效考核体系。强化对非首都功能疏解、人口调控、生态建设、环境保护、资源节约、城市管理、结构优化和民生改善等目标任务完成情况的综合评价考核。
    　　二、完善监督评估　　加强第三方独立评估，听取社会各界、广大群众对规划实施的意见和建议。自觉接受市人大及其常委会对规划实施情况的监督检查。
        """


    # 若该行文本太长，一次截取500个字符
    def cut_line(line):
        for i in range(0, len(line), 300):
            yield line[i: i + 400]


    data = cut_line(text)
    for text in data:
        print(text)
        print('*' * 100)
