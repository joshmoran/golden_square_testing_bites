from lib.check_codeword import *

def test_if_checking_codeword_works():
  result = check_codeword('horse')
  assert result == 'Correct! Come in.'

def test_if_word_starts_with_e_and_ends_with_e():
  result = check_codeword('hedge')
  assert result == 'Close, but nope.'

def test_any_other_word():
  result = check_codeword('anything else')
  assert result == 'WRONG!'