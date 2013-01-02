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
import get_char2 as getchar
from threading import Thread
import thread

#global vars
my_config_file          = "/home/raptor/.my_fave_conky/config"
end_of_program          = False

#Text Foreground Colors
fg_black                = '\033[0;30m'
fg_red                  = '\033[0;31m'
fg_green                = '\033[0;32m'
fg_brown                = '\033[0;33m'
fg_blue                 = '\033[0;34m'
fg_purple               = '\033[0;35m'
fg_cyan                 = '\033[0;36m'
fg_lgray                = '\033[0;37m'
fg_dgray                = '\033[1;30m'
fg_lred                 = '\033[1;31m'
fg_lgreen               = '\033[1;32m'
fg_yellow               = '\033[1;33m'
fg_lblue                = '\033[1;34m'
fg_pink                 = '\033[1;35m'
fg_lcyan                = '\033[1;36m'
fg_white                = '\033[1;37m'

#Text Background Colors
bg_red                  = '\033[0;41m'
bg_green                = '\033[0;42m'
bg_brown                = '\033[0;43m'
bg_blue                 = '\033[0;44m'
bg_purple               = '\033[0;45m'
bg_cyan                 = '\033[0;46m'
bg_gray                 = '\033[0;47m'

#Attributes
at_normal               = '\033[0m'
at_bold                 = '\033[1m'
at_italics              = '\033[3m'
at_underl               = '\033[4m'
at_blink                = '\033[5m'
at_outline              = '\033[6m'
at_reverse              = '\033[7m'
at_nondisp              = '\033[8m'
at_strike               = '\033[9m'
at_boldoff              = '\033[22m'
at_italicsoff           = '\033[23m'
at_underloff            = '\033[24m'
at_blinkoff             = '\033[25m'
at_reverseoff           = '\033[27m'
at_strikeoff            = '\033[29m'

#Colors to use [last one is the normal]
color      = [fg_green+at_bold+at_underl ,
              fg_cyan+at_bold+at_underl  ,
              fg_blue+at_bold+at_underl  ,
              fg_yellow+at_bold+at_underl,
              at_normal+at_boldoff+at_strikeoff+at_blinkoff+at_underloff+at_italicsoff
             ]
whole_line = True

class front_end():
    
    #-------init some global var-------#
    def __init__(self,config_file):
        self.config_file = config_file
        self.old_config  = open(config_file).read()
        self.date        = ""
        self.clock       = ""

    #-------nice string for time-------#
    def get_time(self):
        localtime  = time.localtime()
        year       = str(localtime.tm_year)
        month      = str(localtime.tm_mon)
        day        = str(localtime.tm_mday)
        hour       = str(localtime.tm_hour)
        min        = str(localtime.tm_min)
        sec        = str(localtime.tm_sec)

        self.date  = year + '/' + month + '/' + day
        self.clock = hour + ':' + min   + ':' + sec

    #--------'q' or 'Q' to exit---------#  
    def exit_program(self):
        global end_of_program
        k = ""
        inkey = getchar.getch()
        #for i in xrange(sys.maxint):
        k = inkey
        if k=='q' or k=='Q':
            #break
            end_of_program =True
            thread.exit()
        else:
            time.sleep(1)
            self.exit_program()

    #--------display what we want--------#
    def print_on_screen(self):
        global color
        i = 0
        while 1:
            if end_of_program == False:
                os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
                if open(self.config_file,'r').read() != self.old_config:
                    self.old_config = open(self.config_file,'r').read()
                    self.get_time()
                print "       "+ fg_lred +self.clock+"    "+  fg_lgray+"["+fg_pink+at_italics+self.date+fg_lgray+ at_italicsoff+"]"
                for a in open(self.config_file,'r').readlines():
                    if( i==len(color)-1 ):
                        i = 0
                    a = a.replace("\n","")
                    a = a.replace(":", fg_lcyan+ ":" + color[len(color)-1])
                    if a.startswith('#'):
                        if whole_line == False:
                            a = a.replace('#' , color[i]+"#"+color[len(color)-1])
                        else:
                            a = a.replace('#' , color[i]+"#")
                        i+=1
                    if whole_line:
                        print a+color[len(color)-1]
                    else:
                        print a
                time.sleep(4)
            else:
                break

    #-------main foo of the class-------#
    def run(self):
        self.get_time()
        Thread (target = self.exit_program).start()
        Thread (target = self.print_on_screen).start()
        #while end_of_program == False:
        #print "\n\nThe Program exited successfully\n\n"
        #thread.exit()


#------------RUN IT------------#
front_end(my_config_file).run()

#END!
