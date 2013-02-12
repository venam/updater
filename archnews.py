#https://www.archlinux.org/feeds/news/
#> this could have solved the problem of feed burner
import mechanize, re


def check_news(LOCATION):
    br=mechanize.Browser()
    br.set_handle_gzip(True)
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
    br.open("https://www.archlinux.org/news/", timeout=20)
    i=0
    for a in br.links():
        if i==20:
            news = a.text
        i+=1

    oldnews = re.findall('NEWS:(.*)\n', open(LOCATION+"config", 'r').read())[0]
    if oldnews!=news:
        open(LOCATION+"config.bak","w").write(open(LOCATION+"config", "r").read())
        open(LOCATION+"config","w").write(open(LOCATION+"config.bak", "r").read().replace("NEWS:"+oldnews, "NEWS:"+news))
