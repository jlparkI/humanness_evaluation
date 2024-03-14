"""Retrieves train-test data and organizes it appropriately."""
import os
import wget
import tarfile


def main():
    url = "https://zenodo.org/records/10819061/files/train_test_data_immunogenicity_0.0.2.tar.gz"
    if "train_test_data_immunogenicity_0.0.2.tar.gz" not in os.listdir():
        filename = wget.download(url)
        tf = tarfile.open(filename)
        tf.extractall()
        tf.close()
        os.remove(filename)


if __name__ == "__main__":
    main()
