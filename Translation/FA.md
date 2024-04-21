# موزیک پلیر 🎵🎶

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<img src="https://github.com/jokernets/y/blob/main/Music Player.gif"><br><br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


## `Translation 🔗`

  
- [ٍEnglish](https://github.com/jokernets/Music-player/blob/main/README.md)

- [عربية](https://github.com/jokernets/Music-player/blob/main/Translation/AR.md)


## جدول و فهرست مطالب ✅✔
<!--ts-->
   * [نصب کن!](#installation)

   * [آنالیز کد ها 📈](#analiys-code-)
     * [پارت 1 ✔](#part-1)
     * [پارت 2✔](#part-2)
     * [پارت 3✔](#part-3)
     * [پارت 4✔](#part-4)
  
   * [مثال های ویترین💯](#more-examples-and-showcase-)
     * [تصویر از برنامه 🔆](#project-image)
     * [ویدیو از برنامه 📺](#video-image-of-the-app-)
    
   * [`ارتباط با من 🌐👻`](#connect-me)
   * 
<!--te-->



# نصب کن !

## کتابخونه های زیر رو با پیپ نصب کنید:

```python
pip install `customtkinter`
pip install pygame
pip install threaded
pip instal Pillow
pip install math
pip install time
```

نصب موجود را به روز کنید: `pip3 install (کتابخانه شما) -- ارتقاء`
(تا حد امکان به روز رسانی کنید زیرا این کتابخانه در حال توسعه فعال است)

[صفحه custom tkinter توی گیت هاب 🌟](https://github.com/TomSchimansky/CustomTkinter)



# کد تجزیه و تحلیل :
این کد یک برنامه پخش کننده موسیقی با رابط گرافیکی است. از کتابخانه‌های «tkinter»، «customtkinter»، «pygame» و «PIL» استفاده می‌شود. این برنامه پنجره ای با ابعاد 400 در 480 پیکسل ایجاد می کند و یک پخش کننده موسیقی را نمایش می دهد. همچنین از نخ ها برای اجرای همزمان عملیات استفاده شده است. این برنامه به نظر می رسد که یک پخش کننده موسیقی با عملکرد پیشرفته باشد. 🎵🎶

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

## افزودن تابع ...

## پارت2:

به نظر می رسد شما یک قطعه کد پایتون مربوط به **پخش موسیقی و جلد آلبوم** را به اشتراک گذاشته اید. بیایید کارهایی که هر قسمت از کد شما انجام می دهد را تجزیه و تحلیل کنیم:

1. **راه اندازی اولیه**:
     - ماژول «pygame.mixer» را که معمولاً برای مدیریت صدا و موسیقی در پایتون استفاده می شود، مقداردهی اولیه کرده اید.
     - شما دو لیست تعریف کرده‌اید: «list_of_songs» حاوی نام فایل‌های آهنگ و «list_of_covers» حاوی نام فایل‌های جلد آلبوم.
     - متغیر 'n' روی 0 تنظیم شده است که برای پیگیری آهنگ فعلی استفاده می شود.

2. عملکرد **`get_album_cover`**:
     - این تابع یک «نام_آهنگ» و یک شاخص «n» می گیرد.
     - فایل تصویری (کاور آلبوم) مربوط به آهنگ فعلی را باز می کند.
     - اندازه تصویر را به 250x250 پیکسل تغییر می دهد.
     - یک برچسب در یک پنجره tkinter برای نمایش جلد آلبوم ایجاد می کند.
     - عنوان آهنگ را از نام فایل استخراج کرده و در زیر جلد آلبوم نمایش می دهد.

3. عملکرد ** `پیشرفت` **:
     - این تابع طول آهنگ فعلی (بر حسب ثانیه) را محاسبه می کند و آن را در 3 ضرب می کند (برای اهداف نمایشی).
     - نوار پیشرفت (که در کد شما نشان داده نشده است) را بر اساس موقعیت فعلی آهنگ به روز می کند.

4. عملکرد **`threading**:
     - یک رشته جدید برای اجرای همزمان تابع "پیشرفت" ایجاد می کند.

5. عملکرد **`play_music`**:
     - تابع 'threading' را فراخوانی می کند.
     - نام فایل آهنگ فعلی را بر اساس مقدار "n" تنظیم می کند.
     - آهنگ را با استفاده از «pygame.mixer.music.load» بارگیری می کند.
     - آهنگ را با حجم 0.5 پخش می کند.
     - «get_album_cover» را برای نمایش جلد آلبوم فراخوانی می کند.
     - برای انتقال به آهنگ بعدی، 'n' را افزایش می دهد.

6. **سایر توابع**:
     - "پرش_به جلو": به آهنگ بعدی می رود.
     - `skip_back`: دو آهنگ به عقب برمی گردد.
     - "pause_music": آهنگ در حال پخش را متوقف می کند.
     - `ولوم`: میزان صدا را بر اساس مقدار ارائه شده تنظیم می کند.

لطفاً توجه داشته باشید که برخی از بخش‌های گم شده در کد شما وجود دارد (به عنوان مثال، ایجاد پنجره tkinter، تنظیم نوار پیشرفت) 😊

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

## «بخش 3»:

قطعا! بیایید قطعه کدی که ارائه کرده‌اید را تجزیه کنیم:

1. **دکمه ها و برچسب ها**:
     - شما چندین دکمه و برچسب با استفاده از کتابخانه «customtkinter» ایجاد کرده اید.
     - در اینجا کاری است که هر دکمه و برچسب انجام می دهد:
         - "play_button": دکمه ای با برچسب "Play" که با کلیک کردن، عملکرد "play_music" را فعال می کند.
         - `skip_f`: دکمه ای با نماد ">" که با کلیک کردن به آهنگ بعدی می رود.
         - `lbl`: برچسبی که متن "دکمه پخش را کلیک کنید."
         - `skip_b`: دکمه ای با نماد "<" که با کلیک کردن به آهنگ قبلی برمی گردد.
         - "مکث": دکمه ای با برچسب "مکث" که آهنگ در حال پخش را متوقف می کند.
         - `slider`: یک نوار لغزنده (کنترل صدا) که میزان صدای موسیقی را تنظیم می کند.
         - نوار پیشرفت: نوار پیشرفت (در کد شما نشان داده نمی شود) که پیشرفت آهنگ در حال پخش را نشان می دهد.

2. **تماس های تابع**:
     - دکمه ها با عملکردهای خاصی مرتبط هستند ("play_music"، "skip_forward"، "skip_back"، "pause_music" و "volume").
     - این عملکردها پخش موسیقی، تنظیم صدا و نمایش کاور را کنترل می کنند.

3. **قطعات گمشده**:
     - قطعه کد شما شامل اجرای واقعی توابع ("play_music"، "skip_forward"، و غیره)، کتابخانه "customtkinter" یا تنظیم پنجره tkinter نیست.
     - نوار پیشرفت ("نوار پیشرفت") ذکر شده است اما در قطعه کد نشان داده نشده است.

به یاد داشته باشید که قسمت های از دست رفته را تکمیل کنید (مانند تعریف توابع و تنظیم پنجره tkinter) تا پخش کننده موسیقی خود را کاملاً کاربردی کنید.
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
<img src="https://github.com/jokernets/Music-player/assets/165279911/86db0356-d0b9-41ea-96fd-c15634fa5cc0" width="200" height="300"><br><br><img src="https://github.com/jokernets/y/blob/main/music.gif" width="200" height="300"><br><br>

## نمونه های بیشتر و ویترین 🎄👑

### تصویر ویدیویی برنامه 📺

https://github.com/jokernets/Music-player/assets/165279911/760e6b56-4831-4660-8dca-3fa1c6fb9d67


# "من را وصل کن"🌐👻
<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammad-fallahnejad-849031293/" height="40" width="60" /></a>
