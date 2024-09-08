def main():
	# Prompt the user for a greeting
	greeting = input("Greeting: ")
	# Call the value function and print the result
	result = value(greeting)
	print(f"${result}")

def value(greeting):
# Convert the greeting to lowercase for case-insensitive comparison
	greeting = greeting.lower().strip()
	if 'hello' in greeting:
		return	0
	# Check if the greeting starts with "h" but not "hello"
	elif 'h' == greeting[0]:
		return	20
	else:
		return	100

if __name__ == "__main__":
	main()
