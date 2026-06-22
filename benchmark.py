import time
from typing import Callable, List

def benchmarkAlgorithm(searchFunction: Callable[[str, str], List[int]], textSequence: str, patternSequence: str, strategyName: str) -> List[int]:

    startTime = time.perf_counter()

    foundIndices = searchFunction(textSequence, patternSequence)

    endTime = time.perf_counter()
    executionTime = endTime - startTime

    print("\nAnalysis Complete")
    if not foundIndices:
        print(f"No instances of mutation '{patternSequence}' were detected.")
    else:
        for matchIndex in foundIndices:
            print(f"Mutation '{patternSequence}' found at index {matchIndex}")

    print("\n--- Performance Benchmark ---")
    print(f"Strategy Employed: {strategyName}")
    print(f"Algorithm Execution Time: {executionTime:.6f} seconds")

    return foundIndices