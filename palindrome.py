def is_palindrome(text) :
	""" Takes in a string and determines if palindrome. Returns true or false. """
	
	if len(text) == 1 :
		return True
		
	elif len(text) == 2 and text[0] == text[-1] :
		return True
		
	elif text[0] != text[-1] :
		return False
	
	elif text[0] == text[-1] :
		is_palindrome(text[1:-1])
		return True
