# 论文类
class Paper:
    # 初始化
    def __init__(self):
        # 论文标题
        self.title = ""
        # 论文作者
        self.authors = []
        # 论文文件路径
        self.path = ""
        # 论文摘要
        self.abstract = ""
        # 论文原文
        self.content = ""

    # 获取所有属性
    def get_all_values(self):
        return self.title, self.authors, self.path, self.abstract, self.content

    # 设置所有属性
    def set_all_values(self, title: str, authors: list, path: str, abstract: str, content: str):
        self.title = title
        self.authors = authors
        self.path = path
        self.abstract = abstract
        self.content = content
