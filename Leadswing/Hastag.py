from instabot import Bot
from time import sleep
my_bot = Bot()

#login

my_bot.login(username="xmen_naruto",password="hentai")

#k=0
#send message to someone
my_bot.send_message("heloo bla bla bla....","sujeetKumarrath")

#get the followers:
media_id = my_bot.get_media_id_from_link("https://www.instagram.com/p/CbiRcWsJoFD/?utm_source=ig_web_copy_link")
#user_name = my_bot.get_your_medias("media_id")
followers_list=[]
#followers_list = my_bot.get_user_likers(media_id)
user_name = my_bot.get_your_medias("media_id")
followers_list = my_bot.get_user_followers(user_name)

#my_bot.get_me
for each_followers in followers_list:
    username = my_bot.get_username_from_user_id(each_followers)
    msg = "Heloo-bla-bla ..."+username
    my_bot.send_message(msg,[username])
    print("Dm no.")
    #sleep(5)