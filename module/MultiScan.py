import SingleScan
import common
def MultiScan(filename,level):
	with open (filename,"r") as f:
		for line in f.readlines():
			url="http://"+line.strip()+"/"
			Type=common.GetTypeOfScript(url)
			print "[+] The script of this web is "+Type+"."
			if(level==1):
				name=common.GenerateReport(url)
				Default=SingleScan.SingleScan(url,Type,name)
				Default.OpenDir()
				Default.FindDir()
				Default.Work()
			elif(level==2):
				name=common.GenerateReport(url)
				Default=SingleScan.SingleScan(url,Type,name)
				Default.OpenDir()
				Default.GetProxy()
				Default.WorkByProxy()
			elif(level==3):
				name=common.GenerateReport(url)
				Default=SingleScan.SingleScan(url,Type,name)
				Default.OpenDir()
				Default.Sleep()
			else:
				print "\nWarning :  Wrong input.... "	
				print "\nTips: The max level is 3 . \n"
				print "Examples: Scan by multi threads : -u http://example.com/ --level=1\n"
				print "          Scan by proxies : -u http://example.com/ --level=2 \n "	
				print "          Scan by Delay : -u http://example.com/  --level=3 \n "	
				print "          Multi Scan by proxies : -r dic.txt --level=2 \n "
			
