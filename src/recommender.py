from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

from utils.logger import get_logger
logger = get_logger(__name__)

class AnimeRecommender:
  def __init__(self, retriever, api_key:str, model_name: str):
    self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

    prompt_templates = get_anime_prompt()

    self.prompt = ChatPromptTemplate.from_template(prompt_templates)

    self.chain = (
      {"context": retriever, "question": RunnablePassthrough()}
      | self.prompt
      | self.llm
      | StrOutputParser()
    )

  def get_recommendation(self, query:str):
    result = self.chain.invoke(query)
    return result

