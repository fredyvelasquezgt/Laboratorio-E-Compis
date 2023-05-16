from Parser import Parser

def test_parser01():
  # Arrange
	parser = Parser._from_file('yapar.txt')
	first_item = (parser.grammar.start,0,0) # First item to be used on the closure
	# Act
	closure = parser.closure({first_item})
	# Assert
	for item in closure:
		assert item in {("E'", 0, 0), ('T', 1, 0), ('F', 1, 0), ('E', 0, 0), ('E', 1, 0), ('T', 0, 0), ('F', 0, 0)}

def test_parser02():
	parser = Parser._from_file('yapar.txt')
	closure = {("E'",0,1), ("E", 0, 1)}
	go_to = parser.go_to(closure, '+')
	for item in go_to:
		assert item in {('E', 0, 2), ('T', 1, 0), ('F', 1, 0), ('E', 1, 0), ('T', 0, 0), ('F', 0, 0)}
	
	
def test_parser03():
	parser = Parser._from_file('yapar.txt')
	items = parser.items()
	assert True == False