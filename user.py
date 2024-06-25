from uagents import Agent, Context

# Create the user agent
user_agent = Agent(name="user_agent", seed="user_secret_seed")

# Define the response handler
@user_agent.handle("form_info_response")
async def handle_form_info_response(ctx: Context, response: dict):
    print(response)

# Send a query to the organization agent
async def query_organization_agent():
    # Replace 'organization_agent_address' with the actual address of the organization agent
    await user_agent.send("organization_agent_address", "get_form_info", {"form_type": "contact_form"})

# Run the user agent
if __name__ == "__main__":
    import asyncio

    # Start the user agent and send the query
    user_agent.run()
    asyncio.run(query_organization_agent())
