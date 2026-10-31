
from google.adk.agents import Agent

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-3.8-flash",
    description="Agent specialized in searching travel information.",
    instruction="""
    You are a travel research assistant.

    Your task is to provide useful information about travel destinations,
    including attractions, transportation, accommodation and local recommendations.

    Respond in a clear and organized way.
    Do not invent current prices, schedules or availability.
    If information may change, indicate that it should be verified.
    """
)
