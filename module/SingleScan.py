import Queue
import common
import requests
import threading
import random
import time
class SingleScan:
	def __init__(self,url,Type,filename,ThreadNum=20,Sleeptime=3):
		self.url=url
		self.Type=Type
		self.ThreadNum=ThreadNum
		self.Targets=Queue.Queue()
		self.Pro=[]
		self.RandomProxy=""
		self.Sleeptime=Sleeptime
		self.filename=filename
	def OpenDir(self):
		NameOfDir=["asp","php","aspx","jsp","unknown"]
		for i in range(0,5):
			if(self.Type==NameOfDir[i]):
				with open("config/"+self.Type+".txt","r") as f:
					for line in f.readlines():
						payload=self.url+line.strip()
						if(payload!=self.url):
							self.Targets.put(payload)
			else:
				with open("config/"+self.Type+".txt","r") as f:
					for line in f.readlines():
						payload=self.url+line.strip()
						if(payload!=self.url):
							self.Targets.put(payload)
	def FindDir(self):              
		while not self.Targets.empty():
			target=self.Targets.get()
			try:
				filename=common.GenerateReport(self.url)
				r=requests.head(target,timeout=3)
				if(r.status_code==200):
					print target
					common.AddUrlToReport(target,self.filename)
			except:
				continue
	def Work(self):
		Threads=[]
		for i in range(self.ThreadNum):
			t=threading.Thread(target=self.FindDir)
			Threads.append(t)
			t.start()
		for t in Threads:
			t.join(3)
	def GetProxy(self):
		with open("config/proxy.txt","r") as f:
			for line in f.readlines():
				proxy="https://"+line.strip()+"/"
				self.Pro.append(proxy)
	def Bypass(self):
		while not self.Targets.empty():
			target=self.Targets.get()
			flag=0
			i=random.randint(0,len(self.Pro)-1)
			self.RandomProxy=self.Pro[i]
			try:
				proxy="https://"+self.RandomProxy+"/"
				proxies={"https":proxy}	
				r=requests.head(target,timeout=3,proxies=proxies)
				if(r.status_code==200)&(flag==0):
					print target
					common.AddUrlToReport(target,self.filename)
					flag=1
			except:
				continue
			
	def Sleep(self):
		while not self.Targets.empty():
			target=self.Targets.get()
			try:
				r=requests.head(target,timeout=3)
				if(r.status_code==200):
					print target
					common.AddUrlToReport(target,self.filename)
				time.sleep(self.Sleeptime)
			except:
				continue
	def WorkByProxy(self):
		Threads=[]
		for i in range(self.ThreadNum):
			t=threading.Thread(target=self.Bypass)
			Threads.append(t)
			t.start()
		for t in Threads:
			t.join(3)
