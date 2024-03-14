import os
import pandas as pd
from antpack import SequenceScoringTool



def main(fpath):
    """Uses a sequence scoring tool to assign to clusters
    all of the sequences in the heavy and light files, then
    save the results back to disk with an additional column
    appended containing this information. This may take a
    minute since there are a few million sequences."""
    score_tool = SequenceScoringTool(adjusted_scores = False)

    os.chdir(fpath)

    for chain in ["heavy", "light"]:
        print(f"Now working on {chain}")

        raw = pd.read_csv(f"{chain}_cab_vdj_assigned.csv.gz")

        seqs = raw.sequence_aa.tolist()
        assignments = []

        for i in range(0, len(seqs), 10000):
            seq_batch = seqs[i:i+10000]

            assignments += score_tool.batch_score_seqs(seq_batch,
                            mode="assign").tolist()
            print(f"Done {i}")

        raw["SAM_cluster_weighted"] = assignments

        raw.to_csv(f"{chain}_cab_vdj_assigned.csv.gz",
                index=False)



if __name__ == "__main__":
    fpath = os.path.abspath(os.path.dirname(__file__))
    main(fpath)
