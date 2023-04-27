import pyttsx3     #import pyttsx3
engine = pyttsx3.init()    #initialize the module
text = input('Enter text :')   #get the input text
engine.say(text)      #say the text