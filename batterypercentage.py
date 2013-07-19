import subprocess,configuration,os

def batt_perc():
	outputcommand = subprocess.check_output(["acpi","-b"])
	outputcommand = outputcommand.split(",")[1]
	outputcommand = outputcommand.replace("%","")
	outputcommand = int(outputcommand)
	if ( outputcommand < configuration.BAT_PERC_WARNING ):
		os.system(configuration.BAT_WARN_COMMAND)
