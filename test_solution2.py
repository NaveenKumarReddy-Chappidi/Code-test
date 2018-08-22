''' Write test cases for solution1 '''

import pytest as pytest
from solution2 import doWork

@pytest.fixture #can pass as arguments to test cases
def dataInt():
    ''' provide int obj '''
    return 6

def test_allsuccess(dataInt): #testfunc name should be started with test
    ''' run the case where everything is fine '''
    result = doWork(dataInt)
    assert result == {'retCode': 0, 'data': [['sit', 0, 'sit'], [0, 'sit', 0]]}

def test_dataerror(dataInt):
    ''' provide the data wrong '''
    dataInt = 5
    result = doWork(dataInt)
    assert result == {'retCode': 400, 'error': 'Data is not valid'}