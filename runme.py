from WarriorScanner import run_script
from termcolor import colored
from pyfiglet import Figlet

if __name__=="__main__":
	banner=Figlet(font='banner3-D')
	print(colored(banner.renderText('warrior scanner'),'green'))
	run_script()