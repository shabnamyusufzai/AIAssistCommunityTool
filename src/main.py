import os
import json
import gradio

from preprocessing import convertJSONToText
from embed import embedAndFaiss
from retrieve import retrieveClosestIssueAssociated
from prompting import promptModel

def main():
    os.environ["OPENAI_API_KEY"] = ""
    resources = json.load(open("data/IssuesAndLinks_Flattened.json"))
    userInput = "I need somewhere to sleep tonight."
    document = []
    for resource in resources:
        document.append(convertJSONToText(resource))

    fIndex = embedAndFaiss(document)

    def returnOutput(userIn, history):
        topIssueLinks = retrieveClosestIssueAssociated(document,userIn,fIndex)
        result = promptModel(userIn, topIssueLinks)
        history = []
        history.append((userIn, result))
        return history, ""

    with gradio.Blocks() as demo:
        chatbot = gradio.Chatbot(height=600)
        userInput = gradio.Textbox(placeholder="What can I help you with?")
        userInput.submit(
            returnOutput, 
            [userInput, chatbot],
            [chatbot, userInput]
        )
    demo.launch()
  
if __name__ == "__main__":
    main()
