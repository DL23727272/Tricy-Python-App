from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from database import Database  
import subprocess
import os
Window.size = (368, 640)

class Login(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        
        self.db = Database()  
        
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        
        Clock.schedule_once(self.login, 5)
        
        return sm
    
    def login(self, *args):  
        self.root.current = "login" 
        
    def validate_login(self):
       
        username = self.root.get_screen("login").ids.UsernameLogin.text
        password = self.root.get_screen("login").ids.PasswordLogin.text
        
        if not username or not password:
            self.root.get_screen("login").ids.login_error_label.text = "Empty username or password"
            return
        
        if self.db.login_user(username, password):
            subprocess.Popen(["python", "main.py"])
            os._exit(0)
        else:
            self.root.get_screen("login").ids.login_error_label.text = "Invalid credentials"

    def validate_signup(self):
        username = self.root.get_screen("login").ids.Username.text
        password = self.root.get_screen("login").ids.Password.text
        check_password = self.root.get_screen("login").ids.CheckPassword.text
        
        if not username or not password or not check_password:
            self.root.get_screen("login").ids.error_label.text = "Empty username or password"
            return
        
        if password != check_password:
            self.root.get_screen("login").ids.error_label.text = "Passwords do not match"
            return
        
        signup_successful = self.db.register_user(username, password)
        if signup_successful:
            self.root.get_screen("login").ids.error_label.text = "Signup successful"
        else:
            self.root.get_screen("login").ids.error_label.text = "Username already exists"

        
    def go_home(self):
        self.root.current = "screen 1"

if __name__=="__main__":
    Login().run()
