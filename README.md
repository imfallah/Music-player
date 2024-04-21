# MUSIC PLAYER 🎵🎶
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<img src="https://github.com/jokernets/y/blob/main/Music Player.gif"><br><br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


## `Translation 🔗`

  
- [فارسی](Translation/FA.md)

- [عربية](Translation/AR.md)


Table of contents ✅✔
=================

<!--ts-->
   * [Installation](#installation)

   * [Anilayes Code📈](#analiys-code-)
     * [PART 1✔](#part-1)
     * [PART 2✔](#part-2)
     * [PART 3✔](#part-3)
     * [PART 4✔](#part-4)
  
   * [Mor Example💯](#more-examples-and-showcase-)
     * [Picture Project🔆](#project-image)
     * [Video Project📺](#video-image-of-the-app-)
    
   * [`CONNECT ME🌐👻`](#connect-me)
<!--te-->



# Installation

## Install the module with pip:

```python
pip install `customtkinter`
pip install pygame
pip install threaded
pip instal Pillow
pip install math
pip install time
```

Update existing installation:`pip3 install (YOUR LIBRARY) --upgrade`
(update as often as possible because this library is under active development)

[Custom tkinter in GITHUB🌟](https://github.com/TomSchimansky/CustomTkinter)



# Analiys Code :
This code is a music player program with a graphical interface. `tkinter`, ``customtkinter``, ``pygame`` and ``PIL``libraries are used. The program creates a window with dimensions of 400 x 480 pixels and displays a music player. Also, threads have been used to execute operations simultaneously. This program looks like it is supposed to be a music player with advanced functionality. 🎵🎶

## `PART 1`
```python
#importing Libraries
import tkinter
from tkinter.ttk import Progressbar
import customtkinter  #GUI APP 
import pygame #programe_bar
from PIL import Image, ImageTk #Cover song
from threading import *
import time
import math
import pygame.mixer

#customtkinter Setting color
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  

#create GUI to customtkinter
root = customtkinter.CTk()
root.title('Music Player')
root.geometry('400x480')
#geometry setting
root.geometry("400x480+{}+{}".format(root.winfo_screenwidth() // 2 -270, root.winfo_screenheight() // 2 - 270))

root.mainloop()
```
<img src="https://github.com/jokernets/Music-player/assets/165279911/adf6cf19-09fb-46b3-8ec0-aafee6b11a43" width="200" height="300"><br><br>

## Adding Fuction ...

## `PART 2`:

It seems like you've shared a snippet of Python code related to **music playback and album covers**. Let's break down what each part of your code does:

1. **Initialization**:
    - You've initialized the `pygame.mixer` module, which is commonly used for handling sound and music in Python.
    - You've defined two lists: `list_of_songs` containing song filenames and `list_of_covers` containing album cover filenames.
    - The variable `n` is set to 0, which will be used to keep track of the current song.

2. **`get_album_cover` Function**:
    - This function takes a `song_name` and an index `n`.
    - It opens an image file (album cover) corresponding to the current song.
    - Resizes the image to 250x250 pixels.
    - Creates a label in a tkinter window to display the album cover.
    - Extracts the song title from the filename and displays it below the album cover.

3. **`progress` Function**:
    - This function calculates the length of the current song (in seconds) and multiplies it by 3 (for demonstration purposes).
    - It updates a progress bar (not shown in your code) based on the current position of the song.

4. **`threading` Function**:
    - Creates a new thread to run the `progress` function concurrently.

5. **`play_music` Function**:
    - Calls the `threading` function.
    - Sets the current song filename based on the value of `n`.
    - Loads the song using `pygame.mixer.music.load`.
    - Plays the song with a volume of 0.5.
    - Calls `get_album_cover` to display the album cover.
    - Increments `n` to move to the next song.

6. **Other Functions**:
    - `skip_forward`: Advances to the next song.
    - `skip_back`: Goes back two songs.
    - `pause_music`: Pauses the currently playing song.
    - `volume`: Adjusts the volume based on the provided value.

Please note that there are some missing parts in your code (e.g., tkinter window creation, progress bar setup) 😊

```python
pygame.mixer.init()

list_of_songs = ['music 1','music 2','music 3']
list_of_covers = ['cover 1','cover 2','cover 3'] 

n=0

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)
    
    #Title Songs
    stripped_string = song_name[6:-4]
    
    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.4, rely=.6)


def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(0.4)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)

def threading():
    t1 = Thread(target=progress)
    t1.start()

def play_music():
    threading()
    global n 
    current_song = n
    if n > 2:
        n = 0
        
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    
    get_album_cover(song_name, n)


    n += 1
#skip_forward
def skip_forward():
    
    play_music()
#skip_back
def skip_back():
    global n
    n -= 2
    play_music()
    
#Pause_music
def pause_music():
    pygame.mixer.music.pause()
    
#volume
def volume(value):
    
    pygame.mixer.music.set_volume(value)
```

## `PART 3`:

Certainly! Let's break down the code snippet you've provided:

1. **Buttons and Labels**:
    - You've created several buttons and labels using the `customtkinter` library.
    - Here's what each button and label does:
        - `play_button`: A button labeled "Play" that triggers the `play_music` function when clicked.
        - `skip_f`: A button with the ">" symbol that advances to the next song when clicked.
        - `lbl`: A label displaying the text "Click the Play Button."
        - `skip_b`: A button with the "<" symbol that goes back to the previous song when clicked.
        - `Pause`: A button labeled "Pause" that pauses the currently playing song.
        - `slider`: A slider (volume control) that adjusts the volume of the music.
        - `progressbar`: A progress bar (not shown in your code) that reflects the progress of the currently playing song.

2. **Function Calls**:
    - The buttons are associated with specific functions (`play_music`, `skip_forward`, `skip_back`, `pause_music`, and `volume`).
    - These functions control music playback, volume adjustment, and cover display.

3. **Missing Parts**:
    - Your code snippet doesn't include the actual implementation of the functions (`play_music`, `skip_forward`, etc.), the `customtkinter` library, or the tkinter window setup.
    - The progress bar (`progressbar`) is mentioned but not shown in the code snippet.

Remember to complete the missing parts (such as defining the functions and setting up the tkinter window) to make your music player fully functionaL 😊

```python
# All Buttons
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.55, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.75, rely=0.7, anchor=tkinter.CENTER)

lbl=customtkinter.CTkLabel(master=root,text="Click the Play Button")
lbl.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.26, rely=0.7, anchor=tkinter.CENTER)

Pause = customtkinter.CTkButton(master=root, text='Pause', command=pause_music, width=2)
Pause.place(relx=0.35, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_= 0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a',width=250)
progressbar.place(relx=.5, rely=.78, anchor=tkinter.CENTER)
```
<img src="https://github.com/jokernets/Music-player/assets/165279911/86db0356-d0b9-41ea-96fd-c15634fa5cc0" width="200" height="200"><br><br><img src="https://github.com/jokernets/y/blob/main/music.gif" width="200" height="300"><br><br>


## More Examples and Showcase 🎄👑

### Video image of the APP 📺

https://github.com/jokernets/Music-player/assets/165279911/760e6b56-4831-4660-8dca-3fa1c6fb9d67



# `CONNECT ME`🌐👻

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/in/mohammadfallahnejad/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammadfallahnejad/" height="40" width="60" /></a>













