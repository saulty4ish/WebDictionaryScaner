import optparse
from module import SingleScan
from module import MultiScan
from module import common
def main():
	parser=optparse.OptionParser("-u <Target url> -r <Target list> --level <Bypass or not> -t <Thread number>\nExamples: Scan by multi threads : -u http://example.com/ --level=1\n          Scan by proxies : -u http://example.com/ --level=2\n          Scan by Delay : -u http://example.com/  --level=3\n          Multi Scan by proxies : -r dic.txt --level=2 \n ")
	parser.add_option("-u",dest='url',type="string",help="Please input the target url .")
	parser.add_option("--level",dest='level',type="string",help="Please choose which level to use .")
	parser.add_option("-r",dest='filename',type="string",help="Please input target urls .")
	parser.add_option("-t",dest='threadnum',type="int",help="Please input number of threads .")
	(options,args)=parser.parse_args()
	url=options.url
	level=options.level
	threadnum=options.threadnum	
	filename=options.filename
	if (url!=None)&(level=="1"):     #Default Scan with out bypass.
		Type=common.GetTypeOfScript(url)
		print "[+] The script of this web is "+Type+"."
		if(threadnum!=None):
			name=common.GenerateReport(url)
			Default=SingleScan.SingleScan(url,Type,threadnum,name)
			Default.OpenDir()
			Default.FindDir()
			Default.Work()
		else:
			name=common.GenerateReport(url)
			Default=SingleScan.SingleScan(url,Type,name)  # Default 3 threads
			Default.OpenDir()
			Default.FindDir()
			Default.Work()			
	elif (url!=None)&(level=="2"):     #Use proxies to scan	
		Type=common.GetTypeOfScript(url)
		print "[+] The script of this web is "+Type+"."
		name=common.GenerateReport(url)
		Default=SingleScan.SingleScan(url,Type,name)
		Default.filename=name
		Default.OpenDir()
		Default.GetProxy()	
		Default.WorkByProxy()
	elif (url!=None)&(level=="3"):     #Use timesleep to scan
		Type=common.GetTypeOfScript(url)
		print "[+] The script of this web is "+Type+"."
		name=common.GenerateReport(url)
		Default=SingleScan.SingleScan(url,Type,name)
		Default.filename=name
		Default.OpenDir()
		Default.Sleep()
	elif(filename!=None)&(level=="1"):
		MultiScan.MultiScan(filename,1)
	elif(filename!=None)&(level=="2"):
		MultiScan.MultiScan(filename,2)
	elif(filename!=None)&(level=="3"):	
		MultiScan.MultiScan(filename,3)
	else:
		print "\nWarning :  Wrong input.... "	
		print "\nTips: Add \"http or https\" in url. \n"
		print "Examples: Scan by multi threads : -u http://example.com/ --level=1\n"
		print "          Scan by proxies : -u http://example.com/ --level=2 \n "	
		print "          Scan by Delay : -u http://example.com/  --level=3 \n "	
		print "          Multi Scan by proxies : -r dic.txt --level=2 \n "
main()
