from lib.report_length import * 


def test_check_4_lengthed_word():
  result = report_length('road')
  assert result == "This string was 4 characters long."

def test_check_5_lengthed_word():
  result = report_length('house')
  assert result == "This string was 5 characters long."

def test_check_6_lengthed_word():
  result = report_length('length')
  assert result == "This string was 6 characters long."

def test_check_9_lengthed_word():
  result = report_length('pentagram')
  assert result == "This string was 9 characters long."


