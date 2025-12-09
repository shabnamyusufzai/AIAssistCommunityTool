from openai import OpenAI
client = OpenAI()
def promptModel(userRequest, topIssueLinks):
    formattedLinks = "\n\n\n".join(topIssueLinks)
    prompt = """You are a chatbot chatting with a user. The user is presenting you 
    with an issue that they have. Please respond to them with the links that will be 
    useful to them. This is the users inquiry: """ + userRequest + """\nHere are 
    the links that will help them: """ + formattedLinks + """Your instructions include:
    Respond to them politely, include the links that will be useful to them,
    and ask if they are having any other issues you can help with."""
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    result = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages 
    )
    result = result.choices[0].message.content
    return result
