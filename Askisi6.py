import urllib
import re

print "Pliktrologise thn hmeromhnia ths klhrwshs!!!"
i=raw_input("Hmera: ")
m=raw_input("Mhnas: ")
y=raw_input("Xronos: ")
link="http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+i+"-"+m+"-"+y+".json"
dedomena = urllib.urlopen(link).read()

x=re.findall('\i+', dedomena)
z=157
for i in range(z):
	for j in range(0,7):
		k=i*20
		del x[k]

for i in range(80):
	syn=0
	arithmos=i+1
	for j in range(len(x)):
		if int(x[j])==num:
			syn += syn
	print num,": ",syn
