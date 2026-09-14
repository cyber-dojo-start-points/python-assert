# This sorts before test_hiker.py, so coverage runs this file and passes
# test_hiker.py to it as an argument. The failure here is the whole run.
from hiker import answer

def test_the_answer_is_three_digits_long():
    assert len(str(answer())) == 3


if __name__ == '__main__':
    test_the_answer_is_three_digits_long()
