#Importing modules to support the functionality of the tf_search application
import argparse
import re
import sys
from collections import namedtuple
import doctest

def read_options()->argparse.Namespace:
    """
    Parses the command-line options passed when this Python application is run.

    Returns:
        argparse.Namespace: Parsed arguments including:
            - sequence (str): Path to a FASTA format file containing a DNA sequence.
            - outfile (str): Path to an output file where the results will be stored.
            - tfs (list[str] | None): Optional list of transcription factors to search for,
              provided as space-separated values. If omitted, all default transcription factors
              provided in the Babraham Institute file 'human_tf_consensus.tsv' will be used.
    Example:
        To run the application with all transcription factors:

            $ python tf_search.py input.fa results.csv

        To specify transcription factors manually:

            $ python  tf_search.py input.fa results.csv --tfs HUMAN:FOXK1 HUMAN:ISL1
    """
    parser = argparse.ArgumentParser(description = "Analyse the options for the transcription factor search application.")
    parser.add_argument("sequence", type = str, help = "File path to a FASTA format file containing a DNA sequence")
    parser.add_argument("outfile", type = str, help = "File path to an output file to store the result of the application.")
    parser.add_argument("--tfs", nargs='+', help="List of transcription factors")
    return parser.parse_args()

def read_sequence(seq_arg:str)->dict:
    """
    Converts the FASTA format input file, saved at the file path argument, into a named tuple to summarise the name of the sequence and
    the contents of the sequence in an uninterrupted string.

    Parameters:
    - seq_arg (str): File path to a FASTA format file.

    Returns:
    - namedtuple: A named tuple summarising the name and contents of the sequence in the input file.

    Examples:
    >>> read_sequence('C:/Users/rebec/Documents/babraham_intro_python/babraham_intro_python/Transcription Factors/scyl3_promoter.fa')
    Sequence(seq_name='SCYL3', seq_whole='TATCTCTCATTATCTCTGCTATACTACGGGTGCATCTGTTAACCAAAGCAGCTACTGAGTGGGTAATGAGTGGATACTGTACACAGCGCGGCTACCTGCGACAGATGATTCGCGTCAAGGGTGGGACAGAGTGGATGGCCCGAGATTTAATCGGGCTACTCAGAATACAGGCGGTTTGAAACTTAAGAATTGTTTATTTCTGGAGTTTTCCATTTAACATTTCTGAACCAAGGTTTGACCACAGGTAACTGACACTGCAGAAAGCATGGAGGGGGGCAAAACTACTGCATTAATATTAAAATTTTCAAATATTACTTTTTGCTAAATGAAATGTGATTCAGGACCTTCCCTCTCAAAGATCAAGCGAGATCACCACGACCTCCGCCAGCAGCGGCTCTGCACGACTCCACCCTCGCAGCCCAGCCAATCAAAGCTACAGGTTGAGTGACGTCACTCTCCTGAAAGTCCTCGCTAATTCCCGTACTCCTTTTCTCCGCCCT')
    
    Note to self: I have chosen a namedtuple as the data structure to store the name and the contents of the FASTA file because it allows key-based retrieval of
    the values, but is immutable so that the sequence cannot be changed from that read in from the file.
    """
    Sequence = namedtuple("Sequence", ["seq_name", "seq_whole"])
    with open(seq_arg, "rt", encoding = "UTF-8") as f:
        seq_strip = list(map(str.strip, f))
        seq_whole = "".join(seq_strip[1:]).upper()
        seq_name = seq_strip[0].lstrip(">")
        return Sequence(seq_name, seq_whole)

def re_repl(cons_seq:str)->str:
    """
    Function to replace the ambiguity codes in a DNA sequence with regular expressions representing the bases that could exist in the place of the ambiguity codes.

    Parameters:
    - cons_seq (str): a DNS consensus sequence with ambiguity codes rather than DNA bases. 

    Returns:
    - str: a string containing the original DNS consensus sequence, modified so that its ambiguity codes are replaced with regular expressions for the possible DNA bases.

    Example:
    >>> re_repl('DKSMGCRGGGCMDKDRDV')
    '[AGT][TG][GC][CA]GC[AG]GGGC[CA][AGT][TG][AGT][AG][AGT][ACG]'
    """

    re_dict = dict(zip("YRWSKMDVHB", ["[CT]", "[AG]", "[AT]", "[GC]", "[TG]", "[CA]", "[AGT]", "[ACG]", "[ACT]", "[CGT]"]))
    arg_seq = cons_seq
    for code, repr in re_dict.items():
        cons_re = re.sub(code, repr, arg_seq)
        arg_seq = cons_re
    return cons_re

def read_tf_list(tf_sublist)->dict:
    """
    Function to read the transcription factor consensus sequences saved in the human_tf_consensus.tsv, and output a list of named
    tuples that contain the transcription factor name, consensus sequences, and a sequence with the ambiguity codes replaced with
    regular expressions for the equivalent DNA bases.

    Parameters:
    - tf_sublist (list): optional list of transcription factor names that can be used to filter restrict which transcription factors
    are read into the output list

    Returns:
    - list: list of named tuples that contain the transcription factor name, consensus sequences, and a sequence with the ambiguity
    codes replaced with regular expressions for the equivalent DNA bases.

    Example:
    >>> read_tf_list(['HUMAN:FOXK1'])
    [TransFact(tf='HUMAN:FOXK1', cons_seq='TGTTTHYHHB', re_seq='TGTTT[ACT][CT][ACT][ACT][CGT]')]
    """
    tf_filepath = "C:/Users/rebec/Documents/babraham_intro_python/babraham_intro_python/Transcription Factors/human_tf_consensus.tsv"
    TransFact = namedtuple("TransFact", ["tf", "cons_seq", "re_seq"])

    with open(tf_filepath, "rt", encoding = "UTF-8") as f:
        if tf_sublist != None:
            tf_cons_list = [line.split("\t")[1:3] for line in f if line.split("\t")[1] in tf_sublist]
        else:
            tf_cons_list = [line.split("\t")[1:3] for line in f]
    
    tf_re = list(map(lambda x: TransFact(x[0], cs:=x[1].upper(), re_repl(cs)), tf_cons_list))
    return tf_re

def search_for_tfs(sequence, tf_list):
    """
    Function to search for regular expression matches within a specified
    DNA sequence using a specified list of transcription factor sequences. 

    Parameters:
    - sequence (str): DNA sequence within which to search for transcription factor sequences
    - tf_list (list): list containing transcription factor DNA sequences to search for within
    the DNA sequence

    Returns:
    list: a list of dictionaries containing, for each match between a transcription factor sequence
    within the DNA sequence: the name of the sequence, the name of the transcription factor, the start
    and end position for the match, the consensus sequence for the transcription factor, the actual
    sequence matched during the search.

    Example:
    >>> Sequence = namedtuple("Sequence", ["seq_name", "seq_whole"])
    >>> TransFact = namedtuple("TransFact", ["tf", "cons_seq", "re_seq"])
    >>> search_for_tfs(Sequence(seq_name='SCYL3', seq_whole='TATCTCTCATTATCTCTGCTATACTACGGGTGCATCTGTTAACCAAAGCAGCTACTGAGTGGGTAATGAGTGGATACTGTACACAGCGCGGCTACCTGCGACAGATGATTCGCGTCAAGGGTGGGACAGAGTGGATGGCCCGAGATTTAATCGGGCTACTCAGAATACAGGCGGTTTGAAACTTAAGAATTGTTTATTTCTGGAGTTTTCCATTTAACATTTCTGAACCAAGGTTTGACCACAGGTAACTGACACTGCAGAAAGCATGGAGGGGGGCAAAACTACTGCATTAATATTAAAATTTTCAAATATTACTTTTTGCTAAATGAAATGTGATTCAGGACCTTCCCTCTCAAAGATCAAGCGAGATCACCACGACCTCCGCCAGCAGCGGCTCTGCACGACTCCACCCTCGCAGCCCAGCCAATCAAAGCTACAGGTTGAGTGACGTCACTCTCCTGAAAGTCCTCGCTAATTCCCGTACTCCTTTTCTCCGCCCT'),[TransFact(tf='HUMAN:FOXK1', cons_seq='TGTTTHYHHB', re_seq='TGTTT[ACT][CT][ACT][ACT][CGT]')] )
    [{'seq_name': 'SCYL3', 'tf_name': 'HUMAN:FOXK1', 'start_pos': 190, 'end_pos': 200, 'cons_seq': 'TGTTTHYHHB', 'match_seq': 'TGTTTATTTC'}]

   """
    results = []
    seq = sequence.seq_whole
    for ntuple in tf_list:
        m = list(re.finditer(ntuple.re_seq, seq))
        if len(m)> 0:
            for i in m:
                match = {}
                match["seq_name"] = sequence.seq_name
                match["tf_name"] = ntuple.tf
                match["start_pos"] = i.span()[0]
                match["end_pos"] = i.span()[-1]
                match["cons_seq"] = ntuple.cons_seq
                match["match_seq"] = i.group()
                results.append(match)
    return results

def print_hits(hits, outfile):
    """
    Function to receive the path to an output file from the command line arguments and write information about the transcription factor sequences present in the DNA sequence:

    Parameters:
    - hits (list): a list of dicionaries containing information about the transcription factors present within the DNA sequence.
    This includes: the name of the DNA sequence, the name of the transcription factor, the start and end positions of the transcription factor sequences, 
    a consensus sequence for the transcription factor, and a sequence for the transcription factor with the ambiguity codes replaced with DNA base regular expressions.
    - outfile (str): a file path to the output file that the information will be written to.

    """

    delimiter = ","
    headers = ["sequence", "transcription factor (TF)", "start position", "end position", "TF consensus sequence", "TF actual sequence"]
    first_line = delimiter.join(headers)
    with open(outfile, "wt", encoding = "UTF-8") as f:
        print(first_line, file = f)
        for hit in hits:
            output = [hit["seq_name"], hit["tf_name"], hit["start_pos"], hit["end_pos"], hit["cons_seq"], hit["match_seq"]]
            output_str = [str(i) for i in output]
            line = delimiter.join(output_str)
            print(line, file = f)



def main():
    options = read_options()
    sequence = read_sequence(options.sequence)
    tf_list = read_tf_list(options.tfs)
    hits = search_for_tfs(sequence, tf_list)
    print_hits(hits, options.outfile)

main()
