import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo 
from dotenv import load_dotenv

load_dotenv()

news_agent = Agent(
    name="News Agent",
    model=Groq(id="llama-3.3-70b-versatile"), 
    tools=[DuckDuckGo()], 
    instructions=[
        "Search for the latest financial news about the given company.",
        "Summarize the top news articles.",
        "Provide key insights in markdown format."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

market_analysis_agent = Agent(
    name="Market Analysis Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Analyze recent stock trends based on financial news data.",
        "Identify key stock movements and patterns.",
        "Provide insights on market fluctuations."
    ],
    markdown=True,
    debug_mode=True,
)
sentiment_analysis_agent = Agent(
    name="Sentiment Analysis Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Perform sentiment analysis on the latest financial news.",
        "Determine whether the sentiment is positive, negative, or neutral.",
        "Provide a brief sentiment summary."
    ],
    markdown=True,
    debug_mode=True,
)
try:
    print("\n🔹 Fetching Financial News...")
    news_agent.print_response("Find and summarize the latest financial news about Tesla and NVIDIA.", stream=True)

    print("\n🔹 Performing Market Analysis...")
    market_analysis_agent.print_response("Analyze stock trends based on the news provided above.", stream=True)

    print("\n🔹 Performing Sentiment Analysis...")
    sentiment_analysis_agent.print_response("Analyze sentiment of the news provided above.", stream=True)

except Exception as e:
    print(f"Error: {e}")