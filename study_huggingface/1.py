"""
    NLP is a field of linguistics and machine learning focused on understanding
    everything related to human language. The aim of NLP tasks is not only to
    understand single words individually, but to be able to understand the context
    of those words.

    The following is a list of common NLP tasks, with some examples of each:
        1. Classifying whole sentences: Getting the sentiment of a review, detecting
        if an email is spam, determining if a sentence is grammatically correct or
        whether two sentences are logically related or not.

        2. Classifying each word in a sentence: Identifying the grammatical components
        of a sentences, or the named entities (person, location, organization)

        3. Generating text content: Completing a prompt with auto-generated text,
        filling in the blanks in a text with masked words

        4. Extracting an answer from a text: Given a question and a context, extracting
        the answer to the question based on the information provided in the context.

        5. Generating a new sentence from an input text: Translating a text into another
        language, summarizing a text
"""

from transformers import pipeline


classifier = pipeline("sentiment-analysis")
out = classifier("I've been waiting for a HuggingFace course my whole life", "I hate you!")

print(out)

"""
    There are three main steps involved when you pass some text to a pipeline:
    1. The text is preprocessed into a format the model can understand.
    2. The preprocessed inputs are passed to the model.
    3. The predictions of the model are post-processed, so you can make sense of them.
"""

"""
    Some of the currently available pipelines are:
    1. feature-extraction (get the vector representation of a text)
    2. ner (named entity recognition)
    3. question-answering
    4. sentiment-analysis
    5. summarization
    6. text-generation
    7. translation
    8. zero-shot-classification
"""

classifier = pipeline("zero-shot-classification")
out = classifier("This is a course about the Transformers library",
                 candidate_labels=["education", "business", "politics"])

generator = pipeline("text-generation", model="distilgpt2")
out = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2
)

unmasker = pipeline("fill-mask")
unmasker("This course will teach you all about <mask> models.", top_k=2)

question_answerer = pipeline("question-answering")
question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn"
)

"""
    1. GPT-like (also called auto-regressive Transformer models)
    2. BERT-like (also called auto-encoding Transformer models)
    3. BART / T5-like (also called sequence-to-sequence Transformer models)
"""

"""
    All the Transformer models mentioned above(GPT, BERT, BART, T5, etc) have
    been trained as language models, This means they have been trained on
    large amounts of raw texts in a self-supervised fashion. Self-supervised 
    learning is a type of training in which the objective is automatically 
    computed from the inputs of the model. That means that humans are not
    needed to label the data.
    
    This type of model develops a statistical understanding of the language
     it has been trqained on, but it's not very useful for specific practical
     tasks. Because of this, the general pretrained model then goes through
     a process called transfer learning. During this process, the model is 
     fine-tuned in a supervised way - that is, using human-annotated labels
     - on a given tasks
     
    An example of a task is predicting the next word in a sentence having
    read the n previous words. This is called causal language modeling
    because the output depends on the past and present inputs, but not the 
    future ones
    
    causal language modeling / masked language modeling
"""

"""
    Transfer Learning
    
    Pretraining is the act of training a model from scratch: the weights are randomly
    initialized, and the training starts without any prior knowledge.
    
    Fine-tuning, on the other hand, is the training done after a model has
    been pretrained. To perform fine-tuning, you first acquire a pretrained 
    language model, then perform additional training with a dataset specific
    to your task.
    
    1.The pretrained model was already trained on a dataset that has some similarities with the fine-tuning dataset.
    The fine-tuning process is thus able to take advantage of knowledge acquired by the initial model during pretraining
    (for instance, with NLP problems, the pretrained model will have some kind of statistical understanding of the 
    language you are using for your task)
    2.Since the pretrained model was already trained on lots of data, the fine-tuning requires way less data to get 
    decent results
    3.For the same reason, the amount of time and resources needed to get good results are much lower
"""

"""
    
"""














