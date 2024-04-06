from keybert import KeyBERT
import logging


# KeyBERT 模型
KEYBERT_MODEL = KeyBERT("./model_storage/paraphrase-multilingual-MiniLM-L12-v2")

logger = logging.getLogger("APP")


# KeyBERT 模型类
class KeyBERTModel:
    # TODO 全局唯一一个类
    # 阈值
    threshold = 0.4
    model = KEYBERT_MODEL

    # 从文段中提取关键词
    @classmethod
    def extract_keywords(cls, input_text: str) -> list:
        keywords = cls.model.extract_keywords(input_text, keyphrase_ngram_range=(1, 3), use_mmr=True, diversity=0.4)

        selected_keywords = [x[0] for x in keywords if x[1] >= cls.threshold]
        logger.info("关键词获取成功: {}".format(selected_keywords))

        return selected_keywords
