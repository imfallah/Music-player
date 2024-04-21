#__________________________________________________________________
#                                     
#                           MUSIC PLAYER
#               
#                         GITHUB : jokerents      
#__________________________________________________________________

#importing Library
import tkinter
from tkinter.ttk import Progressbar
import customtkinter  #GUI
import pygame
from PIL import Image, ImageTk #Cover song
from threading import *
import time
import math
import pygame.mixer

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  

##### Tkinter  
root = customtkinter.CTk()
root.title('Music Player')
root.geometry('400x480')

root.geometry("400x480+{}+{}".format(root.winfo_screenwidth() // 2 -270, root.winfo_screenheight() // 2 - 270))

pygame.mixer.init()
##########################

list_of_songs = ['music/Dasht Parvaneha.mp3','music/Plikan_Sorena.mp3','Shootia.mp3','music/pelikan.mp3']
list_of_covers = ['cover/dasht.jpg','cover/albom.jpg','cover/shotia.jpg','cover /pelikan.jpg'] 


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

root.mainloop()
