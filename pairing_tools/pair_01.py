import pytest
from allpairspy import AllPairs

def function_to_be_tested(brand, operating_system, minute) -> bool:
    # do something
    if brand == 'Brand X' and operating_system == '988' and minute == 10 :
        return False
    else:
        return  True


class TestParameterized(object):
    @pytest.mark.parametrize(["brand", "operating_system", "minute"], [
        values for values in AllPairs([
            ["Brand X", "Brand Y"],
            ["98", "NT", "2000", "XP"],
            [10, 15, 30, 60]
        ])
    ])
    def test(self, brand, operating_system, minute):
        assert function_to_be_tested(brand, operating_system, minute)