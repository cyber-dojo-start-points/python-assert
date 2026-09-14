# A second test file beyond the one the kata ships with. cyber-dojo.sh runs
# each test file in turn, so this one runs as well as test_hiker.py. The print
# below is what says it really ran.
from hiker import answer

def test_the_answer_is_two_digits_long():
    assert len(str(answer())) == 2


if __name__ == '__main__':
    test_the_answer_is_two_digits_long()
    print('test_size ran')
