#import gtts module for text conversion

from gtts import gTTS
import os                   #os module is used for saving the output audio file
mytext = input('Enter your text :')
language = 'en'             #language selection
myobj = gTTS(text=mytext, lang=language, slow=True)   #save the output in an object
myobj.save("welcome.mp3")               #save the object in a audio file
os.system("mpg321 welcome.mp3")         #for saving in local directory