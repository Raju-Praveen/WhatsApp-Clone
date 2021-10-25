from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from welcome_screen import WelcomeScreen
from phone_number_screen import PhoneNumberScreen
from profile_register import ProfileRegister
from home_screen import HomeScreen


class Main(MDApp):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(WelcomeScreen(name="welcome_screen"))
		sm.add_widget(HomeScreen(name="home_screen"))
		sm.add_widget(ProfileRegister(name="profile_register"))
		sm.add_widget(PhoneNumberScreen(name="phone_number_screen"))
		sm.add_widget(WelcomeScreen(name="welcome_screen"))
		
		return sm
		
		
if __name__ == "__main__":
	Main().run()