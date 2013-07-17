#!/usr/bin/python2
"""
COPYRIGHT AND PERMISSION NOTICE

Copyright (c) 2013, Patrick Louis <patrick at unixhub.net>

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    1.  The author is informed of the use of his/her code. The author does not have to consent to the use; however he/she must be informed.
    2.  If the author wishes to know when his/her code is being used, it the duty of the author to provide a current email address at the top of his/her code, above or included in the copyright statement.
    3.  The author can opt out of being contacted, by not providing a form of contact in the copyright statement.
    4.  If any portion of the author’s code is used, credit must be given.
            a. For example, if the author’s code is being modified and/or redistributed in the form of a closed-source binary program, then the end user must still be made somehow aware that the author’s work has contributed to that program.
            b. If the code is being modified and/or redistributed in the form of code to be compiled, then the author’s name in the copyright statement is sufficient.
    5.  The following copyright statement must be included at the beginning of the code, regardless of binary form or source code form.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Except as contained in this notice, the name of a copyright holder shall not
be used in advertising or otherwise to promote the sale, use or other dealings
in this Software without prior written authorization of the copyright holder.

"""

#modules
import mangas
import imaploginunix
import weathericon
import archnews
import notify
import base64
import batterypercentage
import os

LOCATION = "/home/raptor/.my_updater/"

if ( batterypercentage.batt_perc()<40 ):
    print "WARNING battery!"
    os.system("beep -l 10  100")

if( mangas.connection() ):

    try:
        ##
        notify.check_pkg(LOCATION)
        ##
    except Exception,the_error:
        print the_error

    try:
        ##
        archnews.check_news(LOCATION)
        ##
    except Exception,the_error:
        print the_error

    try:
        ##
        weathericon.weather_checker(LOCATION,"LEXX0003").procedure()
        ##
    except Exception,the_error:
        print the_error

    try:
        ##
        mangas.check_the_mangas("fairy-tail",LOCATION).run()
        mangas.check_the_mangas("bleach",LOCATION).run()
        mangas.check_the_mangas("beelzebub",LOCATION).run()
        mangas.check_the_mangas("hunter-x-hunter",LOCATION).run()
        mangas.check_the_mangas("shingeki-no-kyojin",LOCATION).run()
        mangas.check_the_mangas("vagabond",LOCATION).run()
        mangas.check_the_mangas("deadman-wonderland",LOCATION).run()
        mangas.check_the_mangas("judge",LOCATION).run()
        mangas.check_the_mangas("berserk",LOCATION).run()
        mangas.check_the_mangas("dgray-man",LOCATION).run()
        mangas.check_the_mangas("claymore",LOCATION).run()
        mangas.check_the_mangas("one-piece",LOCATION).run()
        mangas.check_the_mangas("naruto",LOCATION).run()
        mangas.check_the_mangas("pastel",LOCATION).run()
        mangas.check_the_mangas("i-am-a-hero",LOCATION).run()
        mangas.check_the_mangas("to-love-ru",LOCATION).run()
        mangas.check_the_mangas("kissxsis",LOCATION).run()
        mangas.check_the_mangas("the-world-god-only-knows",LOCATION).run()
        mangas.check_the_mangas("assassination-classroom",LOCATION).run()
        mangas.check_the_mangas("watashi-ni-xx-shinasai",LOCATION).run()
        ##
    except Exception,the_error:
        print the_error

    try:
        ##
        imaploginunix.check_the_email(LOCATION,"unixhub.net","patrick at unixhub.net","password")
        ###
    except Exception,the_error:
        print the_error
