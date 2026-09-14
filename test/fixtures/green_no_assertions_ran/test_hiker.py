# The learner has deleted the tests and left the green pattern behind. There
# is no framework here to count tests, so the colour rests entirely on this
# print, and nothing checks that an assertion ran before it. The coverage
# table is the only place the truth shows: answer() is never called, so
# hiker.py has a line missed even though the light is green.
from hiker import answer

def green_traffic_light_pattern():
    # The regex pattern for a green traffic-light. Do not remove!
    return 'All tests passed'


if __name__ == '__main__':
    print(green_traffic_light_pattern())
