# To Do List Function Design Recipe

## 1. Describe the Problem

```
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.
```

## 2. Design the Function Signature

```python

def includes_to_do(line):
    """Extracts #TODO from line

    Parameters: (list all parameters and their types)
        line: string

    Returns: (state the return value and its type)
        boolean

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
```

## 3. Create Examples as Tests

```python

"""
When we pass in #TODO anywhere in the string
It should return True
"""

def test_pass_in_to_do():
    assert includes_to_do('#TODO buy milk') == True

"""
When we do not pass in #TODO anywhere in the string
It should return False
"""

def test_not_pass_in_to_do():
    assert includes_to_do('drink tea') == False

```

## 4. Implement the Behaviour

