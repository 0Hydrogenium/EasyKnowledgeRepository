from model.llm_model import LLMModel
from model.keybert_model import KeyBERTModel


# 解析单个论文
def parse_paper(abstract):
    keybert_model_obj = KeyBERTModel()

    keywords = keybert_model_obj.extract_keywords(abstract)

    return keywords














