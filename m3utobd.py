import re
fin = open("channels2.m3u")
from blog.models import Channel

#fout = open("channels1.m3u", "wt")
flag=0
l=[]
l1=[]
for line in fin:

	if(line.startswith("#EXTINF:-1") and flag==0):
		l1=re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', line)
		flag=1

	if(line.startswith("http://smumcdnems01.cdnsrv.jio.com/") and flag==1):
    		l1.append('tvg-link='+line.replace('\n',''))
    		flag=0
    		l.append(l1)
    		l1=[]
#print l

for channel in l:

	l1=[]

	for tag in channel:
		
		#print type(tag)
		if(tag.startswith('tvg-name')):
			tag=tag.split("=")
			l1.append(tag[1].replace('"', ''))

		elif(tag.startswith('group-title')):
			tag=tag.split("=")
			l1.append(tag[1].replace('"', ''))

		elif(tag.startswith('tvg-link')):
			tag=tag.split("=")
			l1.append(tag[1].replace('"', ''))
	Channel(name=l1[0],group=l1[1],url=l1[2]).save()
	#b.save()





    #fout.write( line.replace('foo', 'bar') )

   