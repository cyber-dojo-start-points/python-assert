# All three assertions are wrong, and the traceback names only the first.
# An uncaught AssertionError ends the process, so the two calls below it in
# __main__ never happen. A learner reading this sees one failure and has no
# way to tell how many more are waiting.
from hiker import answer

def test_life_the_universe_and_everything():
    assert answer() == 42

def test_the_answer_is_three_digits_long():
    assert len(str(answer())) == 3

def test_the_answer_is_the_question():
    assert str(answer()) == '6 * 7'

def green_traffic_light_pattern():
    # The regex pattern for a green traffic-light. Do not remove!
    return 'All tests passed'


if __name__ == '__main__':
    test_life_the_universe_and_everything()
    test_the_answer_is_three_digits_long()
    test_the_answer_is_the_question()
    print(green_traffic_light_pattern())
