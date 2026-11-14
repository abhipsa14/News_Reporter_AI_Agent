from crewai import Agent
from dotenv import load_dotenv
from tools import tool
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
## Call the genai models

llm=ChatGoogleGenerativeAI(model="",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

## Creating a senior researcher agent with memory and verbose mode

researcher=Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=("Driven by curiosity, you're at the forefront of"
               " technological innovation, seeking to uncover the next big breakthrough."),
               tools=[tool],
               llm=llm,
               allow_delegation=True)

## creating a writer agent with custom tools responsible in writing news blog
news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you have a talent for making technology accessible to everyone."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)