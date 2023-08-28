import os

def download_corpus():
    """
      Downloading corpus files from another repo.
    """
    files = [
      ('vrublevskiyvitaliy/paraphrase_identification/contents/dataset/msr-paraphrase-corpus/msr_paraphrase_train.txt', 'train.txt'),
      ('vrublevskiyvitaliy/paraphrase_identification/contents/dataset/msr-paraphrase-corpus/msr_paraphrase_test.txt', 'test.txt'),
    ]
    os.system("cd raw_data && mkdir mrpc")
    for (file, part) in files:
       os.system(f"curl -o raw_data/mrpc/{part} --remote-name -H 'Accept: application/vnd.github.v3.raw' --location https://api.github.com/repos/{file}")

download_corpus()