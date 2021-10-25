from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class VerifyNumber(MDBoxLayout):
	pass


class PhoneNumberScreen(MDScreen):
	dialog = None
	def verify_phone_dialog(self, *args):
		if not self.dialog:
			self.dialog = MDDialog(title="Verify", type="custom", content_cls=VerifyNumber(), buttons=[MDFlatButton(text="EDIT", theme_text_color="Custom", text_color=(32/255, 198/255, 90/255, 1)), MDFlatButton(text="OK", theme_text_color="Custom", text_color=(32/255, 198/255, 90/255, 1), on_release=self.change_screen)])
		self.dialog.open()
		
	def change_screen(self, *args):
		self.manager.current = "profile_register"
		self.manager.transition.direction = "left"
	
	
class CountryName(ButtonBehavior, MDFloatLayout):
	name = None
	def __init__(self, **kwargs):
		super(CountryName, self).__init__(**kwargs)
		self.name = "India"
		
	def change_name(self):
		self.name = "Australia"