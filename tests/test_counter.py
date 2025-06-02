from lib.counter import * 

def test_counter():
  count = Counter()
  count.add(2)
  result = count.report ()
  assert result == "Counted to 2 so far."