from lib.to_do import *

"""
When we pass in #TODO at the start of the string
It should return True
"""

def test_pass_in_to_do_at_start():
    assert includes_to_do('#TODO buy milk') == True

"""
When we do not pass in #TODO anywhere in the string
It should return False
"""

def test_not_pass_in_to_do():
    assert includes_to_do('drink tea') == False

"""
When we pass in an empty string
It should return False
"""

def test_empty_string():
    assert includes_to_do('') == False

"""
When we pass in #TODO anywhere in the string
It should return True
"""

def test_pass_in_to_do_anywhere():
    assert includes_to_do('buy milk #TODO') == True