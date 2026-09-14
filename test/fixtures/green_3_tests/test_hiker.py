from hiker import answer

def test_life_the_universe_and_everything():
    assert answer() == 42

def test_the_answer_is_two_digits_long():
    assert len(str(answer())) == 2

def test_the_answer_is_not_the_question():
    assert str(answer()) != '6 * 7'

def green_traffic_light_pattern():
    # The regex pattern for a green traffic-light. Do not remove!
    return 'All tests passed'


if __name__ == '__main__':
    test_life_the_universe_and_everything()
    test_the_answer_is_two_digits_long()
    test_the_answer_is_not_the_question()
    print(green_traffic_light_pattern())
