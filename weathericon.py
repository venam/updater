# coding: utf-8
import re
import subprocess
from urllib import URLopener
import configuration

class weather_checker(object):
    def check_weather(self,br):
        response = br.open("http://www.weather.com/weather/tenday/"+configuration.COUNTRY_CODE).readlines()
        weather = ""
        for a in response:
            if 'itemprop=\"weather-phrase\">' in a :
                weather      = re.findall('itemprop=\"weather-phrase\">([^<]+)</span>', a)[0]
                break
        #the old weather in the file
        someweather  = re.findall('WEATHER:(\w+ ?\w+)\n', open(configuration.DATA_FILE, 'r').read())[0]
        if weather != someweather :
            configuration.backup()
            #update the data
            open(configuration.DATA_FILE,"w").write(
                open(configuration.DATA_FILE + ".bak", "r").read().replace(
                    "WEATHER:"+someweather, "WEATHER:"+weather
                    )
                )
        return response

    def check_temp(self,response):
        #get the temperature
        for a in response:
            if "temperature-fahrenheit" in a:
                tempe = re.findall('itemprop=\"temperature-fahrenheit\">(\d*)</span>',a)[0]
                break
        #convert it to celcius
        tempe=str(int((int(tempe)-32)*(float(5)/9)))
        myfile   = open(configuration.DATA_FILE, 'r').read()
        tempeNOW = re.findall('TEMP:(\d*)°C', myfile)[0]
        if tempe!=tempeNOW:
            configuration.backup()
            #replace the temp
            open(configuration.DATA_FILE,"w").write(
                open(configuration.DATA_FILE+".bak", "r").read().replace(
                    "TEMP:"+tempeNOW+"°C", "TEMP:"+tempe+"°C")
                    )

    def check_tomorrow_weather(self,br):
        response = br.open("http://www.weather.com/weather/tomorrow/"+configuration.COUNTRY_CODE).readlines()
        for a in response:
            if '<p class="wx-phrase' in a:
                weather = re.findall('">([^<]+)</',a)[0]
                break
        old_weather = re.findall('TOMORROW:(.*)\n', open(
            configuration.DATA_FILE, 'r').read()
            )[0]
        if weather != old_weather :
            configuration.backup()
            open(configuration.DATA_FILE,"w").write(
                open(configuration.DATA_FILE+".bak", "r").read().replace(
                    "TOMORROW:"+old_weather, "TOMORROW:"+weather
                    )
                )
        return response

    def check_tom_celsius(self,response):
        for a in response:
            if '<p class="wx-temp">' in a:
                tempe    = re.findall(" ([0-9]+)<sup>&deg",a)[0]
                break
        tempe    = str(int((int(tempe)-32)*(float(5)/9)))
        myfile   = open(configuration.DATA_FILE, 'r').read()
        tempeNOW = re.findall('TOM_TEMP:(.+)°C', myfile)[0]
        if tempe!=tempeNOW:
            configuration.backup()
            open(configuration.DATA_FILE,"w").write(
                open(configuration.DATA_FILE+".bak", "r").read().replace(
                    "TOM_TEMP:"+tempeNOW+"°C", "TOM_TEMP:"+tempe+"°C"
                    )
                )

    def procedure(self):
        br = URLopener()
        response = self.check_weather(br)
        self.check_temp(response)
        response = self.check_tomorrow_weather(br)
        self.check_tom_celsius(response)
#END
