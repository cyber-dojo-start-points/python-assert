from hiker import answer

def test_the_answer_is_two_digits_long():
    assert len(str(answer())) == 2

def test_the_answer_is_not_the_question():
    assert str(answer()) != '6 * 9'

def test_life_the_universe_and_everything():
    assert answer() == 42

def green_traffic_light_pattern():
    # The regex pattern for a green traffic-light. Do not remove!
    return 'All tests passed'


if __name__ == '__main__':
    # The two that pass are called first, so the one that fails is the last
    # thing the run reaches and nothing is left waiting behind it.
    test_the_answer_is_two_digits_long()
    test_the_answer_is_not_the_question()
    test_life_the_universe_and_everything()
    print(green_traffic_light_pattern())
