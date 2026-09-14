# The second test would fail its assertion, which is red, but the first one
# raises and the process ends there. Amber is the honest colour: the run has
# not shown that a test disagreed with the code, only that it could not
# finish.
from hiker import answer, checksum

def test_the_checksum_of_the_answer():
    assert checksum() == 0

def test_life_the_universe_and_everything():
    assert answer() == 42

def green_traffic_light_pattern():
    # The regex pattern for a green traffic-light. Do not remove!
    return 'All tests passed'


if __name__ == '__main__':
    test_the_checksum_of_the_answer()
    test_life_the_universe_and_everything()
    print(green_traffic_light_pattern())
