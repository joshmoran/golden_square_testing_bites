import pytest
from lib.present import * 

def test_wrapping_an_empty_present():
  gift = Present()
  result = gift.wrap('')
  assert result == None

def test_wrapping_a_present():
  gift = Present()
  result = gift.wrap('toy soldier')
  assert result == None

def test_wrapping_an_integer():
  gift = Present()
  result = gift.wrap(1000)
  assert result == None 

def test_wrapping_a_none_present():
  gift = Present()
  result = gift.wrap( None )
  assert result == None

def test_unwrapping_a_set_present():
  gift = Present() 
  gift.wrap('barbie')
  result = gift.unwrap()
  assert result == 'barbie' 

def test_already_wrapped_present():
  gift = Present()
  gift.wrap('toy soldier')
  with pytest.raises(Exception) as e:
    gift.wrap('toy soldier')
  error_message = str(e.value)
  assert error_message == 'A contents has already been wrapped.'

def test_unwrapping_an_empty_present():
  gift = Present()
  gift.wrap(None)
  with pytest.raises(Exception) as e:
    result = gift.unwrap()
  result = str(e.value)
  assert result == 'A contents has already been wrapped.'

def test_unwrpping_a_present_that_is_not_wrapped():
  gift = Present()
  with pytest.raises(Exception) as e:
    gift.unwrap()
  result = str(e.value)
  assert result == 'A contents has already been wrapped.'