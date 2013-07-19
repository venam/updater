#!/usr/bin/python2
#
# updater front-end [version 0.1 alpha]
#
# This program will show a nice list of what is beeing
# updated with the module I did for the things I'm
# interested in.
#
# Copyright 2012 Patrick Louis <patrick@unixhub.net>
#
# Distributed under the terms of the GNU General Public License v3.
# See http://www.gnu.org/licenses/gpl.txt for the full license text.

#libraries
import time
import os
import sys
import re
import get_char2 as getchar
from   threading import Thread
import thread
import subprocess
import configuration

#configs
DATA_FILE            = configuration.DATA_FILE
STARTER_SCRIPT       = configuration.STARTER_SCRIPT
WHOLE_LINE           = configuration.WHOLE_LINE

#Text Foreground Colors
fg_black     = '\033[0;30m'
fg_red       = '\033[0;31m'
fg_green     = '\033[0;32m'
fg_brown     = '\033[0;33m'
fg_blue	     = '\033[0;34m'
fg_purple    = '\033[0;35m'
fg_cyan      = '\033[0;36m'
fg_lgray     = '\033[0;37m'
fg_dgray     = '\033[1;30m'
fg_lred	     = '\033[1;31m'
fg_lgreen    = '\033[1;32m'
fg_yellow    = '\033[1;33m'
fg_lblue     = '\033[1;34m'
fg_pink	     = '\033[1;35m'
fg_lcyan     = '\033[1;36m'
fg_white     = '\033[1;37m'
#Text Background Colors
bg_red       = '\033[0;41m'
bg_green     = '\033[0;42m'
bg_brown     = '\033[0;43m'
bg_blue	     = '\033[0;44m'
bg_purple    = '\033[0;45m'
bg_cyan	     = '\033[0;46m'
bg_gray      = '\033[0;47m'
#Attributes
at_normal    = '\033[0m'
at_bold      = '\033[1m'
at_italics   = '\033[3m'
at_underl    = '\033[4m'
at_blink     = '\033[5m'
at_outline   = '\033[6m'
at_reverse   = '\033[7m'
at_nondisp   = '\033[8m'
at_strike    = '\033[9m'
at_boldoff   = '\033[22m'
at_italicsoff= '\033[23m'
at_underloff = '\033[24m'
at_blinkoff  = '\033[25m'
at_reverseoff= '\033[27m'
at_strikeoff = '\033[29m'
#Colors to use [last one is the normal]
color	  = [fg_green+at_bold+at_underl ,
			  fg_cyan+at_bold+at_underl  ,
			  fg_blue+at_bold+at_underl  ,
			  fg_yellow+at_bold+at_underl,
			  at_normal+at_boldoff+at_strikeoff+at_blinkoff+at_underloff+at_italicsoff
			 ]
MAIN  = 0
HELP  = 1
DOWN  = 2
KILL  = 3
START = 4

class front_end():
	#-------init some global var-------#
	def __init__(self,config_file):
		self.config_file	= config_file
		self.old_config	 = open(config_file).read()
		self.date		   = ""
		self.clock		  = ""
		self.end_of_program = False
		self.menu		   = MAIN

	#-------nice string for time-------#
	def get_time(self):
		localtime  = time.localtime()
		year       = str(localtime.tm_year)
		month      = str(localtime.tm_mon)
		day	       = str(localtime.tm_mday)
		hour       = str(localtime.tm_hour)
		min	       = str(localtime.tm_min)
		sec	       = str(localtime.tm_sec)
		self.date  = year + '/' + month + '/' + day
		self.clock = hour + ':' + min   + ':' + sec

	def listen_for_input(self):
		while self.end_of_program ==False:
			#time.sleep(1)
			inkey = getchar.getch()
			#for i in xrange(sys.maxint):
			if inkey =='q' or inkey=='Q':
				#break
				self.end_of_program = True
				return
				#sys.exit(0)
				#self kill by sending SIGTERM signal
				#os.kill(int( os.getpid() ), 15)
			elif inkey == 'h' or inkey == 'H' :
				self.menu = HELP
			elif inkey == 'm' or inkey == 'M' :
				self.menu = MAIN
			elif inkey == 'k' or inkey == 'K' :
				self.menu = KILL
			elif inkey == 'd' or inkey == 'D' :
				self.menu = DOWN
			elif inkey == 's' or inkey == 'S' :
				self.menu = START

	def main_interface(self):
		color
		i = 0
		#takes the date
		today_is = subprocess.check_output(["date","+%a-%b-%e"]).replace("\n","")
		#clear the screen
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		# check the date
		#if open(self.config_file,'r').read() != self.old_config:
		#	self.old_config = open(self.config_file,'r').read()
		#	self.get_time()
		#print "	   "+ fg_lred +self.clock+"	"+  fg_lgray+"["+fg_pink+at_italics+self.date+fg_lgray+ at_italicsoff+"]"
		print at_bold+fg_pink +"__{  "+at_blink+fg_pink+"UPDATER"+at_bold+ at_blinkoff+fg_pink +"  }__"+at_normal
		for a in open(self.config_file,'r').readlines():
			if( i==len(color)-1 ):
				i = 0
			a = a.replace("\n","")
			#if there's 2 : then color what is after in green
			if len(re.findall("(:)",a))==2:
				a = a.replace(":",":"+fg_green,1)
				#the date is the 3 one
				the_date = a.split(":")[2]
				#if it's today then color it to pink
				if the_date == today_is:
					a = a.replace(the_date,fg_pink +the_date+color[len(color)-1])
			#change : to a cyan :
			a = a.replace(":", fg_lcyan+ ":" + color[len(color)-1])
			#if line start with # choose a color[i] from the palette
			if WHOLE_LINE:
				if a.startswith('#'):
					a = a.replace('#' , color[i]+"#")
					i+=1
				print a+color[len(color)-1]
			else:
				if a.startswith('#'):
					a = a.replace('#' , color[i]+"#"+color[len(color)-1])
					i+=1
				print a

	def help_interface(self):
		#clear the screen
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		print at_bold+fg_pink +"__{  "+at_blink+fg_pink+"HELP"+at_bold+ at_blinkoff+fg_pink +"  }__"+at_normal

	def killer_interface(self):
		print at_bold+fg_pink +"__{  "+at_blink+fg_pink+"KILLER"+at_bold+ at_blinkoff+fg_pink +"  }__"+at_normal


	#--------display what we want--------#
	def print_on_screen(self):
		while self.end_of_program == False:
			now_menu = self.menu
			if self.menu == MAIN :
				self.main_interface()
			elif self.menu ==HELP:
				self.help_interface()
			#check if the program needs to end or sleep
			for a in xrange(8):
				#directly quit the sleep if the menu is different
				if now_menu != self.menu:
					break
				if self.end_of_program == False:
					time.sleep(1)
				else:
					return

	def closing_program(self):
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		print "\n\nThe Program exited successfully\n\n"

	#-------main foo of the class-------#
	def run(self):
		self.get_time()
		t1 = Thread (target = self.listen_for_input)
		t2 = Thread (target = self.print_on_screen)
		t1.start()
		t2.start()
		t1.join()
		self.closing_program()


#------------RUN IT------------#
front_end(DATA_FILE).run()
#END!
