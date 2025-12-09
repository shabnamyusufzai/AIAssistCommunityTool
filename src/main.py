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


    # ---------------------------------------------------------
    # Using gradio to launch the chatbot UI
    with gradio.Blocks() as demo:
        chatbot = gradio.Chatbot(height=600)
        userInput = gradio.Textbox(placeholder="What can I help you with?")
        userInput.submit(
            returnOutput, 
            [userInput, chatbot],
            [chatbot, userInput]
        )
    demo.launch()
    # --------------------------------------------------------

    
    # To test accuracy, precision, recall
    # Comment the code below in and the block of gradio code out for precision, recall, F1, and accuracy
    # ---------------------------------------------------------

    # testData = json.load(open("data/testData.json"))
    # testDataResults = []
    # totalTP = 0
    # totalPrecision = 0
    # totalRecall = 0
    # totalF1 = 0
    # fIndex = embedAndFaiss(document)
    # for test in testData:
    #     userQuery = test["query"]
    #     issue = test["issue"]
    #     topIssueLinks = retrieveClosestIssueAssociated(document, userQuery, fIndex,1)
    #     firstIssue = topIssueLinks[0].split("Issue:")[1].split("Description:")[0].strip()
    #     truePos, precision, recall, F1 = calculatePrecisionRecallF1(issue, [firstIssue],1)
    #     testDataResults.append(
    #         {
    #             "precision": precision,
    #             "recall": recall,
    #             "F1": F1 
    #         }
    #     )
    #     totalPrecision = totalPrecision + precision
    #     totalRecall = totalRecall + recall
    #     totalF1 = totalF1 + F1
    #     totalTP = totalTP + truePos
    # totalPrecision = totalPrecision / 36
    # totalRecall = totalRecall / 36
    # totalF1 = totalF1 / 36
    # accuracy = totalTP / 36
    # print(totalPrecision)
    # print(totalRecall)
    # print(totalF1)
    # print(accuracy)


if __name__ == "__main__":
    main()
