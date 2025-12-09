from embed import model

def retrieveClosestIssueAssociated(document, userRequest, faissIndex, k=3):
    closest = []
    embeddedUserRequest = model.encode([userRequest])
    distance, ind = faissIndex.search(embeddedUserRequest, k)
    ind = ind[0]
    for i in ind:
        closest.append(document[i])
    return closest
