import mechanize
import re
import subprocess
from time import sleep

WEBSITE_TO_CHECK_CONNECTION = "http://venam.dotgeek.org"
KEYWORD					    = "empty"

class check_the_mangas():
	def __init__(self,manga_name,LOCATION):
		self.manga_name	  = manga_name
		self.myfile		  = open(LOCATION+"config",'r').read()
		self.manga_oldnumber = self.get_number()
		self.manga_nownumber = self.manga_oldnumber
		self.manga_olddate   = self.get_date  ()
		self.nowdate		 = self.today_date()
		self.br			  = mechanize.Browser()
		self.LOCATION		= LOCATION

	def get_number(self):
		return re.findall(self.manga_name+':([0-9]+):',self.myfile)[0]

	def get_date(self):
		return re.findall(self.manga_name+":"+str(self.manga_oldnumber)+':(.*)\n',self.myfile)[0]

	def today_date(self):
		return subprocess.check_output(["date","+%a-%b-%e"]).replace("\n","")

	#return 1 if the connection is working
	def test_connection(self):
		try:
			global WEBSITE_TO_CHECK_CONNECTION
			global KEYWORD
			self.br = mechanize.Browser()
			self.br.set_handle_robots(False)
			self.br.open(WEBSITE_TO_CHECK_CONNECTION, timeout=4)
			if KEYWORD in self.br.response().read():
				return 1
			else:
				return 0
		except:
			return 0

	def run(self):
		if( self.test_connection() ):
			last_chapter = False
			try:
				while(last_chapter==False):
					to_open = "http://www.mangareader.net/" + self.manga_name + "/" + str( int(self.manga_nownumber)+1 )
					self.br.open( to_open, timeout=4 )
					if "is not released yet. If you liked" in self.br.response().read():
						last_chapter = True
						if self.manga_name + ":" + str(self.manga_nownumber) not in open(self.LOCATION+"config", "r").read():
							#open (self.LOCATION+".todownload",'a').write(self.manga_name+":"+str(self.manga_nownumber)+"\n")
							open(self.LOCATION+"config.bak",'w').write(open(self.LOCATION+"config", "r").read())
							open(self.LOCATION+"config",'w').write(open(self.LOCATION+"config.bak", "r").read().replace(self.manga_name+":"+str(self.manga_oldnumber)+":"+ self.manga_olddate, self.manga_name+":"+str(self.manga_nownumber)+":"+self.nowdate))
					else:
						self.manga_nownumber = str( int(self.manga_nownumber)+1 )
			except :
				if "is not released yet. If you liked" in self.br.response().read():
					if self.manga_name + ":" + str(self.manga_nownumber) not in open(self.LOCATION+"config", "r").read():
						open(self.LOCATION+"config.bak",'w').write(open(self.LOCATION+"config", "r").read())
						open(self.LOCATION+"config",'w').write(open(self.LOCATION+"config.bak", "r").read().replace(self.manga_name+":"+str(self.manga_oldnumber)+":"+ self.manga_olddate, self.manga_name+":"+str(self.manga_nownumber)+":"+self.nowdate))
				pass

def connection():
	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.open("http://venam.dotgeek.org", timeout=4)
		if KEYWORD in br.response().read():
			return 1
		else:
			return 0
	except:
		return 0

