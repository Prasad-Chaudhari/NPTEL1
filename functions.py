import pyautogui
import time

def travel(n):
	pyautogui.typewrite('\t'*int(n),interval=.25)

def write(s):
	pyautogui.typewrite(s,interval=.25)

def sleep(n):
	time.sleep(n)

def press(k):
	pyautogui.press(k)

def makingOfGroups(emailId,password,courseName,courseId):
	sleep(15)
	write(emailId)
	press('enter');sleep(10)
	write(password)
	press('enter')
	print "Signed In"

	sleep(15)
	travel(16);press('enter')
	print "Opening Create group page"

	sleep(10)
	write('Announcement list for '+courseName)
	press('tab')
	write(courseId+"-announce")
	press('tab')
	print "Group name and email id written"

	write("This is the mailing list of all registered users of the course "+courseName+". It is used to send announcements from the course staff.")
	print "written description"

	travel(3);press('enter')
	press('up');press('enter')
	print "View Topics-> Public"

	travel(2);press('enter')
	press('up');press('up');press('enter')
	press('up');press('enter')
	print "Post -> Owners of group, Managers of group"

	travel(2);press('enter')
	press('down');press('enter')
	print "Join the group -> Public"

	travel(2);press('enter');sleep(2);press('enter')
	print "Group created"

	sleep(15)
	travel(3);press('enter');sleep(2)
	press('f6')
	sleep(5)
	pyautogui.keyDown('shift')
	travel(6)
	pyautogui.keyUp('shift')
	press('enter')
	print "Managing settings"

	sleep(10)
	travel(2)
	press('space')
	print "Selecting the only member of group"

	travel(18);press('enter');sleep(2)
	press('up');press('enter')
	press('down');press('down');press('enter')
	print "Action -> Set Posting Permission -> Override - Allow Posting"

	sleep(10)
	travel(18);press('left');sleep(2)
	travel(2);press('right');sleep(2)
	press('tab')
	press('enter')
	sleep(5)
	travel(4);press('left');sleep(2)
	travel(16);press('enter')
	press('down');press('down');press('down');press('enter')
	travel(16);press('enter')
	print "Settings -> Email Options -> Post Replies -> Owner of the group"

	sleep(5)
	travel(11);press('enter');sleep(5)
	travel(4);press('left');sleep(2)
	travel(4);press('space')
	travel(20);press('enter')
	print "Settings -> Moderation -> Moderate all the messages of group"

	sleep(5)
	travel(8);press('left');sleep(2)
	travel(1);press('right');sleep(2)
	travel(4);press('enter');sleep(5)
	travel(5);press('left');sleep(2)
	travel(3);press('enter')
	press('down');press('down');press('down');press('enter')	
	travel(19);press('enter')
	print "Permission -> Access Permission -> Contact the owners -> Owner, Managers of the group"

	sleep(5)
	pyautogui.keyDown('shift')
	travel(1)
	pyautogui.keyUp('shift')
	press('enter');sleep(10)
	travel(16);press('enter')
	print "Opening Create group page"

	sleep(10)
	write("Discussion forum for "+courseName)
	press('tab')
	write(courseId+"-discuss")
	press('tab')
	print "Group name and email id written"

	write("Discussion forum for "+courseName)
	print "written description"

	travel(2);press('enter')
	press('down');press('down');press('down');press('enter')
	print "Group type -> Q&A forum"

	travel(1);press('enter')
	press('up');press('enter')
	print "View Topics-> Public"

	travel(2);press('enter')
	press('up');press('enter')
	print "Post -> Public"

	travel(2);press('enter')
	press('down');press('enter')
	print "Join the group -> Public"

	travel(2);press('enter');sleep(2)
	press('enter')
	print "Group created"

	sleep(15)
	travel(3);press('enter');sleep(5)
	press('f6');sleep(3)
	pyautogui.keyDown('shift')
	travel(6)
	pyautogui.keyUp('shift')
	press('enter')
	print "Managing settings"

	sleep(10)
	travel(2);press('space')
	travel(18);press('enter')
	press('up');press('up');press('right');press('enter')
	print "Members -> All members -> actions -> change delivery Setting -> No email"

	sleep(5)
	travel(18);press('left');sleep(2)
	travel(5);press('right');sleep(2)
	travel(1);press('enter');sleep(5)
	travel(7);press('left');sleep(2)
	travel(8);press('space')
	travel(17);press('enter')
	print "Information -> General Information -> Post Options -> Allow Posting by Email"

	sleep(10)
	travel(8);press('right');sleep(2)
	travel(3);press('enter');sleep(10)
	travel(5);press('left');sleep(2)
	travel(3);press('left');sleep(2)
	travel(8);press('enter')
	press('up');press('enter')
	travel(15);press('enter')
	print "Setting -> Moderation -> Spam messages -> Skip the moderations queue and post to the group"

	sleep(10)
	travel(8);press('left');sleep(2)
	travel(1);press('right');sleep(2)
	travel(3);press('enter');sleep(5)
	travel(5);press('left');sleep(2)
	travel(16);press('enter')
	press('up');press('enter')
	travel(2);press('enter')
	press('up');press('enter')
	travel(10);press('enter')
	press('up');press('enter')
	travel(16);press('enter')
	print "Permission -> Moderation Permission -> Many settings changed"

	sleep(10)
	pyautogui.keyDown('shift')
	travel(1)
	pyautogui.keyUp('shift')
	press('enter');sleep(10)
	travel(10);press('enter');sleep(2)
	travel(5);press('enter');sleep(15)
	travel(8);press('enter');sleep(10)
	travel(3);press('enter')
	press('f6');sleep(1)
	travel(3);press('enter');sleep(2)
	travel(1);press('enter')
