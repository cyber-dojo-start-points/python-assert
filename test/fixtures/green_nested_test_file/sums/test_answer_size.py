# A test file in a sub-directory. cyber-dojo.sh finds test files at any depth
# and PYTHONPATH names the sandbox root, so this file runs and can import the
# source file sitting above it. The print below is what says it really ran.
from hiker import answer

def test_the_answer_is_two_digits_long():
    assert len(str(answer())) == 2


if __name__ == '__main__':
    test_the_answer_is_two_digits_long()
    print('nested test_answer_size ran')
