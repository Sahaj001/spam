import pyautogui as pyg
import time
import subprocess as sp
import os

class spamImage:
        
        def __init__(self, groupName, startText="u know who?", imageText=":O"):
                self.groupName = groupName
                self.startText = startText
                self.imageText = imageText
        
        def hotkey(self,key):
                pyg.keyDown('command')
                if key == "paste":
                        pyg.press('v')
                elif key == "find":
                        pyg.press('f')
                pyg.keyUp('command')  

        def imagepaste(self,filename):
                
                comnd = [
                "osascript",
                "-e",
                'set the clipboard to (read (POSIX file "'
                + filename +
                '") as JPEG picture)',
                ]
                
                sp.Popen(comnd)
                
                #paste and send
                time.sleep(0.5)
                self.hotkey("paste")
                time.sleep(0.5)
                pyg.typewrite(self.imageText)
                pyg.press('enter')
         
        def start(self):
                # open application
                sp.Popen(["/usr/bin/open", "-W", "-a", "/Applications/Whatsapp.app"])                       

                # check is application is opened
                time.sleep(2)

                #find group
                self.hotkey("find")

                #enter group name
                pyg.typewrite(self.groupName)
                pyg.press('enter')
                print("found")
                time.sleep(0.5)

                #enter some text to group
                pyg.typewrite(self.startText+"\n")

                # iterate through every file in folder
                directory = os.fsencode("/Users/sahajsingh/Documents/drone/image/")
                
                for file in os.listdir(directory):
                        filename = os.fsencode(file)
                        filex = str(os.path.join(directory, filename))
                        myfile = filex[2:-1];
                        if myfile.endswith(".jpg") or myfile.endswith(".jpeg"):
                                self.imagepaste(myfile)



if __name__ == "__main__":

        # spamImage(GroupName, StartText, Text with each image)
        
        mySpam = spamImage("Sara", "u no who? sahaj", ":)")
        
        mySpam.start()
