import os
import sys
import subprocess
import pyautogui
import time

class SupaplexCheatEngine:

	def __init__(self):
		self.p = subprocess.Popen("SUPAPLEX.EXE")
		self.screenWidth, self.screenHeight = pyautogui.size()
		self.currentMouseX, self.currentMouseY = pyautogui.position()

	def waitForImage(self, name, timeout=30):
		tStart = time.time()
		image = pyautogui.locateOnScreen("hacker-engine-data/"+name)
		#Searches for the image
		while image == None:
		    image = pyautogui.locateOnScreen("hacker-engine-data/"+name)
		    if time.time() - tStart > timeout:
		    	print("Giving up, can't find image: "+name)
		    	return None
		return image


	def startGame(self):
		image = self.waitForImage("startup-entry-code.png")
		if image == None:
			return
		pyautogui.write("420", interval=0.25)
		pyautogui.press('enter')
		image = self.waitForImage("player-menu-down.png")
		print(image)
		if image == None:
			return
		pyautogui.moveTo(image.left, image.top, duration=2, tween=pyautogui.easeInOutQuad)
		pyautogui.click()


	def terminate(self):
		self.p.terminate()

	def run(self):
		self.pOut = self.p.communicate()
		time.sleep(3)
		self.startGame()


if __name__ == "__main__":

	engine = SupaplexCheatEngine()
	engine.run()
	engine.terminate()