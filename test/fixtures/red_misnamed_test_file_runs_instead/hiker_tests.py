# A learner who names a file this way expects it to be left alone, because
# that is what a framework doing discovery would do. The glob *test*.py has
# no such rule: it matches anywhere in the name, and hiker_tests.py sorts
# before test_hiker.py, so this is the file that runs and test_hiker.py is
# only an argument to it.
from hiker import answer

def test_the_answer_is_three_digits_long():
    assert len(str(answer())) == 3


if __name__ == '__main__':
    test_the_answer_is_three_digits_long()
