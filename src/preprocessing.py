def convertJSONToText(resource):
    textFile = []
    issue = resource["issue"]
    description = resource["description"]
    textFile.append("Issue: " + issue + "\n")
    textFile.append("Description: " + description + "\n")
    links = resource["links"]
    textFile.append("\nResources:\n")

    for link in links:
        textFile.append("- " + link + "\n")
        textFile.append("\n")
    return "".join(textFile)
