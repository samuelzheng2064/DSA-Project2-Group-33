# Genetic Sequence Identifier

### Team 33: Bellina Milito, Anish Subramanian, Samuel Zheng

## Overview: 
Python program that implements Knuth-Morris-Pratt and Rabin-Karp algorithms to identify specific genetic sequences within large DNA datasets.

## Motivation: 
In bioinformatics and medical software development, rapid and memory‑efficient sequence matching is essential for early disease diagnosis and genetic research. Our program demonstrates how optimized algorithms can process millions of base pairs while searching against thousands of known mutations — enabling faster, more scalable clinical analysis.

## Features: 
- Genome loading: 
  - Supports FASTA genome files of any size
  - Automatically skips FASTA header lines, cleans whitepasce, and concatenates all sequence lines into a single continuous DNA string
  - Ensures consistent formatting by converting all bases to uppercase

- Flexible input options
  - CSV mutation database input
      - Allows to search for multiple mutation motifs in one run
  - Single mutation input
      - Warns when an inputted sequence has non-DNA characters to detect input typos

- Function selection options
  - KMP Algorithm : Efficent prefix-based pattern matching using and LPS table to skip redundant comparisons
  - Rabin-Karp Algorithm : Rolling hash-based matching optimized for scanning large genomes
  - Dual-Mode comparison : Users can run both algorithms in a single run to compare preformance and optimize accuracy. 

- Benchmarking : Every run reports search time, whether the mutation was found, all indicies where the mutation occurs, and which algorithm was used.

## Project structure: 
main/

|-- .idea

|-- _pycache_ : python cache

|-- benchmark.py : preformance benchmarking 

|-- data_loader.py : FASTA + CSV parsing + DNA validation

|-- kmp_search.py : KMP algorithm 

|-- main.py : CLI entry point

|-- rabinKarp.py : Rabin-Karp algorithm

|-- test.py : testing utilities


## Requirements:
Python 3

## How to run:
Download a FASTA genome file into that folder. We used the E. coli K-12 reference genome (NCBI accession U00096.3). You also use the same file as us by seeing the References section below for the download link. However, any FASTA file will also work.
Open a terminal in that folder and run python3 main.py
Then follow the prompts

## Example usage: 

=== Exact Sequence Motif Finder ===

Enter path to main DNA sequence: ecoli_U00096.3.fasta

Loaded DNA sequence with 4641652 base pairs.


|

Enter red flag mutation sequence (or path to database): ATGCGTACGT

|

Choose a search algorithm:
1. KMP
2. Rabin-Karp
3. Both
Enter 1, 2, or 3: 3

|

Initializing search...

|

Analysis Complete

Mutation 'ATGCGTACGT' found at index 708333

Mutation 'ATGCGTACGT' found at index 1068458

|

--- Performance Benchmark ---

Strategy Employed: KMP Algorithm

Algorithm Execution Time: 0.089552 seconds

|

Analysis Complete

Mutation 'ATGCGTACGT' found at index 708333

Mutation 'ATGCGTACGT' found at index 1068458

|

--- Performance Benchmark ---

Strategy Employed: Rabin-Karp Algorithm

Algorithm Execution Time: 0.120381 seconds


## References: 
National Center for Biotechnology Information (NCBI). (2013). Escherichia coli str. K‑12 substr. MG1655, complete genome (Accession No. U00096.3).  https://www.ncbi.nlm.nih.gov/nuccore/U00096.3 (ncbi.nlm.nih.gov in Bing)

