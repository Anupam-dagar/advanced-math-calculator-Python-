import urllib
import json

#Function to do API call
def api_call(operation, expression):
	connect = urllib.urlopen("https://newton.now.sh/%s/%s"%(operation,expression))
	output_string = connect.read()
	output_json = json.loads(output_string)
	if "error" not in output_json:
		print output_json['result']
	else:
		print output_json['error'] + "\n" + "Please check for errors in operation or expression."
	connect.close()

#main code
print "Welcome to advanced mathematical calculator"
print "-------------------------------------------\n"
operation_choices = ['simplify', 'factor', 'derive', 'integrate', 'zeroes', 'tangent', 'area', 'cos', 'sin', 'tan', 'arccos', 'arcsin', 'arctan', 'abs', 'log']
print "Operations which can be performed are:\n"
while True:
	for choices in operation_choices:
		print choices
		no_of_char = len(choices)
		print "-" * no_of_char
	operation = raw_input("Input the operation to be performed:")
	expression = raw_input("Input the expression:")
	api_call(operation, expression)
	exit_input = raw_input("Solve another expression? Enter y to continue or n to exit\n")
	exit_input.lower()
	if exit_input == "n":
		break