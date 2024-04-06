from unstructured.partition.auto import partition

from paper2node.paper import Paper
from model.llm_model import LLMModel


# TODO
# # 获取表格内容
# with pdfplumber.open(path) as pdf:
#     first_page = pdf.pages[0]
#     tables = first_page.extract_tables()
#     for table in tables:
#         df = pd.DataFrame(table)
#         # 第1列当成表头
#         df = pd.DataFrame(table[1:], columns=table[0])


# 读取单个论文文件pdf
def read_paper(path: str) -> Paper:
    # 用unstructed库的partition类加载pdf文件
    elements = partition(path)
    elements = [str(element) for element in elements]

    # 获取论文类的所有属性值

    abstract_flag = False
    abstract_para_list = []
    content_flag = False
    content_para_dict = {}
    unselected_titles = []
    sub_title_template = ""
    sub_title = ""
    sub_para = ""
    counter = 1
    for i in range(len(elements)):
        # 读取候选标题
        if (not abstract_flag) and (not content_flag):
            unselected_titles.append(elements[i])

        # 结束读取摘要+开始读取原文
        if "INTRODUCTION" in elements[i].upper():
            abstract_flag = False
            content_flag = True

            sub_title_template = elements[i].upper().replace("INTRODUCTION", "")

        # 根据子标题分割文段
        if sub_title_template and sub_title_template in elements[i] and elements[i].replace(sub_title_template, "").replace(" ", "").isalpha():
            if sub_title:
                content_para_dict[sub_title] = sub_para
            sub_title_template = sub_title_template.replace(str(counter), str(counter+1))
            counter += 1
            sub_title = elements[i]
            sub_para = ""

        # 读取原文
        if content_flag:
            sub_para += elements[i]

        # 读取摘要
        if abstract_flag:
            abstract_para_list.append(elements[i][:-1]) if elements[i][-1] == "-" else abstract_para_list.append(elements[i])

        # 开始读取摘要
        if (not abstract_flag) and "ABSTRACT" in elements[i].upper():
            abstract_flag = True

    title = LLMModel.get_complete_paper_title(unselected_titles)
    # TODO 作者
    authors = []
    abstract = "".join(abstract_para_list)
    content = content_para_dict

    # TODO content
    content = "".join(content.values())

    # 将所有属性值存储到新的论文类里
    paper_obj = Paper()
    paper_obj.set_all_values(title, authors, path, abstract, content)

    return paper_obj


