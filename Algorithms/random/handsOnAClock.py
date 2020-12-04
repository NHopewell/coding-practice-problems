"""
360 degrees in a circle

30 degrees between each hour OR each 5 mins

{
    1:, 5,
    2: 10,
    3: 15,
    4: 20,
    5: 25,
    6: 30,
    7: 35,
    8: 40,
    9: 45,
    10: 50,
    11: 55,
    12: 00
}

hours = 12 minutes = 30

30 - 0 / 5 = 6

6 * 30 = 180
360 - 180 = 180

if minutes == 30: minus 15 degrees from first angle, add it to second
if minutes == 15: minus 7.5 degrees from first angle, add it to second
take min
"""
import pytest


def get_smaller_angle(hour: int, minutes: int) -> int:
    
    degrees_total = 360
    degrees_per_hour = 30
    
    clock = {
        1: 5,
        2: 10,
        3: 15,
        4: 20,
        5: 25,
        6: 30,
        7: 35,
        8: 40,
        9: 45,
        10: 50,
        11: 55,
        12: 00
    }
    
    if minutes == clock[hour]:
        if minutes in (15, 45):
            first_angle = 7.5
            second_angle = degrees_total - first_angle
            
        else:
            return 0
    else:
    
        base = (minutes - clock[hour]) / 5  
        first_angle = base * degrees_per_hour
        second_angle = degrees_total - first_angle

        if minutes == 30:
            first_angle -= 15
            second_angle += 15
        elif minutes == 15:
            first_angle -= 7.5
            second_angle += 7.5
    
    
    return min(first_angle,second_angle)
    
    

    
####################################

def test_get_smaller_angle_case_one():
    
    hour, minute = 12, 30
    
    expected = 165
    
    actual = get_smaller_angle(hour, minute)
    
    assert actual == expected
    
    
def test_get_smaller_angle_case_two():
    
    hour, minute = 3, 30
    
    expected = 75
    
    actual = get_smaller_angle(hour, minute)
    
    assert actual == expected
    
    
def test_get_smaller_angle_case_three():
    
    hour, minute = 3, 15
    
    expected = 7.5
    
    actual = get_smaller_angle(hour, minute)
    
    assert actual == expected
    
    
if __name__ == '__main__':
    pytest.main()