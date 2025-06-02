from lib.gratitudes import * 

def test_single_formatted_return_of_gratitudes():
  gratitude = Gratitudes()
  gratitude.add('my cats')
  result = gratitude.format()
  assert result == "Be grateful for: my cats"

def test_multiple_formatted_return_of_gratitudes():
  gratitude = Gratitudes()
  gratitude.add('my cats')
  gratitude.add('my partner')
  result = gratitude.format()
  assert result == "Be grateful for: my cats, my partner"

  