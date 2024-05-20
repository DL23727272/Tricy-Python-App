from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
import subprocess
import os
from database import Database  
Window.size = (368, 640)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        global sm 
        self.db = Database()
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("main.kv"))
        return sm
    
    def submit_booking(self):
        # Get user input data
        name = self.root.get_screen("main").ids.name_field.text
        address = self.root.get_screen("main").ids.address_field.text
        contact_number = self.root.get_screen("main").ids.contact_number_field.text
        pickup_area = self.root.get_screen("main").ids.pickup_area_field.text
        destination = self.root.get_screen("main").ids.destination_field.text
        num_persons = self.root.get_screen("main").ids.num_persons_field.text
        
        success = self.db.insert_booking(name, address, contact_number, pickup_area, destination, num_persons)
        
        if success:
            self.root.get_screen("main").ids.error_label.text = "Booking submitted successfully"
        else:
            self.root.get_screen("main").ids.error_label.text = "Failed to submit booking. Please try again."

        
    def go_home(self):
            subprocess.Popen(["python", "login.py"])
            os._exit(0)
   
if __name__=="__main__":
    MainApp().run()