import pytest
from lib.present import * 

def test_wrapping_an_empty_present():
  gift = Present()
  result = gift.wrap('')
  assert result == None

def test_wrapping_a_present():
  gift = Present()
  with pytest.raises(Exception) as e: 
    gift.wrap('toy soldier')
  error_message = str(e.value)
  assert error_message == 'A contents has already been wrapped.'



# def test_unwrapping_an_empty_present():


# def test_unwrapping_a_present():