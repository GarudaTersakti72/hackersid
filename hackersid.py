import requests, sys
# Mirror Submiter Mass hackersid.com
# GARUDA TERSAKTI 72 
GN='\033[0;32m' # ijo
LGN='\033[1;32m' # ijo terang
DT='\033[0m' # Default
print "\r%sGARUDA TERSAKTI 72%s" % (LGN, DT)
print "\r"
hacker = raw_input("nick : "+GN)
team = raw_input(DT+"team : "+GN)
urls = raw_input(DT+"file : ").strip()
try:
   open(urls)
except IOError:
    print "gaada urls.txt"
    exit()
else:
    try:
       a = open(urls,'r').readlines()
       for kntl in a:
         babi = kntl.rstrip().strip().lower()
         data = {'notifier':hacker, 'team':team, 'domain':babi, 'poc':'Other Web Application bug', 'reason':'Heh...just for fun!','submit':'submit'}
         req = requests.post("http://hackersid.com/single", data=data).text
         if 'success' in req:
           print "%s   %s< sukses%s  " % (babi,LGN, DT)
         else:
           print "\rgagal di : ", babi           
    except KeyboardInterrupt:
        exit()