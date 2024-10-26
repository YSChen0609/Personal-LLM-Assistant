from langchain.agents import initialize_agent, Tool
from langchain.llms import GPT4All
from langchain.memory import ConversationBufferMemory
from modules.email_handler import EmailHandler
from modules.pdf_reader import PDFReader
from modules.meeting_scheduler import MeetingScheduler
from modules.internet_search import InternetSearch
from modules.user_interaction import UserInteraction
from modules.privacy_manager import PrivacyManager

def main():
    # Initialize components
    llm = GPT4All(model="./ggml-gpt4all-j-v1.3-groovy.bin") # local LLM model
    memory = ConversationBufferMemory(memory_key="chat_history")
    email_handler = EmailHandler()
    pdf_reader = PDFReader()
    meeting_scheduler = MeetingScheduler()
    internet_search = InternetSearch()
    user_interaction = UserInteraction()
    privacy_manager = PrivacyManager()

    tools = [
        Tool(
            name="Email",
            func=email_handler.handle,
            description="Useful for sending emails"
        ),
        Tool(
            name="PDFReader",
            func=pdf_reader.read,
            description="Useful for reading PDF files"
        ),
        Tool(
            name="MeetingScheduler",
            func=meeting_scheduler.schedule,
            description="Useful for scheduling meetings"
        ),
        Tool(
            name="InternetSearch",
            func=internet_search.search,
            description="Useful for searching the internet"
        ),
    ]

    agent = initialize_agent(
        tools, 
        llm, 
        agent="conversational-react-description", 
        memory=memory,
        verbose=True
    )

    while True:
        user_input = user_interaction.get_input()
        if privacy_manager.is_private_info(user_input):
            response = llm(user_input)  
        else:
            response = agent.run(user_input)
        user_interaction.display_output(response)

if __name__ == "__main__":
    main()