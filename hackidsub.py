import requests,threading,random,time
from urlparse import urlparse
GN='\033[1;32m'
R='\033[1;31m'
DT='\033[0m'

list_agents = ['Opera/9.12 (X11; Linux i686; U; en) (Ubuntu)',
               'Opera/9.25 (Macintosh; Intel Mac OS X; U; en)',
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; ja) Opera 11.00',
               'Mozilla/5.0 (Windows NT 5.0; U; de) Opera 8.50',
               'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
               'Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100']               

def sukses(dom):
    print "{}[+] sukses :> {}{}".format(GN,dom,DT)               

class main:
    def __init__(self,hacker,team,jmbt):
        self.hacker = hacker
        self.jmbt = jmbt 
        self.team = team 
        self.perulangan(hacker,team,jmbt)
    def perulangan(self,hacker,team,jmbt):
        try:
           print "babi"
           list_t = [] 
           for urls in open(jmbt,'r').readlines():
             urls = urls.rstrip()

             rand_head = random.choice(list_agents)
             if "://" in urls:
               urls = urls.replace("http://","").replace("https://","")
             else:
               urls = urls
             t = threading.Thread(target=self.auto_submit,args=(hacker,team,urls))
             list_t.append(t)
           for t in list_t:
             t.start()
        except IOError:
             exit()

    def auto_submit(self,hacker,team,urls):
        try:
             my_url = "https://hackersid.com/api/mirrorNew?hacker="+hacker+"&team="+team+"&url="+urls+"&poc=Not%20available&reason=Not%20available"
             sontol = requests.get(my_url,headers={'User-Agent':random.choice(list_agents)}).text 
             if "Success" in sontol:
               sukses(urls)
             else:
               print "fuck it :< ", urls 
               print my_url
               print sontol
        except IOError:
            print "[->] error open list of urls!"
        except requests.exceptions.RequestException:
            print "[-] exceptions > ", urls                  

heker = raw_input("hacker > ").replace(" ","%20")
if len(heker) == 0:
  heker = "DarkOct02"
tim = raw_input("tim > ").replace(" ","%20")
if len(tim) == 0:
  tim = "GARUDA TERSAKTI 72"
zz = raw_input("urls > ") 
main = main(heker.replace(" ","%20"),tim.replace(" ","%20"),zz)     