try:
    2/0
except(ZeroDivisionError):
    raise ValueError from None

