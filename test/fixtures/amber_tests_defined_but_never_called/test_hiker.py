# There is no framework here to find these and call them, so the __main__
# block at the foot of the file is what runs a test. The learner has written
# tests and removed that block, so the file is imported, the defs are made,
# and no assertion is ever evaluated. The second test would fail.
from hiker import answer

def test_life_the_universe_and_everything():
    assert answer() == 42

def test_the_answer_is_two_digits_long():
    assert len(str(answer())) == 2
