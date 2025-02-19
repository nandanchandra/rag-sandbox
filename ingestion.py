import os

from dotenv import load_dotenv
from langchain_community.document_loaders.text import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

if __name__ == "__main__":

    REDIS_URL = os.environ.get("REDIS_URL")
    OPEN_AI_MODEL = os.environ.get("OPEN_AI_MODEL")
    VECTOR_STORE_INDEX = os.environ.get("VECTOR_STORE_INDEX")
    VECTOR_STORE_INDEX_PREFIX = os.environ.get("VECTOR_STORE_INDEX_PREFIX")
    VECTOR_SIMILARITY_METRIC = os.environ.get("VECTOR_SIMILARITY_METRIC")

    embeddings = OllamaEmbeddings(model=OPEN_AI_MODEL)

    redis_config = RedisConfig(
        index_name=VECTOR_STORE_INDEX,
        key_prefix=VECTOR_STORE_INDEX_PREFIX,
        redis_url=REDIS_URL,
        distance_metric=VECTOR_SIMILARITY_METRIC,
    )

    vector_store = RedisVectorStore(embeddings, config=redis_config)

    currnt_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(currnt_dir, "example.txt")

    file_loader = TextLoader(file_path)
    document_to_split = file_loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document_to_split)

    vector_store.add_documents(texts)
