# Genetic Sequence Identifier

### Team 33: Bellina Milito, Anish Subramanian, Samuel Zheng

## Overview: 
Python program that implements Knuth-Morris-Pratt and Rabin-Karp algorithms to identify specific genetic sequences within large DNA datasets.

## Motivation: 
In bioinformatics and medical software development, rapid and memory‑efficient sequence matching is essential for early disease diagnosis and genetic research. Our program demonstrates how optimized algorithms can process millions of base pairs while searching against thousands of known mutations — enabling faster, more scalable clinical analysis.

## Features: 
-Genome loading

-Multiple input options

-Function selection between the KMP algorithm, Rabin-Karp algorithm, or both

-Benchmarking

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

Mutation 'ATGCGT' found at index 45012

Mutation 'ATGCGT' found at index 89201

|

--- Performance Benchmark ---

Strategy Employed: KMP Algorithm

Algorithm Execution Time: 0.120381 seconds

|

Analysis Complete

Mutation 'ATGCGT' found at index 45012

Mutation 'ATGCGT' found at index 89201

|

--- Performance Benchmark ---

Strategy Employed: Rabin-Karp Algorithm

Algorithm Execution Time: 0.089552 seconds


## References: 
National Center for Biotechnology Information (NCBI). (2013). Escherichia coli str. K‑12 substr. MG1655, complete genome (Accession No. U00096.3).  https://www.ncbi.nlm.nih.gov/nuccore/U00096.3 (ncbi.nlm.nih.gov in Bing)

