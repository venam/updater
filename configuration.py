#configuration file

DATA_FILE                   = "/home/raptor/.my_updater/data"
STARTER_SCRIPT              = "/usr/bin/updater"
WHOLE_LINE                  = True          #display the whole line colored
SCRIPT_NAME                 = "/updater.py" #for the killer grep
WEBSITE_TO_CHECK_CONNECTION = "http://venam.dotgeek.org"
KEYWORD	                    = "empty"
COUNTRY_CODE                = "LEXX0003"
BAT_PERC_WARNING            = 50            #warning if batt perc under this value
BAT_WARN_COMMAND            = "beep -l 10  100" #command to exec at warning bat
#run the following commang when a manga is out, will replace MANGA with the manga name
MANGA_NEW_CMD               = "urxvt -e sh -c 'figlet -f smshadow -t MANGA;sleep 4000;'"
MANGA_LIST                  = [
	"fairy-tail",
	"bleach",
	"beelzebub",
	"hunter-x-hunter",
	"shingeki-no-kyojin",
	"vagabond",
	"deadman-wonderland",
	"judge",
	"berserk",
	"dgray-man",
	"claymore",
	"one-piece",
	"naruto",
	"pastel",
	"i-am-a-hero",
	"to-love-ru",
	"kissxsis",
	"the-world-god-only-knows",
	"assassination-classroom",
	"watashi-ni-xx-shinasai"
	]
IMAP_DOMAIN                = "unixhub.net"
IMAP_USER                  = "patrick at unixhub.net"
IMAP_PASSWD                = "password"

def backup():
	open(DATA_FILE+".bak",'w').write(
		open(DATA_FILE, "r").read()
		)
