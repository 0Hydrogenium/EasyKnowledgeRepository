import copy

from mindmap2node.mindmap import Mindmap
import xmindparser

# xmindparser配置
xmindparser.config = {
    # 是否展示主题ID
    'showTopicId': True,
    # 是否隐藏空值
    'hideEmptyValue': True
}


def read_mindmap(path: str) -> Mindmap:
    # 将.xmind文件转换为dict
    content = xmindparser.xmind_to_dict(path)

    if isinstance(content, list) and len(content) > 0:
        content = content[0]

    if "画布" in content["title"] and "topic" in content.keys():
        content = content["topic"]

    # 定义脑图结构递归获取函数
    def recursive_load_every_str(cur_dict, key_list):
        new_key_list = copy.deepcopy(key_list)
        new_key_list.append(cur_dict["title"])

        if "topics" in cur_dict.keys() and isinstance(cur_dict["topics"], list):
            for sub_cur_dict in cur_dict["topics"]:
                recursive_load_every_str(sub_cur_dict, new_key_list)

        elif "topics" not in cur_dict.keys():
            new_content.append(new_key_list)

    new_content = []
    recursive_load_every_str(content, [])

    return new_content
