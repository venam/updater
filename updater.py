#!/usr/bin/python2
#
# updater [version 0.1 alpha]
#
# This program will start the modules
# Simply replace or add what you want
#
# Copyright 2012 Patrick Louis <patrick@unixhub.net>
#
# Distributed under the terms of the GNU General Public License v3.
# See http://www.gnu.org/licenses/gpl.txt for the full license text.


#modules
import mangas
import emailupdates
import weathericon
import archnews
import notify

LOCATION = "/folder/location/"

if( mangas.connection() ):

    ##
    mangas.check_the_mangas("hunter-x-hunter",LOCATION).run()
    ##

    ##
    emailupdates.check_the_mails("user@hotmail.com","password","display",LOCATION).run()
    ##

    ##
    weathericon.check_weather(LOCATION)
    weathericon.check_tomorrow_weather(LOCATION)
    weathericon.check_tom_celsius(LOCATION)
    weathericon.check_temp(LOCATION)
    ##

    ##
    archnews.check_news(LOCATION)
    ##

    ##
    notify.check_pkg(LOCATION)
    ##
