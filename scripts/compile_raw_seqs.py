"""Contains routines for compiling raw downloads from OAS into single
gzipped csv."""
from Bio import SeqIO
from antpack import SingleChainAnnotator


def process_raw(in_fname, out_fname, chain_type="heavy"):
    """Processes all the .gz files in a target directory and
    converts them to a single gzipped csv containing all of the
    sequences from the input plus selected extracted information.
    Once this step has been run, the much larger raw OAS downloads
    can be deleted."""
    sc_annotator = SingleChainAnnotator()

    if chain_type == "heavy":
        min_length = 110
    else:
        min_length = 105

    out_seqrecs = []

    with open(in_fname, "r", encoding="utf-8") as inhandle:
        for seqrec in SeqIO.parse(inhandle, 'fasta'):
            try:
                nseq = str(seqrec.seq.translate())
            except:
                continue
            _, percent_ident, _, err = sc_annotator.analyze_seq(nseq)
            if err != "":
                continue
            if percent_ident < 0.85:
                continue
            if len(nseq) < min_length:
                continue
            out_seqrecs.append(seqrec)

    print(f"Chain {chain_type}, retrieved {len(out_seqrecs)} useful sequences.")
    with open(out_fname, "w+", encoding="utf-8") as outhandle:
        SeqIO.write(out_seqrecs, outhandle, "fasta")

if __name__ == "__main__":
    process_raw("cAb-Rep_heavy.nt.fasta", "cab_heavy.fasta",
            "heavy")
    process_raw("cAb-Rep_light.nt.fasta", "cab_light.fasta",
            "light")
