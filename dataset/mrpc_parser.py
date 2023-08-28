class MRPCParser:
  def __init__(self, location_folder):
    self.location_folder = location_folder
    self.__parse_data()
  
  def __parse_data(self):
    """
    Load and parse the MSRP dataset.
    """
    train_location = self.location_folder + '/train.txt'
    test_location = self.location_folder + '/test.txt'

    self.test_data = self.__parse_file(test_location)
    self.train_data = self.__parse_file(train_location)

  def __parse_file(self, filename):
    data = []
    with open(filename, 'r', encoding='utf8') as f:
        f.readline()  # skipping the header of the file
        for line in f:
            text = line.strip().split('\t')
            item = {
                'sen_1': text[3],
                'sen_2': text[4],
                'label': int(text[0])
            }
            data.append(item)
    return data