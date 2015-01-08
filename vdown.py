import urllib

def download(url, name, num):
     try:
          img = urllib.urlopen(url)
          fhand = open(name, 'w')
          size = 0
          while True:
             info = img.read(100000)
             if len(info) < 1 : break
             size = size + len(info)
             fhand.write(info)
          
          print size,'Downloaded.'
          fhand.close()
     except:
          print "Error in downloading", name

print '\t\t\t V Down \t\t\t\n'
downlist = dict()
fn = raw_input("Enter file name: ")
try:
     myfile = open(fn);
     for line in myfile:
          if not line.startswith("Download: "): continue
          line.strip();
          x = line.split(': ')
          try:
               name = x[2]
               url = x[1]
          except:
               print "This line is corrupt (skiping line)-\n",line
               continue
          print "\nName:",name,"URL:",url
          downlist[name] = url
except:
     print "Error - This file does not exist"

count = 1
for name, url in sorted(downlist.items()):
     print "\nNumber:",count,"Name:",name,"URL:",url
     print "Downloading...."
     download(url, name, count)
     count = count + 1
