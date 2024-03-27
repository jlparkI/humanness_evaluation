"""Retrieves train-test data and organizes it appropriately."""
import os
import tarfile
import wget


def main():
    url = "https://zenodo.org/records/10864595/files/train_test_data_immunogenicity_0.0.3.tar.gz"
    if "train_test_data_immunogenicity_0.0.3.tar.gz" not in os.listdir():
        filename = wget.download(url)
        with tarfile.open(filename) as tf:
            tf.extractall()
        os.remove(filename)


if __name__ == "__main__":
    main()
