import subprocess

def batt_perc():
	outputcommand = subprocess.check_output(["acpi","-b"])
	outputcommand = outputcommand.split(",")[1]
	outputcommand = outputcommand.replace("%","")
	outputcommand = int(outputcommand)
	return outputcommand
