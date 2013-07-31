
from a import values

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:	
		return False

ivals = list(filter(is_int, values))
print(ivals)

