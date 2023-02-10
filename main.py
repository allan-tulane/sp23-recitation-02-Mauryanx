"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n
	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
  if n <= 1:
    return n
  else:
    return a * simple_work_calc(n/b, a, b) + n


def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == #TODO
	assert work_calc(20, 3, 2) == #TODO
	assert work_calc(30, 4, 2) == #TODO

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
    if n <= 1:
    return f(n)
  else:
    return a * work_calc(n/b, a, b,f) + f(n)
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
if n <= 1:
        return 0
    else:
        return max(span_calc(n/b, a, b, f), f(n)) + 1

def test_work():
	""" done. """
  assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 3, 2, lambda n: n*n) == 886
	assert work_calc(30, 4, 2, lambda n: n) == 465
	assert work_calc(100, 3, 2, lambda n: n*n*n) == 61100
	assert work_calc(250, 2, 3, lambda n: n*n) == 20001
	assert work_calc(500, 4, 5, lambda n: n) == 107151

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in input_sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
  # create work_fn1
  def work_fn1(n):
    return n**2

	# create work_fn2
  def work_fn2(n):
    return n**3

  res = compare_work(work_fn1, work_fn2)
	print(res)

def test_compare_span():
	# TODO

# Define the input values for n to be used in the comparison
    inputs = [10, 100, 1000]

    # Define the span functions to be compared
    span_fn1 = lambda n: n
    span_fn2 = lambda n: n ** 2

    # Call compare_span to compare the span functions
    res = compare_span(span_fn1, span_fn2, inputs)
    print(res)


def compare_span(span_fn1, span_fn2, n_values):
    """
    Compare the values of two span functions for different values of n

    Params:
    span_fn1.......The first span function to compare
    span_fn2.......The second span function to compare
    n_values.......A list of values of n to compare the span functions for
  
  Returns:
    A tuple containing two lists:
    The first list contains the values of the first span function for each value       of n
    The second list contains the values of the second span function for each value     of n
    """
  results1 = [span_fn1(n) for n in n_values]
  results2 = [span_fn2(n) for n in n_values]
  return (results1, results2)