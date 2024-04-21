# مشغل الموسيقى 🎵🎶

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<img src="https://github.com/jokernets/y/blob/main/Music Player.gif"><br><br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


## `الترجمه 🔗`

  
- [English]()
- [فارسی]()






## جدول المحتويات ✅✔



<!--ts-->

 * [تثبیت](#%D8%AB%D9%8E%D8%A8%D9%8E%D9%91%D8%AA%D9%8E)

 * [كود التحليل 📈](#%D9%83%D9%88%D8%AF-%D8%A7%D9%84%D8%AA%D8%AD%D9%84%D9%8A%D9%84)
   * [الجزء 1✔](
#%D8%A7%D9%84%D8%AC%D8%B2-1)
   * [الجزء 2✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-2)

   * [الجزء 3✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-3)
   
* [المزيد من الأمثلة💯](#%D8%A7%D9%84%D9%85%D8%B2%D9%8A%D8%AF-%D9%85%D9%86-%D8%A7%D9%84%D8%B9%D9%8A%D9%86%D8%A7%D8%AA-%D9%88%D8%A7%D9%84%D8%B9%D8%B1%D8%B6-)
  * [مشروع فيديو📺](#%D8%B5%D9%88%D8%B1%D8%A9-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%84%D9%84%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC-)
 


*[`تواتصل معی🌐👻`](#%D8%A7%D8%AA%D8%B5%D9%84-%D8%A8%D9%8A)
<!--te-->



# ثَبَّتَ!

## قم بتثبيت المكتبات التالية باستخدام النقطة:

```python
pip install `custom tkinter`
pip install pygame
pip install threaded
pip instal Pillow
pip install math
pip install time
```

قم بتحديث التثبيت الحالي: تثبيت pip3 (مكتبتك) - ترقية
(قم بالتحديث قدر الإمكان لأن هذه المكتبة قيد التطوير النشط)


[صفحة المكتبة custom tkinter على جيثب🌟](https://github.com/TomSchimansky/CustomTkinter)



# كود التحليل:
## `الجز 1`:
هذا الكود عبارة عن برنامج مشغل موسيقى ذو واجهة رسومية. يتم استخدام مكتبات tkinter وcustomtkinter وpygame وPIL. يقوم هذا البرنامج بإنشاء نافذة بحجم 400 × 480 بكسل ويعرض مشغل الموسيقى. تُستخدم الخيوط أيضًا لتنفيذ العمليات في وقت واحد. يبدو أن هذا التطبيق هو مشغل موسيقى عالي الأداء. 🎵🎶


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
<img src="https://github.com/jokernets/y/assets/165279911/54a3c058-81cf-419e-81eb-b8f4147134cf" width="200" height="300"><br><br>

## إضافة وظيفة...

## الجزء 2:

يبدو أنك شاركت جزءًا من كود Python المتعلق بـ **تشغيل الموسيقى وصورة الألبوم**. دعنا نحلل ما يفعله كل جزء من التعليمات البرمجية الخاصة بك:

1. **الإعداد الأولي**:
      - لقد قمت بتهيئة الوحدة ``pygame.mixer''، والتي تُستخدم عادةً لإدارة الصوت والموسيقى في Python.
      - لقد حددت قائمتين: "list_of_songs" التي تحتوي على أسماء ملفات الأغاني و"list_of_covers" التي تحتوي على أسماء ملفات غلاف الألبوم.
      - تم تعيين المتغير 'n' على 0، والذي يستخدم لتتبع المسار الحالي.

2. وظيفة **`get_album_cover`**:
      - تأخذ هذه الوظيفة "song_name" وفهرس "n".
      - يفتح ملف الصورة (غلاف الألبوم) للأغنية الحالية.
      - تغيير حجم الصورة إلى 250x250 بكسل.
      - إنشاء ملصق في نافذة tkinter لعرض صورة الألبوم.
      - يستخرج عنوان الأغنية من اسم الملف ويعرضه تحت غلاف الألبوم.

3. الأداء ** ``التقدم'' **:
      - تحسب هذه الوظيفة طول الأغنية الحالية (بالثواني) وتضربها في 3 (لأغراض العرض التوضيحي).
      - يقوم بتحديث شريط التقدم (غير الموضح في الكود الخاص بك) بناءً على موضع المسار الحالي.

4. وظيفة **`الترابط**:
      - إنشاء موضوع جديد لتشغيل وظيفة "التقدم" بشكل متزامن.

5. وظيفة **`play_music'**:
      - يستدعي وظيفة "الخيوط".
      - يضبط اسم الملف للمسار الحالي بناءً على قيمة "n".
      - تحميل الأغنية باستخدام "pygame.mixer.music.load".
      - تشغيل الأغنية بمستوى صوت 0.5.
      - يستدعي get_album_cover لعرض غلاف الألبوم.
      - يزيد 'n' للانتقال إلى المسار التالي.

6. **وظائف أخرى**:
      - "skip_forward": للانتقال إلى المسار التالي.
      - `skip_back`: تخطي مسارين للخلف.
      - "pause_music": يوقف الأغنية الجاري تشغيلها مؤقتًا.
      - ``مستوى الصوت'': يضبط مستوى الصوت بناءً على القيمة المقدمة.

يرجى ملاحظة أن هناك بعض الأجزاء المفقودة في التعليمات البرمجية الخاصة بك (على سبيل المثال، إنشاء نافذة tkinter، وتعيين شريط التقدم) 😊
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

## "الجز 3":

بالتأكيد! دعنا نحلل مقتطف الشفرة الذي قدمته:

1. **الأزرار والعلامات**:
      - لقد قمت بإنشاء العديد من الأزرار والتسميات باستخدام مكتبة "customtkinter".
      - إليك ما يفعله كل زر وتسمية:
          - "play_button": زر يسمى "Play" والذي عند النقر عليه يقوم بتنشيط وظيفة "play_music".
          - `skip_f`: زر به رمز ">" ينتقل إلى المسار التالي عند النقر عليه.
          - `lbl`: ملصق يحتوي على النص "انقر فوق زر التشغيل".
          - `skip_b`: زر به رمز "<" يعود إلى المسار السابق عند النقر عليه.
          - "إيقاف مؤقت": زر يسمى "إيقاف مؤقت" يقوم بإيقاف الأغنية الجاري تشغيلها مؤقتًا.
          - `شريط التمرير`: شريط تمرير (التحكم في مستوى الصوت) يضبط مستوى صوت الموسيقى.
          - شريط التقدم: شريط تقدم (غير موضح في الكود الخاص بك) يُظهر تقدم الأغنية قيد التشغيل حاليًا.

2. **استدعاءات الوظائف**:
      - ترتبط الأزرار بوظائف محددة ("play_music" و"skip_forward" و"skip_back" و"pause_music" و"volume").
      - تتحكم هذه الوظائف في تشغيل الموسيقى وتعديل مستوى الصوت وعرض الغطاء.

3. **الأجزاء المفقودة**:
      - لا يتضمن مقتطف الكود الخاص بك التنفيذ الفعلي للوظائف ("play_music"، "skip_forward"، وما إلى ذلك)، أو مكتبة "customtkinter"، أو إعداد نافذة tkinter.
      - تم ذكر شريط التقدم ("شريط التقدم") ولكن لم يتم عرضه في مقتطف الشفرة.

تذكر إكمال الأجزاء المفقودة (مثل تحديد الوظائف وإعداد نافذة tkinter) لجعل مشغل الموسيقى الخاص بك يعمل بكامل طاقته.
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
<img src="https://github.com/jokernets/y/assets/165279911/6deeb82b-a2c8-4594-866a-632eb9f05920" width="200" height="300"><br><br><img src="https://github.com/jokernets/y/blob/main/music.gif" width="200" height="300"><br><br>

## المزيد من العينات والعرض 🎄👑

### صورة فيديو للبرنامج 📺


   # "لا تشعر بأي شيء".


# "اتصل بي"🌐👻
<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammad-fallahnejad-849031293/" height="40" width="60" /></a>
