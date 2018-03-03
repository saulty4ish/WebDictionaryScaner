import requests
def GetTypeOfScript(url):     #Judge the script of website.
	try:
		r=requests.get(url,timeout=3)
	except requests.exceptions.ReadTimeout:
		print "Conncet failure,can't judge the script."
	except requests.exceptions.ConnectTimeout:
		print "Conncet failure,can't judge the script."
	if("aspx" in r.text):
		return "aspx"
	elif("php" in r.text):
		return  "php"
	elif("asp" in r.text):
		return  "asp" 
	elif("jsp" in r.text):	
		return  "jsp" 
	else:
		return "dir"

def GenerateReport(target):
	filename1=target.replace("http://","_")
	filename2=filename1.replace("/","_")
	filename3=filename2.replace(".","_")
	return filename3
def AddUrlToReport(url,filename):
	with open(filename+".txt","a") as f:
		f.write(url+"\n")
