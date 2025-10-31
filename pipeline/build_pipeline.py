from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

def main():
  try:
    logger.info("..START build pipeline")
    loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
    processed_csv = loader.load_and_process()
    logger.info("..SUCCESS data loaded and processed")

    vector_builder = VectorStoreBuilder(processed_csv)
    vector_builder.build_and_save_vectorstore()
    logger.info("..SUCCESS vector store")
    logger.info("..END build pipeline")
  except Exception as e:
    logger.error(f"xx>>> Failed to build pipeline {str(e)}")
    raise CustomException("Error during recommendation", e)

if __name__ == "__main__":
  main()