#Convert text file into audio
#  text_to_audio.py
#  
#  Copyright 2020 Yogesh Lamichhane <yogeshlmc3@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.  

from gtts import gTTS
import os

print("Enter the full path of your text file to convert into audio: ")
location = input() #Taking the path of text file as input from user

basename = os.path.basename(location) #Getting filename (with extension i.e, filename.txt) to produce output as filename.mp3
basename = basename[:-4] # removing '.txt' extension from filename to produce output result as filename.mp3

yourFile = open(location, "r")
myText = yourFile.read().replace("\n", " ") #replaces new line (\n) of text with a space ( )

language = 'en'     #to convert text in English to English audio
#if your file is in other language and want the output audio in that language replace 'en' with your
#language example: 'ne' for Nepali, 'fr' for French and so on
output = gTTS(text=myText, lang=language, slow=False)

print("Converting text to audio...")
output.save(basename + ".mp3")

yourFile.close()
print("Finally! Your text is converted to audio.")
