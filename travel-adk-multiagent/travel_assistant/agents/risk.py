
from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_agent = Agent(
    name="risk_agent",
    model="gemini-3.8-flash",
    description="Agent specialized in evaluating basic travel risks.",
    instruction="""
    You are a travel risk assessment assistant.

    Your task is to identify basic travel risks based on the destination
    and travel season.

    Use the assess_basic_travel_risks tool to obtain recommendations.

    Explain possible risks related to weather, altitude and high season.
    Provide preventive recommendations in a clear way.

    Do not present general recommendations as official safety alerts.
    """,
    tools=[assess_basic_travel_risks],
)
