import unittest


def digital_root(n):
    num = n
    while num >= 10:
        _n = num
        num = 0
        
        while _n > 0:
            num += _n % 10
            _n //= 10

    return num


class TestDigitalRoot(unittest.TestCase):
    def test_digital_root(self):
        test_cases = [
            {
                'n': 16,
                'expected': 7
            },
            {
                'n': 942,
                'expected': 6
            },
            {
                'n': 132189,
                'expected': 6
            },
            {
                'n': 493193,
                'expected': 2
            }
        ]
        for test_case in test_cases:
            n = test_case['n']
            expected = test_case['expected']
            self.assertEqual(digital_root(n), expected)


if __name__ == '__main__':
    unittest.main()
