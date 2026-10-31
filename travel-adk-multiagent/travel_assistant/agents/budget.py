
from google.adk.agents import Agent

from travel_assistant.tools.budget_tools import estimate_trip_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-3.8-flash",
    description="Agent specialized in estimating travel budgets.",
    instruction="""
    You are a travel budget assistant.

    Your task is to help users estimate the cost of their trips.

    Ask for the destination, number of days and daily budget when necessary.
    Use the estimate_trip_budget tool to calculate the estimated total.

    Explain the budget calculation clearly.
    Always indicate that the result is an estimate, not a confirmed price.
    """,
    tools=[estimate_trip_budget],
)
