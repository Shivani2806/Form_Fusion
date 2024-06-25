from uagents import Agent, Context

# Define form data
forms = {
    "contact_form": {
        "description": "A form to collect user's contact details.",
        "organization": "Customer Service Department",
        "fields": ["Name", "Email", "Phone Number"]
    },
    "registration_form": {
        "description": "A form for user registration.",
        "organization": "User Registration Department",
        "fields": ["Username", "Password", "Email", "Date of Birth"]
    },
    "feedback_form": {
        "description": "A form to collect user feedback.",
        "organization": "Feedback and Support Department",
        "fields": ["Name", "Email", "Comments"]
    }
}

# Create the agent
agent = Agent(name="organization_agent", seed="organization_secret_seed")

# Define the query handler for form descriptions
@agent.handle("get_form_info")
async def get_form_info(ctx: Context, content: dict):
    form_type = content.get("form_type")
    if form_type in forms:
        form_info = forms[form_type]
        ctx.send("form_info_response", form_info)
    else:
        ctx.send("form_info_response", {"error": "Form type not found"})

# Run the agent
if __name__ == "__main__":
    agent.run()
