from dataset import MRPCParser

def main():
    parser = MRPCParser('dataset/raw_data/mrpc')
    train_data = parser.train_data
    train_data_count = len(train_data)
    print(f"Number of train pairs is {train_data_count}")
    test_data = parser.test_data
    test_data_count = len(test_data)
    print(f"Number of test pairs is {test_data_count}")
    

if __name__ == "__main__":
    main()