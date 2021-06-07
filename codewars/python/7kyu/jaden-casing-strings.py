import unittest


def to_jaden_case(string):
    answer = ""
    is_first_char = True

    for idx, char in enumerate(string):
        if is_first_char:
            answer += char.upper()
            is_first_char = False
        else:
            answer += char

        if char == ' ':
            is_first_char = True

    return answer


class TestToJadenCase(unittest.TestCase):
    def testToJadenCase(self):
        quote = "How can mirrors be real if our eyes aren't real"
        self.assertEqual(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")


if __name__ == '__main__':
    unittest.main()
