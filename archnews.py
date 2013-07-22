#https://www.archlinux.org/feeds/news/
#> this could have solved the problem of feed burner
import re,configuration
from urllib import FancyURLopener

def check_news():
	br = FancyURLopener()
	response = br.open("http://www.archlinux.org/news/").readlines()
	for a in response:
		if 'title="View: ' in a:
			news = re.findall('">([^<]+)</a>',a)[0]
			break

	oldnews = re.findall('NEWS:(.*)\n', open(
		configuration.DATA_FILE, 'r').read()
		)[0]
	if oldnews!=news:
		configuration.backup()
		open(configuration.DATA_FILE,"w").write(
			open(configuration.DATA_FILE+".bak", "r").read().replace(
				"NEWS:"+oldnews, "NEWS:"+news)
				)
