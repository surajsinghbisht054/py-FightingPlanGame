#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
print __author__

import Tkinter, time, random, sys
from PIL import Image, ImageTk
SPEED_OF_PLAIN=10
SPEED_OF_ROCK=5.0
Bullet_SIZE=3
NUMBER_ROCKS=15
NUMBER_OF_BULLETS=50
BULLETS_HIT_PER_ROCK=4
INCREASING_RATE=1
BULLETS_SPEED=SPEED_OF_PLAIN*2

class canvas(Tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        Tkinter.Canvas.__init__(self, *args, **kwargs)
        self.creating_ground_for_figting()
        self.creating_game_mechanizism()
        
    def creating_game_mechanizism(self):
        self.create_fighter_plain_image()
        self.binding_keys_movement()
        self.rocks=[]
        self.creating_bullets_line()
        
    def creating_ground_for_figting(self):
        h=self.winfo_screenheight()
        w=self.winfo_screenwidth()
        img=Image.open('sky3.jpg')
        img=img.resize((w,h))
        img=ImageTk.PhotoImage(img)
        self.imageid123=img
        self.create_image(w/2,h/2, image=img)
        
    def check_bullet_hit_(self):
        h=self.winfo_height()
        w=self.winfo_width()
        for rock in self.rocks:
            a,b,c,d=self.bbox(rock)
            k=self.find_overlapping(a,b,c,d)
            if len(k)>=BULLETS_HIT_PER_ROCK:
                x1,y1=self.coords(rock)
                self.move(rock,0,-h-70)
                sw=random.randint(0, w)
                sw=sw-x1
                self.move(rock,sw,0)
		
        return
        
    
    def game_firing_rules(self):
        a,b,c,d=self.bbox(self.plain)
	b=b+30
	d=d-30
	a=a+30
	c=c-30
        k=self.find_overlapping(a,b,c,d)
        if len(k)>=3:
            w=self.winfo_width()/2
            h=self.winfo_height()/2
            self.create_text(w,h, text='Game Over', font=('arial 45 bold'), fill='red')
	    self.master.update()
	    time.sleep(3)
	    self.master.destroy()
	    sys.exit(0)
        self.check_bullet_hit_()
        return

    
    def creating_bullets_line(self):
        self.bullets=[]
        x=0
        for i in range(NUMBER_OF_BULLETS):
            self.creating_bullets()
        for i in self.bullets:
            self.move(i, 0, -x)
            x=x+100
        
    def creating_bullets(self):
        sh=50
        x1,y1=self.coords(self.plain)
        y1=(y1-50)-sh
        x1=x1-Bullet_SIZE
        x2=x1+Bullet_SIZE*2
        y1=y1-Bullet_SIZE
        y2=y1+Bullet_SIZE*5
        storeobj=self.create_rectangle(x1,y1,x2,y2, fill='blue')
        self.bullets.append(storeobj)
        return
    
    def updating_bullets(self):
        w=self.winfo_width()
        h=self.winfo_height()
        x1_,y1_=self.coords(self.plain)
        h=y1_-70
        for bullet in self.bullets:
            x1,y1,x2,y2=self.coords(bullet)
            k=self.find_overlapping(x1,y1,x2,y2)
            sw=x1+((x2-x1)/2)
            sw=x1_-sw
            if y1<=0:
                self.move(bullet,sw,h)
            else:
                self.move(bullet,0,-BULLETS_SPEED)
        return

    def creating_falling_rocks_rain(self):
        self.img_list=[]
        self.master.update()
        self.master.update_idletasks()
        for i in range(NUMBER_ROCKS):
            self.creating_falling_rocks()
        return
        
    def creating_falling_rocks(self):
        rock=Image.open('Rock.png')
        img=ImageTk.PhotoImage(rock)
        self.img_list.append(img)
        w=self.winfo_width()
        h=self.winfo_height()
        sw=random.randint(0, w)
        sh=random.randint(0, h)
        storeobj=self.create_image(sw,sh, image=img)
        self.rocks.append(storeobj)
        return
    
    def update_rock_falls(self):
        h=self.winfo_height()
        w=self.winfo_width()
        if len(self.rocks)==0:
            self.creating_falling_rocks_rain()
        for rock in self.rocks:
            x1,y1=self.coords(rock)
            if y1>h+50:
                self.move(rock,0,-h-70)
                sw=random.randint(0, w)
                sw=sw-x1
                self.move(rock,sw,0)
            else:
                self.move(rock,0,int(SPEED_OF_ROCK))
        return
    
    def update_loop(self):
        self.update_rock_falls()
        self.updating_bullets()
        self.game_firing_rules()
        return
        
    def binding_keys_movement(self):
        for seq in ['<Key-Right>','<Key-Left>','<Key-Up>','<Key-Down>']:
            self.master.bind(seq, self.plain_movement_control)
        return

    def plain_movement_control(self, event):
        x1,y1=self.coords(self.plain)
        w=self.winfo_width()
        h=self.winfo_height()
        if event.keysym=='Right':
            if x1<w-25:
                self.move(self.plain, SPEED_OF_PLAIN,0)
                pass
        elif event.keysym=='Left':
            if x1>25:
                self.move(self.plain, -SPEED_OF_PLAIN,0)
                pass
        elif event.keysym=='Up':
            if y1>25:
                self.move(self.plain, 0,-SPEED_OF_PLAIN)
                pass
        elif event.keysym=='Down':
            if y1<h-25:
                self.move(self.plain, 0,SPEED_OF_PLAIN)
        else:
            print 'Left'
        return
        
    def create_fighter_plain_image(self):
        img=Image.open('plain2.png')
        img=img.resize((100,100))
        img=ImageTk.PhotoImage(img)
        self.storedimage1=img
        h=self.winfo_screenheight()-70
        self.plain=self.create_image(50,h, image=img)
        return

if __name__=='__main__':
    root=Tkinter.Tk(className='Fiter Plain')
    game=canvas(root, background='white')
    game.pack(expand='yes', fill='both')
    
    root.wait_visibility(root)
    #root.attributes('-alpha', 0.9)
    root.attributes('-fullscreen','true')
    
    while True:
        root.update()
        root.update_idletasks()
        game.update_loop()
        time.sleep(0.01)
