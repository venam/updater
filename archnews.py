#https://www.archlinux.org/feeds/news/
import mechanize, re

def create_browser():
    br=mechanize.Browser()
    br.set_handle_gzip(True)
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
    return br

def check_news(LOCATION):
    br = create_browser()
    br.open("http://www.archlinux.org/news/", timeout=10)
    for a in br.response().readlines():
        if 'title="View: ' in a:
            news = re.findall('">([^<]+)</a>',a)[0]
            break

    oldnews = re.findall('NEWS:(.*)\n', open(
        LOCATION+"config", 'r').read()
        )[0]
    if oldnews!=news:
        open(LOCATION+"config.bak","w").write(
            open(LOCATION+"config", "r").read()
            )
        open(LOCATION+"config","w").write(
            open(LOCATION+"config.bak", "r").read().replace(
                "NEWS:"+oldnews, "NEWS:"+news)
                )
