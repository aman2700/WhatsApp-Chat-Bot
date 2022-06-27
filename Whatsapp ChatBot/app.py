from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from time import sleep
import random
from selenium import webdriver
from time import sleep
import os



class person:
    name = ''
    def setName(self, name):
        self.name = name

class username:
    user = ''
    def setUser(self,user):
        self.user = user

class password:
    pword = ''
    def setPass(self,pword):
        self.pword = pword
        
class post:
    posts = ''
    def setPost(self, posts):
        self.posts = posts
#class download:
#    image = ''
#    def setImage(self,image)
 #   self.image = image

app = Flask(__name__)

@app.route("/")
def hello():
    return "I'm alive!"

@app.route("/sms", methods=['POST'])





def sms_reply():

    msg = request.form.get('Body')
    print(msg)
    
    resp = MessagingResponse()
    
    def send_msg(sms):
        account_sid = 'ACb4c5XXXXXXXXXXXXXXXX'
        auth_token = '97a2XXXXXXXXXXXXXXXX'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=f'{sms}',
                                    from_='whatsapp:+1415XXXX86',
                                    to='whatsapp:+98xxxx41'
                                )

        print(message.sid)


    def send_media(media):
        account_sid = 'XXXXXXXXXXXXX'
        auth_token = 'XXXXXXXXXXXXX'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    media_url=f"{media}",
                                    from_='whatsapp:+XXXXXXX',
                                    to='whatsapp:+XXXXXXXXX'
                                )

        print(message.sid)


    def there_exists(terms):
        for term in terms:
            if term in msg:
                return True
    
    if there_exists(['hey','hi','hello','hola','wassup','sup','whatsup','whats up']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        send_msg(greet)

    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            send_msg("my name is Friday!")
        else:
            send_msg("my name is Friday. what's your name?")

    if there_exists(["my name is"]):
        person_name = msg.split("is")[-1].strip()
        send_msg(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember
    
        
    if there_exists(['username']):
        users = msg.split('username')[-1].strip()
        send_msg(f'your username: {users}')
        user_obj.setUser(users)

    
    if there_exists(['password']):
        passwords = msg.split('password')[-1].strip()
        send_msg(f"your password: {passwords}")
        pw_obj.setPass(passwords)
    
    if there_exists(['post']):
        posted = msg.split('post')[-1].strip()
        send_msg(f"scrolling {posted} post...")
        post_obj.setPost(posted)

    if there_exists(['corona virus','corona']):
        send_msg('getting stats.. please wait')
        class Corona:
            def __init__(self):
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")        
                
                self.driver = webdriver.Chrome(chrome_options=options)
                self.driver.get('https://www.worldometers.info/coronavirus/')
                
                world_case = self.driver.find_element_by_xpath("//div[@class='maincounter-number']").text
                print("Total Cases in the world= ",world_case)
                send_msg(f"Total Cases in the world= {world_case}")
                sleep(2)
                
                world_death = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[6]/div/span").text 
                print('Total Death due to Corona Virus in the World: ',world_death)
                send_msg(f'Total Death due to Corona Virus in the World: {world_death}')
                sleep(2)
                
                recover = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[7]/div/span").text
                print('Total Recovered in the World: ',recover)
                send_msg(f'Total Recovered in the World: {recover}')
                
                sleep(2) 
                
                usa_tc = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[4]/td[2]").text
                print('Total Cases in USA: ',usa_tc)
                send_msg(f'Total Cases in USA: {usa_tc}')

                sleep(2)

                usa_td = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[4]/td[4]").text
                print("Total Death in USA: ",usa_td)
                send_msg(f"Total Death in USA: {usa_td}")

                sleep(2)

                usa_nd = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[4]/td[5]").text
                print("New Death Today in USA: ",usa_nd)
                send_msg(f"New Death Today in USA: {usa_nd}")
                sleep(2)
                
                italy_td = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[7]/td[4]").text
                print("Total Death in Italy: ",italy_td)
                send_msg(f"Total Death in Italy: {italy_td}")

                sleep(2)

                india_tc = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[24]/td[2]").text
                print('Total Cases in India: ',india_tc)
                send_msg(f'Total Cases in India: {india_tc}')

                sleep(2)

                india_td = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[24]/td[4]").text
                print('Total Death in India: ',india_td)
                send_msg(f'Total Death in India: {india_td}')

                sleep(2)
                
                india_nc =  self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[24]/td[3]").text
                print("New Cases in India Today: ",india_nc)
                send_msg(f"New Cases in India Today: {india_nc}")
                
                sleep(2)

                india_nd = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]/tr[24]/td[5]").text
                print("New Deaths Today in India: ",india_nd)
                send_msg(f"New Deaths Today in India: {india_nd}")
                self.driver.quit()
        bot = Corona()
        
    
    if there_exists(['scroll feed']):
        post_scroll = int(post_obj.posts)
        print(post_scroll)

        scroll = int(post_scroll)*693
        print(scroll)
        class InstaScroll:
            
            def download_feed(self):
                options = webdriver.ChromeOptions()
                #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("start-maximized")
                options.add_argument("--no-sandbox")     
                
                self.driver = webdriver.Chrome(chrome_options=options)
                
                self.driver.get("https://instagram.com")
                self.driver.implicitly_wait(4)
                        
                self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                    .send_keys(user_obj.user)
                self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                    .send_keys(pw_obj.pword)
                
                self.driver.find_element_by_xpath('//button[@type="submit"]')\
                    .click()
                send_msg('logged in')
                print('logged in')
                self.driver.implicitly_wait(6)
                #self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
                    
                
                img_srcs = []
                
            
                self.driver.execute_script(f"window.scrollTo(0, {scroll});") # scroll down

                img_srcs.extend([img.get_attribute('src') for img in self.driver.find_elements_by_class_name('FFVAD')]) # scrape srcs

                img_srcs = list(set(img_srcs)) # clean up duplicates
                
                for link in img_srcs:
                    print(link)
                    send_media(link)
                self.driver.quit()
                
            
        bot = InstaScroll()
        bot.download_feed()

 
 
 
 
 
    #if there_exists(['download images of']):
     #   images = msg.split('of')[-1].strip()
      #  send_msg(f'you want to download images of {images}')
        #img_obj.setImage(images)
    if there_exists(['download images of']):
        images = msg.split('of')[-1].strip()
        print(images)
        send_msg(f'downloading images of {images} please wait for few seconds {person_obj.name}')
        
    
        class InstaDownload:
            def download_user_images(self):
                options = webdriver.ChromeOptions()
                #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
      
                self.driver = webdriver.Chrome(chrome_options=options)
                self.driver.get(f"https://instagram.com/{images}")
                self.driver.implicitly_wait(2)

                img_srcs = []
                finished = False
                while not finished:

                    finished = self.infinite_scroll() # scroll down

                    img_srcs.extend([img.get_attribute('src') for img in self.driver.find_elements_by_class_name('FFVAD')]) # scrape srcs

                img_srcs = list(set(img_srcs)) # clean up duplicates
                
                for link in img_srcs:
                    print(link)
                    send_media(link)
                self.driver.quit()
                
            
            def infinite_scroll(self):
                self.last_height = self.driver.execute_script("return document.body.scrollHeight")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                self.driver.implicitly_wait(5)

                self.new_height = self.driver.execute_script("return document.body.scrollHeight")


                if self.new_height == self.last_height:
                    return True

                self.last_height = self.new_height
                return False

        bot = InstaDownload()
        bot.download_user_images()


    
    
    if there_exists(["how are you","how are you doing"]):
        send_msg(f"I'm very well, thanks for asking {person_obj.name}")

    if there_exists(['send me your photo','your photo','send me your image']):
        send_msg("ok wait")
        send_media("https://cdn.statically.io/img/manofmany.com/wp-content/uploads/2019/07/50-Minimalist-iPhone-Wallpapers-37.jpg")
        
    if there_exists(["nice",'you are pretty','good','excellent']):
        send_msg(f'thankyou {person_obj.name}')
    
    if there_exists(["exit", "quit", "goodbye",'bye']):
        send_msg(f"Ok bye {person_obj.name}")

    
    if there_exists(['instagram']):
        user_cred = user_obj.user
        send_msg(user_cred)
        user_pass = pw_obj.pword
        send_msg(user_pass)

        send_msg('sending results in few seconds')
        
        class InstaBot:
            def __init__(self,user_cred,user_pass):
                options=webdriver.ChromeOptions()
                #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
            
                
                self.driver = webdriver.Chrome(chrome_options=options)        
                
                self.driver.get("https://instagram.com")
                self.driver.implicitly_wait(2)
                
                self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                    .send_keys(user_cred)
                self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                    .send_keys(user_pass)
                
                self.driver.find_element_by_xpath('//button[@type="submit"]')\
                    .click()
                send_msg('logged in')
                print('logged in')
                #sleep(4)
                #self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
                self.driver.implicitly_wait(6)

            def get_unfollowers(self):
                self.driver.get(f"https://instagram.com/{user_cred}")
                sleep(4)
                self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                    .click()
                print('following')
                send_msg('scraping your following')
                following = self._get_names()
                self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
                    .click()
                print('getting names')
                send_msg('scraping your followers and getting names')
                followers = self._get_names()
                not_following_back = [user for user in following if user not in followers]
                self.driver.quit()
                send_msg('here are the cunts who are not following back')
                for name in not_following_back:
                    send_msg(name)
                               
                    
            
            def _get_names(self):
                    
                
                self.driver.implicitly_wait(3)
                scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
                last_ht, ht = 0, 1
                while last_ht != ht:
                    last_ht = ht
                    self.driver.implicitly_wait(3)
                    ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
                links = scroll_box.find_elements_by_tag_name('a')
                names = [name.text for name in links if name.text != '']
                # close button
                self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
                    .click()
                
                return names
        
                
                
                


        my_bot = InstaBot(user_cred,user_pass)
        my_bot.get_unfollowers()

        
        
    
    #else:
     #   resp.message("Friday you said : {}".format(msg))
   #https://fridaywhatsappbot.herokuapp.com/sms
    return str(resp)
sleep(1)
person_obj = person()
user_obj = username()
pw_obj = password()
post_obj = post()
#img_obj = download()    
    

if __name__ == "__main__":
    app.run(debug=True)
