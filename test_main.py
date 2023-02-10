from main import *

def test_simple_work():
	""" done. """
#	assert simple_work_calc(10, 2, 2) == #TODO
#	assert simple_work_calc(20, 3, 2) == #TODO
#assert simple_work_calc(30, 4, 2) == #TODO
  assert simple_work_calc(10, 2, 2) == 15
	assert simple_work_calc(20, 3, 2) == 113
	assert simple_work_calc(30, 4, 2) == 429
	assert simple_work_calc(100, 3, 2) == 6100
	assert simple_work_calc(250, 2, 3) == 21501
	assert simple_work_calc(500, 4, 5) == 107151

def test_work():
	#assert work_calc(10, 2, 2,lambda n: 1) == #TODO
	#assert work_calc(20, 1, 2, lambda n: n*n) == #TODO
	#assert work_calc(30, 3, 2, lambda n: n) == #TODO
  assert work_calc(10, 2, 2, lambda n: 1) == 21
  assert work_calc(20, 1, 2, lambda n: n*n) == 181
  assert work_calc(30, 3, 2, lambda n: n) == 465
  assert work_calc(40, 4, 2, lambda n: n/2) == 172
  assert work_calc(50, 5, 2, lambda n: n/3) == 198
  assert work_calc(60, 6, 2, lambda n: n/4) == 220