import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color, Ellipse, Rotate
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import numpy as np




class OpenScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "openscreen"
        self.b1_pos = (Window.width/2, Window.height/2 )
        self.b2_pos = (Window.width/2, Window.height/2 )
        self.button_single = Button(text = "Single Player", font_size = 20, size_hint = (0.2,0.1))
        self.button_single.pos = (Window.width/2 - (self.button_single.size[0]/1.3), Window.height/2 -60)
        self.button_single.bind(on_release = self.change_screen_single)
        self.add_widget(self.button_single)
        self.button_double = Button(text = "Double Player", font_size = 20, size_hint = (0.2,0.1) )
        self.button_double.pos = (Window.width/2 - (self.button_double.size[0]/1.3), Window.height/2 -60 - self.button_single.size[1])
        self.button_double.bind(on_release = self.change_screen_double)
        self.add_widget(self.button_double)

        self.ellipse_width = 200
        self.ellipse_height = 200
        self.ellipse_pos_x = (Window.width- self.ellipse_width)/2
        self.ellipse_pos_y = (Window.height - self.ellipse_height)/2 + 150
        self.ellipse_pos =  (self.ellipse_pos_x, self.ellipse_pos_y)
        self.ellipse_size = (self.ellipse_width, self.ellipse_height)
        self.origin_x= self.ellipse_pos_x +self.ellipse_width/2
        self.origin_y = self.ellipse_pos_y + self.ellipse_height/2
        self.origin = (self.origin_x, self.origin_y)
        self.angle = 0
        
        with self.canvas:
            self.earth = Ellipse(source = "images/earth.png",pos = self.ellipse_pos, size = self.ellipse_size)
    

        

    def change_screen_single(self,instance):
        print("Let's Play Single!")
        app.sm.current = "playsingle"
        Clock.schedule_interval(app.update, 0)


    def change_screen_double(self, instance):
        print("Let's PLay Double!")
        app.sm.current = "playdouble"
        Clock.schedule_interval(app.update2, 0)
        


class PlaySingle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "playsingle"
    '''
    def on_enter(self):
        app.p.add_widget(app.t)
        app.p2.add_widget(app.t2)
        for i in app.single_mode:
            self.add_widget(i)
    '''
class PlayDouble(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "playdouble"
    '''
    def on_enter(self):
        app.p2.add_widget(app.t2)
        for i in app.double_mode:#iterate list of widgets and add them to player widget
            self.add_widget(i)
    '''

class End(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_size = 0
        self.label = Label(text = "You Lost", font_size = 40 )
        self.name ="end"
        self.b_pos = (Window.width/2 -30, Window.height/2 + 80)
        self.button_play_again = Button(text = "Play Again", font_size = 20, size_hint = (None,None), pos = self.b_pos)
        self.button_play_again.bind(on_release = self.play_again)
        self.add_widget(self.button_play_again)
        self.add_widget(self.label)
    
    
 
    def play_again( self, instance):
        #app.play1.clear_widgets()
        #app.play2.clear_widgets()
        #app.sm.add_widget(app.open)
        app.sm.current = "openscreen"
        
        

        

class Earth(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ellipse_width = 200
        self.ellipse_height = 200
        self.ellipse_pos_x = (Window.width- self.ellipse_width)/2
        self.ellipse_pos_y = (Window.height - self.ellipse_height)/2
        self.ellipse_pos =  (self.ellipse_pos_x, self.ellipse_pos_y)
        self.ellipse_size = (self.ellipse_width, self.ellipse_height)
        self.origin_x= self.ellipse_pos_x +self.ellipse_width/2
        self.origin_y = self.ellipse_pos_y + self.ellipse_height/2
        self.origin = (self.origin_x, self.origin_y)
        self.angle = 0
        
        with self.canvas:
            self.earth = Ellipse(source = "images/earth.png",pos = self.ellipse_pos, size = self.ellipse_size)
            
        
    def move(self, dt, key):
        step_size = dt *100
        
        if "d" in key: #self.keysPressed:
            
            self.angle += step_size
            self.canvas.clear()
            with self.canvas:
                Rotate(origin = self.origin, angle = self.angle)
                self.earth = Ellipse(source = "images/earth.png",pos = self.ellipse_pos, size = self.ellipse_size)

        if "a" in key: #self.keysPressed:
            self.angle -= step_size
            self.canvas.clear()
            with self.canvas:
                Rotate(origin = self.origin, angle = self.angle)
                self.earth = Ellipse(source = "images/earth.png",pos = self.ellipse_pos, size = self.ellipse_size)

class Earth2(Earth):
    pass

class Time(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = 0
        self.min = int(self.time/60)
        self.sec = int(self.time%60)
        self.time_display = "Time: {0}:{1}".format(self.min,self.sec)
        self.obj_size = (80,10)
        self.obj_pos_x = 10
        self.obj_pos_y = Window.height - self.obj_size[1] -10
        self.obj_pos = (self.obj_pos_x, self.obj_pos_y)

        with self.canvas:
            self.obj = Label(text = self.time_display, pos = self.obj_pos, size= self.obj_size )

    def run_time(self,dt):
        self.time += dt
        self.min = int(self.time/60)
        self.sec = int(self.time%60)
        self.time_display = "Time: {0}:{1}".format(self.min,self.sec)
        self.canvas.clear()
        with self.canvas:
            self.obj = Label(text = self.time_display, pos = self.obj_pos, size= self.obj_size )

class Time2(Time):  
    pass

    
class Obstacle(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "obstacle"
        self.angle = 0
        self.origin_x = Window.width/2
        self.origin_y =Window.height/2
        self.origin = (self.origin_x, self.origin_y)
        self.obj_size_x = 20
        self.obj_size_y = 20
        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj_size = (self.obj_size_x, self.obj_size_y)
        self.obj_pos = (self.obj_pos_x,self.obj_pos_y)

        with self.canvas:
            self.obj = Rectangle(size = self.obj_size, pos = self.obj_pos, source = "images/tree.jpg")

        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)

    def move(self, dt, key): #method to move the object when the keys are pressed
        step_size = dt *100 #step_size = 100 frames
        
        if "d" in key: 
            
            self.angle -= step_size

        if "a" in key: 
            self.angle += step_size
            
        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj.pos = (self.obj_pos_x, self.obj_pos_y)
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)
    

class Obstacle2(Obstacle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "obstacle 2"
        self.angle = 135


class Obstacle3(Obstacle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "obstacle 2"
        self.angle = 225

class Obstacle4(Obstacle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "obstacle 4"

class Obstacle5(Obstacle2):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "obstacle 5"

class Obstacle6(Obstacle3):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "obstacle 6"
    
       
class Player(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Player"
        self.origin_x = Window.width/2
        self.origin_y =Window.height/2
        self.origin = (self.origin_x, self.origin_y)
        self.obj_size = (20,20)
        self.obj_pos_x = self.origin[0] - (self.obj_size[0]/2)
        self.obj_pos_y= self.origin[1] + 100 - (self.obj_size[1]/2)
        self.obj_pos = (self.obj_pos_x, self.obj_pos_y)
        
        
        with self.canvas:
            self.obj = Ellipse(size = self.obj_size, pos = self.obj_pos, source = "images/happy.png")
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] +self.obj_size[1]/2)
    
    def move(self, dt, key):
        step_size = dt*100
        self.gravity(dt)


        if "w" in key: #self.keysPressed:
            if self.obj_pos_y <= self.origin_y + 100 - (self.obj_size[1]/2):
                self.obj_pos_y += dt*5000

        self.pos = (self.obj_pos_x, self.obj_pos_y)        
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)
  
        
    def gravity(self,dt):
        if self.obj_pos_y > self.origin_y + 100 - (self.obj_size[1]/2):
            self.obj_pos_y -= dt*100
            self.obj.pos = (self.obj_pos_x, self.obj_pos_y)

class Player2(Player):
    pass


class Chaser1(Widget): #For Single Player Mode
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Chaser red 1"
        self.origin_x= Window.width/2
        self.origin_y = Window.height/2
        self.origin = (self.origin_x, self.origin_y) 
        self.angle = 90
        self.obj_size_x = 20
        self.obj_size_y = 20
        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj_size = (self.obj_size_x, self.obj_size_y)
        self.obj_pos = (self.obj_pos_x,self.obj_pos_y)
        
        with self.canvas:
            self.obj = Ellipse(pos = self.obj_pos, size = self.obj_size, source = "images/red.jpg")
   
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)

    def move(self,dt,key): #makes chaser chase after player automatically
        step_size = dt*100
        angle = 0
        
        if "d" in key:    
            self.angle -= step_size
            
        if "a" in key:    
            self.angle += step_size
        #To automate the movement of the chaser.
        if self.angle >= 360:
            angle = self.angle%360
        elif -360 <= self.angle < 0:
            angle = self.angle+360
        elif angle < -360:
            angle = self.angle%360
        else:
            angle = self.angle
        
        if 90< angle <270:
            self.angle += step_size*0.95
        if 0 < angle <90 or 270 < self.angle%360 < 360:
            self.angle -=step_size*0.95

        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj.pos = (self.obj_pos_x, self.obj_pos_y)
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)



class Chaser2(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Chaser red 2"
        self.origin_x= Window.width/2
        self.origin_y = Window.height/2
        self.origin = (self.origin_x, self.origin_y) 
        self.angle = 90
        self.obj_size_x = 20
        self.obj_size_y = 20
        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj_size = (self.obj_size_x, self.obj_size_y)
        self.obj_pos = (self.obj_pos_x,self.obj_pos_y)
        
        with self.canvas:
            self.obj = Ellipse(pos = self.obj_pos, size = self.obj_size, source = "images/red.jpg")
   
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)


    def move(self,dt,key):
        
        step_size = dt*100
    
        if "j" in key:
            self.angle += step_size*1.1
        
        if "l" in key:
            self.angle -= step_size*1.1

        if "d" in key:    
            self.angle -= step_size
            
        if "a" in key:    
            self.angle += step_size


        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj.pos = (self.obj_pos_x, self.obj_pos_y)
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)

class Power(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Power"
        self.origin_x= Window.width/2
        self.origin_y = Window.height/2
        self.origin = (self.origin_x, self.origin_y) 
        self.angle = 45
        self.obj_size_x = 20
        self.obj_size_y = 20
        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj_size = (self.obj_size_x, self.obj_size_y)
        self.obj_pos = (self.obj_pos_x,self.obj_pos_y)
        
        with self.canvas:
            self.obj = Ellipse(pos = self.obj_pos, size = self.obj_size, source = "images/blue.png")

        self.keysPressed = set()
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)




    def move(self,dt,key):
        

        step_size = 100*dt

        if "d" in key:    
            self.angle -= step_size

        if "a" in key:    
            self.angle += step_size


        self.obj_pos_x = self.origin[0] + 100*np.sin(((90+self.angle)/180)*np.pi) - (self.obj_size_x/2)
        self.obj_pos_y = self.origin[1] + 100*np.cos(((90+self.angle)/180)*np.pi) - (self.obj_size_y/2)
        self.obj.pos = (self.obj_pos_x, self.obj_pos_y)
        self.center = (self.obj.pos[0] + self.obj_size[0]/2, self.obj.pos[1] + self.obj_size[1]/2)

class Power2(Power):
    pass

class StartApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.keysPressed = set()
        self._keyboard = Window.request_keyboard(self.on_keyboard_closed, self)
        self._keyboard.bind(on_key_down = self.on_key_down)
        self._keyboard.bind(on_key_up = self.on_key_up)
        
        #widgets
        self.g = Earth()
        self.g2 = Earth2()
        self.c1 = Chaser1()
        self.c2 = Chaser2()
        self.p = Player()
        self.p2 = Player2()
        self.o = Obstacle()
        self.o2 = Obstacle2()
        self.o3 = Obstacle3()
        self.o4 = Obstacle4()
        self.o5 = Obstacle5()
        self.o6 = Obstacle6()
        self.t = Time()
        self.t2 = Time2()

        #Screens
        self.open = OpenScreen()
        self.play1 = PlaySingle()
        self.play2 = PlayDouble()
        self.sm = ScreenManager()
        self.end = End()

        self.single_mode = [self.p, self.c1, self.o, self.o2, self.o3, self.g] #list of widgets to update for single player
        self.double_mode = [self.p2, self.c2, self.o4, self.o5, self.o6,self.g2] #list of widgets to update for single player

    def on_keyboard_closed(self):
        self.keyboard.unbind(on_key_down = self.on_key_down)
        self.keyboard.unbind(on_key_up = self.on_key_up)
        self.keyboard = None
    
    def on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)
    
 
    def on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def update(self, dt):
        key = self.keysPressed

        for i in self.single_mode:
            i.move(dt,key)
        
  
        for i in self.single_mode[1:5]:
            self.collide(self.p, i)
    
        self.t.run_time(dt)
        #self.hit_obstacle()
        #self.caught()
        self.end_game()

    def update2(self, dt):

        key = self.keysPressed

        for i in self.double_mode:
            i.move(dt,key)
        
        for i in self.double_mode[1:5]:
            self.collide(self.p2, i)

        #self.collide(self.p2, self.pow2)
        #self.collide(self.pow2, self.c2)
        #self.collide(self.p2, self.c2)
        self.t2.run_time(dt)
        #self.hit_obstacle()
        #self.caught()
        self.end_game()
        
    def end_game(self):
        if self.caught() or self.hit_obstacle():
            print("end")
            Clock.unschedule(app.update2)
            Clock.unschedule(app.update)
            self.sm.current = "end"
            
            self.remove()
            self.build_again()
            self.restart_pos()
            
            
    def restart_pos(self):
        
        self.c1.obj.pos = self.c1.obj_pos 
        self.c2.obj.pos = self.c2.obj_pos 
        self.p.obj.pos = self.p.obj_pos 
        self.p2.obj.pos = self.p2.obj_pos
        self.o.obj.pos = self.o.obj_pos 
        self.o2.obj.pos = self.o2.obj_pos 
        self.o3.obj.pos = self.o3.obj_pos  
        self.o4.obj.pos = self.o4.obj_pos  
        self.o5.obj.pos = self.o5.obj_pos 
        self.o6.obj.pos = self.o6.obj_pos  

        self.g.angle = 0
        self.g2.angle = 0
        self.c1.angle = 90
        self.c2.angle = 90
        self.p
        self.p2
        self.o.angle = 0
        self.o2.angle =135
        self.o3.angle = 225
        self.o4 = 0
        self.o5 = 135
        self.o6 = 225
        #self.t 
        #self.t2

        '''
        self.c1.center  = (self.c1.obj_pos_x + self.c1.obj_size[0]/2, self.c1.obj_pos_y + self.c1.obj_size[1]/2)
        self.c2.center = (self.c2.obj_pos_x + self.c2.obj_size[0]/2, self.c2.obj_pos_y + self.c2.obj_size[1]/2)
        self.pow.center  (self.pow.obj_pos_x + self.pow.obj_size[0]/2, self.pow.obj_pos_y+ self.pow.obj_size[1]/2)
        self.pow2.center = (self.pow2.obj_pos_x + self.pow2.obj_size[0]/2, self.pow2.obj_pos_y + self.pow2.obj_size[1]/2)
        self.p.center = (self.p.obj_pos_x + self.p.obj_size[0]/2, self.p.obj_pos_y + self.p.obj_size[1]/2)
        self.p2.center = (self.p2.obj_pos_x + self.p2.obj_size[0]/2, self.p2.obj_pos_y + self.p2.obj_size[1]/2)
        self.o.center = (self.o.obj_pos_x + self.o.obj_size[0]/2, self.o.obj_pos_y + self.o.obj_size[1]/2)
        self.o2.center  = (self.o2.obj_pos_x + self.o2.obj_size[0]/2, self.o2.obj_pos_y + self.o2.obj_size[1]/2)
        self.o3.center = (self.o3.obj_pos_x+ self.o3.obj_size[0]/2, self.o3.obj_pos_y + self.o3.obj_size[1]/2)
        self.o4.center = (self.o4.obj_pos_x + self.o4.obj_size[0]/2, self.o4.obj_pos_y + self.o4.obj_size[1]/2)
        self.o5.center =(self.o5.obj_pos_x + self.o5.obj_size[0]/2, self.o5.obj_pos_y + self.o5.obj_size[1]/2)
        self.o6.center =(self.o6.obj_pos_x + self.o6.obj_size[0]/2, self.o6.obj_pos_y + self.o6.obj_size[1]/2)
        '''
    def remove(self):
        del self.g
        del self.g2
        del self.c1
        del self.c2
        del self.p 
        del self.p2
        del self.o
        del self.o2
        del self.o3 
        del self.o4 
        del self.o5 
        del self.o6
        del self.t
        del self.t2

        

    def build_again(self):
        self.g = Earth()
        self.g2 = Earth2()
        self.c1 = Chaser1()
        self.c2 = Chaser2()
        self.p = Player()
        self.p2 = Player2()
        self.o = Obstacle()
        self.o2 = Obstacle2()
        self.o3 = Obstacle3()
        self.o4 = Obstacle4()
        self.o5 = Obstacle5()
        self.o6 = Obstacle6()
        self.t = Time()
        self.t2 = Time2()
            
            

    def collide(self, c1, c2): #check collison between arguments c1 and c2 which are widgets
        dx = c1.center[0] - c2.center[0]
        dy = c1.center[1] - c2.center[1]
        d = (dx**2 + dy**2)**0.5
        r_total = c1.obj_size[0]/2 + c2.obj_size[0]/2
        if d < r_total:
            print(c1.name + " collided with " + c2.name)
            return True

    def caught(self): #check if chaser caught player
        if self.collide(self.p, self.c1) or self.collide(self.p2, self.c2):
            print("caught!")
            return True
            
    
    def hit_obstacle(self): #check if player hit obstacle
        for i in self.single_mode[2:5]:
            if self.collide(self.p, i):
                print("hit!")
                return True
        for i in self.double_mode[2:5]:
            if self.collide(self.p2, i):
                print("hit")
                return True

    def build(self):
        
        self.sm.add_widget(self.open)
    
        self.p.add_widget(self.t)
        for i in self.single_mode[1:]:
            self.p.add_widget(i)
        
        self.p2.add_widget(self.t2)
        for i in self.double_mode[1:]:#iterate list of widgets and add them to player widget
            self.p2.add_widget(i)

    
        self.play1.add_widget(self.p)
        self.play2.add_widget(self.p2)
        self.sm.add_widget(self.play1)
        self.sm.add_widget(self.play2)
        self.sm.add_widget(self.end)

        return self.sm

if __name__ == "__main__":
    app = StartApp()
    app.run()

   