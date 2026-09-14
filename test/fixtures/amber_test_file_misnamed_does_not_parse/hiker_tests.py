# Half written, so it does not parse, and named in a way the learner expects
# to be left alone. The glob *test*.py matches it anyway and it sorts first,
# so this is the file coverage tries to run and the run gets no further.
from hiker import answer

def test_the_answer_is_two_digits_long():
    assert len(str(answer()) == 2
