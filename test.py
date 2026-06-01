"""Trivial, intentionally useless code for testing commits."""

def do_nothing(value=None):
	"""Return the input unchanged."""
	return value


class UselessCounter:
	"""Counts things without doing anything useful."""

	def __init__(self):
		self._count = 0

	def increment(self):
		self._count += 1
		return self._count


def main():
	counter = UselessCounter()
	for _ in range(3):
		counter.increment()

	do_nothing("nothing to see here")


if __name__ == "__main__":
	main()
