import unittest


def is_isogram(string):
    history = {}
    for c in string.lower():
        if c in history:
            return False
        history[c] = ""
    return True



class TestIsIsogram(unittest.TestCase):
    def test_is_isogram(self):
        test_cases = [
            {
                'string': 'Dermatoglyphics',
                'output': True
            },
            {
                'string': 'aba',
                'output': False
            },
            {
                'string': 'moOse',
                'output': False
            }
        ]
        for test_case in test_cases:
            string = test_case['string']
            expected = test_case['output']
            self.assertEqual(is_isogram(string), expected)


if __name__ == '__main__':
    unittest.main()
