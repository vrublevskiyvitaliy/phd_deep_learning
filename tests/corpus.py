import unittest

from dataset.mrpc_parser import MRPCParser

class TestMRPCParser(unittest.TestCase):
    def get_parser(self):
        return MRPCParser('dataset/raw_data/mrpc')

    def test_size_train_test_blocks(self):
        parser = self.get_parser()
        count_test = len(parser.test_data)
        count_train = len(parser.train_data)
        self.assertEqual(count_test, 1725)
        self.assertEqual(count_train, 4076)
        

if __name__ == '__main__':
    unittest.main()