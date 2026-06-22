from rabinKarp import rabinKarpSearch
from benchmark import benchmarkAlgorithm

if __name__ == "__main__":
    #mock data
    sampleGenome = "ATGCGATCGTACGATGCGTACGTATGCGTACGGTTACGATGCGT"
    targetMutation = "ATGCGT"

    print("Initializing search...")

    #testing rabin karp
    benchmarkAlgorithm(
        searchFunction=rabinKarpSearch,
        textSequence=sampleGenome,
        patternSequence=targetMutation,
        strategyName="Rabin-Karp Algorithm"
    )