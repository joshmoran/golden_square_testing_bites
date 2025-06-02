import pytest
from lib.password_checker import * 

def test_check_length_of_a_password_less_than_eight_characaters():
  my_pass = PasswordChecker()
  with pytest.raises(Exception) as e:
    my_pass.check( 'mypass')
  error_message = str(e.value)
  assert error_message == "Invalid password, must be 8+ characters."

def test_checking_a_password_more_than_eight_characters():
  my_pass = PasswordChecker()
  result = my_pass.check('mypassword')
  assert result == True 

def test_adding_an_integer_to_password_checker():
  my_pass = PasswordChecker()
  with pytest.raises(TypeError) as e:
    my_pass.check( 0000000 )
  error_message = str(e.value )
  assert error_message == "object of type 'int' has no len()"run