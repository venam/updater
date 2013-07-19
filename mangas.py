import mechanize
import re
import subprocess
from time import sleep
import configuration

class check_the_mangas():
	def __init__(self,manga_name):
		self.manga_name	     = manga_name
		self.myfile		     = open(configuration.DATA_FILE,'r').read()
		self.manga_oldnumber = self.get_number()
		self.manga_nownumber = self.manga_oldnumber
		self.manga_olddate   = self.get_date  ()
		self.nowdate		 = self.today_date()
		self.br			     = mechanize.Browser()

	def get_number(self):
		return re.findall(self.manga_name+':([0-9]+):',self.myfile)[0]

	def get_date(self):
		return re.findall(self.manga_name+":"+str(self.manga_oldnumber)+':(.*)\n',self.myfile)[0]

	def today_date(self):
		return subprocess.check_output(["date","+%a-%b-%e"]).replace("\n","")

	#return 1 if the connection is working
	def test_connection(self):
		try:
			self.br = mechanize.Browser()
			self.br.set_handle_robots(False)
			self.br.open(configuration.WEBSITE_TO_CHECK_CONNECTION, timeout=4)
			if configuration.KEYWORD in self.br.response().read():
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
						if self.manga_name + ":" + str(self.manga_nownumber) not in open(configuration.DATA_FILE, "r").read():
							os.system(configuration.MANGA_NEW_CMD.replace("MANGA",self.manga_name))
							configuration.backup()
							open(configuration.DATA_FILE,'w').write(open(configuration.DATA_FILE+".bak", "r").read().replace(self.manga_name+":"+str(self.manga_oldnumber)+":"+ self.manga_olddate, self.manga_name+":"+str(self.manga_nownumber)+":"+self.nowdate))
					else:
						self.manga_nownumber = str( int(self.manga_nownumber)+1 )
			except :
				if "is not released yet. If you liked" in self.br.response().read():
					if self.manga_name + ":" + str(self.manga_nownumber) not in open(configuration.DATA_FILE, "r").read():
						configuration.backup()
						open(configuration.DATA_FILE,'w').write(open(configuration.DATA_FILE+".bak", "r").read().replace(self.manga_name+":"+str(self.manga_oldnumber)+":"+ self.manga_olddate, self.manga_name+":"+str(self.manga_nownumber)+":"+self.nowdate))
				pass

def connection():
	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.open(configuration.WEBSITE_TO_CHECK_CONNECTION, timeout=4)
		if configuration.KEYWORD in br.response().read():
			return 1
		else:
			return 0
	except:
		return 0

