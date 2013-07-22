# coding: utf-8
import mechanize
import re
import subprocess
import configuration

class weather_checker(object):
    def create_browser(self):
        br=mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_handle_gzip(True)
        br.addheaders = [('User-agent','Mozilla/5.0 (Windows; Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1')]
        return br

    def check_weather(self,br):
        br.open("http://www.weather.com/weather/tenday/"+configuration.COUNTRY_CODE, timeout=10)
        weather = ""
        for a in br.response().readlines():
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
        return br

    def check_temp(self,br):
        #get the temperature
        for a in br.response().readlines():
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
        return br

    def check_tomorrow_weather(self,br):
        br.open("http://www.weather.com/weather/tomorrow/"+configuration.COUNTRY_CODE, timeout=10)
        for a in br.response().readlines():
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
        return br

    def check_tom_celsius(self,br):
        for a in br.response().readlines():
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
        return br


    def procedure(self):
        br = self.create_browser()
        br = self.check_weather(br)
        br = self.check_temp(br)
        br = self.check_tomorrow_weather(br)
        br = self.check_tom_celsius(br)

#END
