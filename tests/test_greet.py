
from lib.greet import * 



def test_add_name_to_a_greeter():
  result = greet('Josh')
  assert result == 'Hello, Josh!'