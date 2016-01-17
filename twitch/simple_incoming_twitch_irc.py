#Writen in python version 2.7.9

import socket
import requests
import json
import time

print "Press control-c to exit the program..."
raw = False
#Variables needed to connect to twitch
default_nick = "justinfan0"
NICKNAME = "bomb_mask"#put your nickname here please
OAUTH_KEY = ""#put your oauth key here please
try:
    channels = raw_input("What channel do you want to join: ").lower()
except:
    channels = "!batedurgonnadie"

total_followers = 1
command = None
if channels[0] == '@':
    target_user = (channels.strip())[1:]
    channels = ['',]
    command = "WHOIS {}\r\n".format(target_user)

elif channels[0] == '!':
    target_user = (channels.strip())[1:]
    base_url = """https://api.twitch.tv/kraken/users/{user}/follows/channels?limit={limit}&offset={offset}"""

    url = base_url.format(user=target_user, limit=1, offset=0)
    headers = {'Accept' : 'application/vnd.twitchtv.v3+json'}

    incoming_data = requests.get(url,headers=headers).json()

    total_followers = incoming_data["_total"]
    print total_followers
    k = raw_input("continue?")
    del k
    if total_followers > 0:
        print total_followers

        channels = [incoming_data["follows"][0]["channel"]["name"],]
        incoming_count = 1
        while incoming_count < total_followers:
            users_left = total_followers - incoming_count

            if users_left < 100:
                limit = users_left
            else:
                limit = 100

            url = base_url.format(user = target_user, limit = limit, offset = incoming_count)

            incoming_data = requests.get(url, headers=headers).json()


            for follow in incoming_data["follows"]:
                channels.append(follow["channel"]["name"])

            incoming_count += limit
            print incoming_count,'/',total_followers,'\t',(float(incoming_count)/total_followers)*100,'%'
            time.sleep(1)

        for channel in channels:
            print channel


    else:
        channels=[target_user,]

elif len(channels.split(' ')) > 1:
    channels = channels.split(' ')

else:
    channels = [channels,]

if True:
    #creating the object that lets us talk to the internet (a socket)
    irc = socket.socket()

    #(connecting to twitch irc servers)
    print "Connecting to twitch"
    irc.connect(("irc.twitch.tv", 6667))

    #If the information is wrong for PASS and NICK then we get disconnected
    #irc.sendall("PASS {}\r\n".format(OAUTH_KEY))
    irc.sendall("NICK {}\r\n".format(default_nick))

    if command == None:
        amount_of_joins = 0
        #calc eta
        print "ETA : ", 0.5*total_followers

        start_time = time.time()
        for channel in zip(*[channels[i:] for i in xrange(2)]):
            irc.sendall("JOIN #{}\r\n".format(channel[0]))
            time.sleep(0.5)
            amount_of_joins += 1

            print """{precentage}% Elapsed Time:{elapsed_time}(s)\t JOINED -> {lattest_join}{line_padding}\r"""\
            .format(precentage=int((float(amount_of_joins)/total_followers)*100), elapsed_time=int(time.time()-start_time), lattest_join=channel[0], line_padding=' '*10),
    elif command != None:
        irc.sendall(command)   

    irc.sendall('CAP REQ :twitch.tv/tags\r\n')

    try:
        while True:
            #get latest message from twitch (4096 is a buffer size)
            incoming = irc.recv(4096)

            #if they ask if we are still here reply with PONG to say we are
            if incoming.startswith("PING"):
            	irc.sendall("PONG tmi.twitch.tv\r\n")

            if raw:
                print incoming

            else:
                #Print the incoming data from the IRC connection
                try:
                    action = incoming.split(' ')[2]
                except:
                    print incoming
                    continue

                if action == "PRIVMSG":
                    msg_parts = incoming.split(' ')
                    c_msg = {}
                    c_msg["tags"] = dict(item.split('=') for item in msg_parts[0][1:].split(';'))
                    c_msg["sender"] = msg_parts[1][1:].split('!')[0]
                    c_msg["action"] = msg_parts[2]
                    c_msg["channel"] = msg_parts[3]
                    c_msg["message"] = ' '.join(msg_parts[4:])[1:].strip()
                    
                    print c_msg["channel"]+'\t::\t'+c_msg["sender"]+': '+c_msg["message"]+'\n'
                    

            with open("logging.txt",'a+') as fout:
                fout.write('&'+str(time.time())+';'+incoming)
                
    #clean up if we get a ctrl-c        
    except KeyboardInterrupt:
        #close twitch irc connection
        irc.close()

