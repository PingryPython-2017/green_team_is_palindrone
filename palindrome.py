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


# Main Program:

message = input("Give me a message: ")

if is_palindrome(message) == True:
	print('"{}" is a palindrome.'.format(message))
elif is_palindrome(message) == False:
	print('"{}" is not a palindrome.'.format(message))