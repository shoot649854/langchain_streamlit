import logging
import os
from typing import Any, List, Tuple, Union

import dotenv
import vertexai
from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_google_community import VertexAISearchRetriever
from langchain_google_vertexai import ChatVertexAI
from src.control.Markdown import read_markdown

# from functools import lru_cache
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")
LOCATION_ID = os.getenv("LOCATION_ID")
DATA_STORE_ID = os.getenv("DATA_STORE_ID")

# Set up basic logging configuration
dotenv.load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

# https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference
MODEL_NAME = "gemini-1.5-flash-001"


class VertexAIChat:
    def __init__(self) -> None:
        self.chat_model = ChatVertexAI()
        self.initial_template = read_markdown(os.path.join(os.getcwd(), "src/model/prompt_initial.md"))
        self.initial_prompt = PromptTemplate(
            template=self.initial_template,
            input_variables=["chat_history", "action_input"],
        )
        self.template = read_markdown(os.path.join(os.getcwd(), "src/model/prompt_general.md"))
        self.prompt = PromptTemplate(template=self.template, input_variables=["chat_history", "action_input"])
        self.memory = ConversationBufferMemory(memory_key="chat_history")

    def search_immigration_database(self, query: str) -> Union[str, Tuple[str, List[Any]]]:
        """Search for visa information using VertexAI Search Retriever."""
        filter_condition = None

        retriever = VertexAISearchRetriever(
            project_id=PROJECT_ID,
            data_store_id=DATA_STORE_ID,
            location_id=LOCATION_ID,
            engine_data_type=0,
            max_documents=3,
            filter=filter_condition,
            query_expansion_condition=2,
        )
        try:
            documents = retriever.invoke(query)
            sources = [doc.metadata["source"] for doc in documents]
            logger.info("\n\nここですよ\n\n")
            return str(documents), sources
        except Exception as e:
            return f"Failed to retrieve data: {str(e)}"

    # https://console.cloud.google.com/gen-app-builder/locations/global/engines/immigration-advise-search_1720277205703/data/documents?project=vaulted-zodiac-253111
    # @lru_cache(maxsize=128)
    def initialize_llm_chain(self):
        tools = [
            Tool(
                name="search_immigration_database",
                func=self.search_immigration_database,
                description="This tool provides visas and immigration information. ",
            )
        ]
        try:
            llm = ChatVertexAI(model=MODEL_NAME)
        except Exception as e:
            logger.info(f"Error initializing VertexAI: {e}")
            raise
        return initialize_agent(
            tools=tools,
            llm=llm,
            prompt=self.prompt,
            memory=self.memory,
            verbose=True,
            agent_type="zero-shot-react-description",
        )

    def get_response(self, messages) -> str:
        chat_model = ChatVertexAI(project=PROJECT_ID, model=MODEL_NAME)
        return chat_model.predict_messages(messages)

    def get_RAG_response(self, messages, response_search_immigration: str) -> str:
        chat_model = ChatVertexAI(project=PROJECT_ID, model=MODEL_NAME)
        messages.append(AIMessage(response_search_immigration))
        return chat_model.predict_messages(messages)

    def _update_memory(self, msg_input: str, response: str) -> None:
        self.memory.save_context({"input": msg_input}, {"output": response})

    def get_HumanMessageContent(self, message):
        return HumanMessage(content=message["content"])

    def get_AIMessageContent(self, message):
        return AIMessage(content=message["content"])
