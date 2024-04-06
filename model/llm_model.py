from openai import OpenAI
import tiktoken
import requests
import json
import logging


# GPT API key
FREE_GPT_API_KEY = "sk-62ISlL7ZIg7encG74OyX54jn5LfYVd64fQmYQ2Udo9fmgHzR"
VIP_GPT_API_KEY = "sk-9KoneJj0s8QfycNL5TO11VcBTIimHKSLrBdzEJdXeKY5xe3O"
# GPT 模型
GPT_MODEL = OpenAI(api_key=FREE_GPT_API_KEY, base_url="https://api.chatanywhere.tech")

logger = logging.getLogger("APP")


# LLM模型名称常量类
class LLMModelName:
    gpt = "gpt"
    gemini = "gemini"


# LLM模型类
class LLMModel:

    # API使用次数
    gpt_api_uses = 0
    # API使用次数最大值
    GPT_API_USES_MAXIMUM = 100

    #  GPT大模型生成文本
    @classmethod
    def gpt_generate(cls, input_text):
        """
            输入token数限制: 4096
        """
        if cls.gpt_api_uses < cls.GPT_API_USES_MAXIMUM:
            cls.gpt_api_uses += 1
        else:
            print("gpt LLM model uses exceeds the maximum setting!")
            return ""

        messages = [{
            "role": "user",
            "content": input_text
        }]

        # 计算输入文本的token数
        token_calculator = tiktoken.encoding_for_model('gpt-3.5-turbo')
        token_num = len(token_calculator.encode(input_text))

        completion = GPT_MODEL.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        output_text = completion.choices[0].message.content

        return output_text

    # 根据根主题词生成主题词树
    @classmethod
    def generate_theme_tree(cls, root_theme) -> list:
        example = "| Level 1 | Level 2 | Level 3 |\n|-|-|-|\n| Deep Learning | Supervised learning | Convolutional Neural Networks |\n|  |  | Recurrent Neural Networks |\n|  |  | Transformer Networks |\n|  |  | Graph Neural Networks |\n|  | Unsupervised learning | Generative Adversarial Networks |\n|  |  | Variational Autoencoders |\n|  |  | Diffusion Models |\n|  | Reinforcement learning | Q-learning |\n|  |  | Policy Gradients |\n|  |  | Actor-Critic Methods |"
        input_text = "Please generate a three-level topic word tree for this field based on the topic word '{}', and the results will be shown in a table, modeled after the following table: [{}], with one topic word per cell, and generate as much the topic word as possible.".format(root_theme, example)

        output_text = cls.gpt_generate(input_text)

        table_line_list = [x for i, x in enumerate(output_text.split("\n")) if i >= 2]

        theme_list = []
        for line in table_line_list:
            # 去除"'s"
            line = line.replace("'s", "").replace("*", "")

            theme_list.append([x.strip(" ") for x in line.split("|") if x != " " and x != ""])

        fixed_theme_list = []
        cell1 = ""
        cell2 = ""
        for line in theme_list:
            if line[0]:
                cell1 = line[0]
            if line[1]:
                cell2 = line[1]
            cell3 = line[2]

            fixed_theme_list.append([cell1, cell2, cell3])

        return fixed_theme_list

    # 从列表中获取完整的论文标题
    @classmethod
    def get_complete_paper_title(cls, unselected_titles):
        # 去除全为数字的子项
        unselected_titles = [x for x in unselected_titles if not x.isdigit()]

        for i in range(1, len(unselected_titles)):
            concat_str = "{} {}".format(unselected_titles[i-1].strip(" "), unselected_titles[i].strip(" "))
            input_text = "[{}] Determine syntactically if the above string is a complete paper title. Please answer yes or no.".format(concat_str)

            output_text = cls.gpt_generate(input_text)

            if "yes" in output_text.lower():
                logger.info("读取标题成功: {}".format(concat_str))
                return concat_str

        logger.info("读取标题失败".format(unselected_titles))
        return ""


