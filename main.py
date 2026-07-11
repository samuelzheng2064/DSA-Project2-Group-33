import os

from data_loader import read_genome, read_mutations, is_dna_sequence
from kmp_search import kmp_search
from rabinKarp import rabinKarpSearch
from benchmark import benchmarkAlgorithm


def main():
    print("=== Exact Sequence Motif Finder ===")

    genome_path = input("Enter path to main DNA sequence: ").strip()
    if not os.path.exists(genome_path):
        print("That file does not exist. Please check the path and try again.")
        return

    genome = read_genome(genome_path)
    print("Loaded DNA sequence with " + str(len(genome)) + " base pairs.")

    mutation_input = input("Enter red flag mutation sequence (or path to database): ").strip()

    # figure out if they typed a sequence or gave us a csv file to load
    if mutation_input.lower().endswith(".csv") or os.path.exists(mutation_input):
        # they meant to give us a file, so make sure it actually exists before
        # we try to open it, otherwise read_mutations crashes on a bad path
        if not os.path.exists(mutation_input):
            print("That mutation file does not exist. Please check the path and try again.")
            return
        mutations = read_mutations(mutation_input)
        if len(mutations) == 0:
            print("No valid mutation sequences were found in that file.")
            return
        print("Loaded " + str(len(mutations)) + " mutation(s) from the database.")
    else:
        single_mutation = mutation_input.upper()
        if not is_dna_sequence(single_mutation):
            print("Warning: that does not look like a DNA sequence, searching anyway.")
        mutations = [single_mutation]

    print("")
    print("Choose a search algorithm:")
    print("  1. KMP")
    print("  2. Rabin-Karp")
    print("  3. Both")
    choice = input("Enter 1, 2, or 3: ").strip()

    print("")
    print("Initializing search...")

    for mutation in mutations:
        if choice == "1":
            benchmarkAlgorithm(kmp_search, genome, mutation, "KMP Algorithm")
        elif choice == "2":
            benchmarkAlgorithm(rabinKarpSearch, genome, mutation, "Rabin-Karp Algorithm")
        else:
            # anything other than 1 or 2 just runs both so we can compare them
            benchmarkAlgorithm(kmp_search, genome, mutation, "KMP Algorithm")
            benchmarkAlgorithm(rabinKarpSearch, genome, mutation, "Rabin-Karp Algorithm")


if __name__ == "__main__":
    main()
