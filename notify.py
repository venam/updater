# coding : utf-8
import os,re
import configuration

def check_pkg():
	oldnum=re.findall('PKGS:(.*)\n', open(
		configuration.DATA_FILE, 'r').read()
		)[0]
	try:
		p = os.popen("pacman -Qu |wc -l")
		p = p.read()
		p = p.rstrip()

		if ':'+p+' New pkg' not in oldnum :
			if p!= '0':
				configuration.backup()
				open(configuration.DATA_FILE,"w").write(
					open(configuration.DATA_FILE+".bak", "r").read().replace(
						"PKGS:"+oldnum, "PKGS:"+p+" New Pkg"
						)
					)
			else:
				configuration.backup()
				open(configuration.DATA_FILE,"w").write(
					open(configuration.DATA_FILE+".bak", "r").read().replace(
						"PKGS:"+oldnum, "PKGS:"+"Up-To-Date")
						)
	except Exception,e:
		print e
