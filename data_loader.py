import csv


def is_dna_sequence(text):
    if text == "":
        return False
    for letter in text:
        if letter not in "ACGT":
            return False
    return True


def read_genome(file_path):
    # fasta files have a ">" header line then the actual sequence split over a
    # bunch of lines, so skip the header and stick the rest together
    sequence_parts = []

    genome_file = open(file_path, "r")
    for line in genome_file:
        line = line.strip()
        if line == "" or line.startswith(">"):
            continue
        sequence_parts.append(line.upper())
    genome_file.close()

    return "".join(sequence_parts)


def read_mutations(file_path):
    # the csv might have a name column or a header row, so just grab whatever
    # in each row actually looks like DNA and ignore everything else
    mutations = []

    mutation_file = open(file_path, "r")
    reader = csv.reader(mutation_file)
    for row in reader:
        for field in row:
            candidate = field.strip().upper()
            if is_dna_sequence(candidate):
                mutations.append(candidate)
    mutation_file.close()

    return mutations
