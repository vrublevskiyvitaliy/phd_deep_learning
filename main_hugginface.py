from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def encode(examples):
    return tokenizer(examples['sentence1'], examples['sentence2'], truncation=True, padding='max_length')

def main():
    dataset = load_dataset('glue', 'mrpc', split='train')
    model = AutoModelForSequenceClassification.from_pretrained('bert-base-cased')
    tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
    dataset = dataset.map(encode, batched=True)
    return dataset[0]

if __name__ == "__main__":
    print(main())