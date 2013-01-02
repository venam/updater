# coding: utf-8
import mechanize
import re
import subprocess

COUNTRY_CODE = "LEXX003"

def printIcon(cond,timing):
    if timing>19 or timing<6:
        if cond == 'Partly Cloudy' or cond == 'Mostly Cloudy' or 'N/A':
            return 'l'
        elif cond == 'Fair' or cond == 'Clear' or cond=='Sunny':
            return 'N'
        elif cond == 'Cloudy' or cond == 'Fog':
            return 'n'
        elif  'Storms' or 'Thunder' in cond:
            return 's'
        elif cond == 'Snow':
            return 't'
        elif cond == 'Rain' or cond == 'Light Rain':
            return 'r'
        elif cond == 'Shower':
            return 'q'
        else:
            return 'N'
    else:
        if cond == 'Partly Cloudy' or cond == 'Mostly Sunny' or cond=='Mostly Cloudy' or 'N/A':
            return 'b'
        elif cond == 'Fair' or cond == 'Sunny' or cond=='Clear':
            return 'D'
        elif cond == 'Cloudy' or cond == 'Fog':
            return 'd'
        elif  'Storms' or 'Thunder' in cond:
            return 'i'
        elif cond == 'Snow':
            return 'j'
        elif cond == 'Rain' or cond == 'Light Rain':
            return 'h'
        elif cond == 'Shower':
            return 'g'


def check_weather(LOCATION):
    timing=subprocess.check_output(["date"])
    timing=int(re.findall(" ([0-9]{2}|[0-9]{1}):",timing)[0])
    br=mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_handle_gzip(True)
    br.addheaders = [('User-agent','Mozilla/5.0 (Windows; Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1')]
    br.open("http://www.weather.com/weather/tenday/"+COUNTRY_CODE, timeout=5)
    open(LOCATION + "temperature.txt",'w').write(br.response().read())
    weather      = re.findall('itemprop=\"weather-phrase\">(.*)</span>', open(LOCATION+"temperature.txt").read())[0]
    someweather  = re.findall('WEATHER:(.*)\n', open(LOCATION + "config", 'r').read())[0]

    myIcon       = printIcon(weather,timing)
    myIconInFile = re.findall('WEATHERICON:(.*)\n', open(LOCATION + "config", 'r').read())[0]
    if myIcon   != myIconInFile or weather != someweather :
        open(LOCATION + "config.bak","w").write(open(LOCATION+"config", "r").read())
        open(LOCATION + "config","w").write(open(LOCATION + "config.bak", "r").read().replace("WEATHERICON:"+myIconInFile, "WEATHERICON:"+myIcon).replace("WEATHER:"+someweather, "WEATHER:"+weather))


def check_temp(LOCATION):
    tempe = re.findall('itemprop=\"temperature-fahrenheit\">(.*)</span>',open(LOCATION + "temperature.txt").read())[0]
    tempe=str(int((int(tempe)-32)*(float(5)/9)))
    myfile = open(LOCATION + "config", 'r').read()
    tempeNOW = re.findall('TEMP:(.*)°C', myfile)[0]
    if tempe!=tempeNOW:
        open(LOCATION + "config.bak","w").write(open(LOCATION + "config", "r").read())
        open(LOCATION + "config","w").write(open(LOCATION+"config.bak", "r").read().replace("TEMP:"+tempeNOW+"°C", "TEMP:"+tempe+"°C"))


#re.findall(,br.response().read())
def check_tomorrow_weather(LOCATION):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_handle_gzip(True)
    br.addheaders = [('User-agent','Mozilla/5.0 (Windows; Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1')]
    br.open("http://www.weather.com/weather/tomorrow/"+COUNTRY_CODE, timeout=10)
    open(LOCATION + "tomorrow.txt",'w').write(br.response().read())
    weather = re.findall("([A-Za-z]*)\" class=\"wx-weather-icon",open(LOCATION+"tomorrow.txt" ).read())[0]
    old_weather = re.findall('TOMORROW:(.*)\n', open(LOCATION+"config", 'r').read())[0]
    if weather != old_weather :
        open(LOCATION+"config.bak","w").write(open(LOCATION+"config", "r").read())
        open(LOCATION+"config","w").write(open(LOCATION+"config.bak", "r").read().replace("TOMORROW:"+old_weather, "TOMORROW:"+weather))

def check_tom_celsius(LOCATION):
    tempe    = re.findall(" ([0-9]*)<sup>&deg",open(LOCATION+"tomorrow.txt").read())[0]
    tempe    = str(int((int(tempe)-32)*(float(5)/9)))
    myfile   = open(LOCATION+"config", 'r').read()
    tempeNOW = re.findall('TOM_TEMP:(.*)°C', myfile)[0]
    if tempe!=tempeNOW:
        open(LOCATION+"config.bak","w").write(open(LOCATION+"config", "r").read())
        open(LOCATION+"config","w").write(open(LOCATION+"config.bak", "r").read().replace("TOM_TEMP:"+tempeNOW+"°C", "TOM_TEMP:"+tempe+"°C"))



#END
