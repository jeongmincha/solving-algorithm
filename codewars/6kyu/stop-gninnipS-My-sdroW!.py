import unittest


def spin_words(sentence):
    answer_words = []
    words = sentence.split(' ')
    for word in words:
        if len(word) >= 5:
            answer_words.append(word[::-1])
        else:
            answer_words.append(word)
    
    return ' '.join(answer_words)


class TestSpinWords(unittest.TestCase):
    def testSpinWords(self):
        test_cases = [
            {
                'sentence': 'Welcome',
                'output': 'emocleW'
            },
            {
                'sentence': 'This is a test',
                'output': 'This is a test'
            },
            {
                'sentence': 'This is another test',
                'output': 'This is rehtona test'
            }
        ]
        for test_case in test_cases:
            sentence = test_case['sentence']
            expected = test_case['output']
            self.assertEqual(spin_words(sentence), expected)


if __name__ == '__main__':
    unittest.main()
