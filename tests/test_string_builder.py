from lib.string_builder import *

def test_srting_builder_size_return():
  my_string = StringBuilder()
  my_string.add("string")
  result = my_string.size()
  assert result == 6

def test_srting_builder_output_return():
  my_string = StringBuilder()
  my_string.add("string")
  result = my_string.output()
  assert result == 'string'

