def rabinKarpSearch(textSequence: str, patternSequence: str, alphabetSize: int = 256,
                    primeModulus: int = 1000000007) -> list:

    matchIndices = []
    lengthOfText = len(textSequence)
    lengthOfPattern = len(patternSequence)

    if lengthOfPattern == 0 or lengthOfText < lengthOfPattern:
        return matchIndices

    patternHashValue = 0
    textHashValue = 0
    hashMultiplier = 1

    for characterIndex in range(lengthOfPattern - 1):
        hashMultiplier = (hashMultiplier * alphabetSize) % primeModulus


    for characterIndex in range(lengthOfPattern):
        patternHashValue = (alphabetSize * patternHashValue + ord(patternSequence[characterIndex])) % primeModulus
        textHashValue = (alphabetSize * textHashValue + ord(textSequence[characterIndex])) % primeModulus

    for windowStartIndex in range(lengthOfText - lengthOfPattern + 1):

        if patternHashValue == textHashValue:
            if textSequence[windowStartIndex: windowStartIndex + lengthOfPattern] == patternSequence:
                matchIndices.append(windowStartIndex)


        if windowStartIndex < lengthOfText - lengthOfPattern:
            textHashValue = (alphabetSize * (
                        textHashValue - ord(textSequence[windowStartIndex]) * hashMultiplier) + ord(
                textSequence[windowStartIndex + lengthOfPattern])) % primeModulus

            if textHashValue < 0:
                textHashValue = textHashValue + primeModulus

    return matchIndices