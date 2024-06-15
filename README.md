# Form_Fusion
organization.py:

Starts and waits for incoming queries.
When it receives a query for "get_form_info" with the form type "contact_form", it looks up the form details in the forms dictionary and sends back the response.

user.py:

Starts and sends a query to the organization.py agent.
Receives the response and prints the form information to the console.
