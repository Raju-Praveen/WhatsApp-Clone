from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.carousel import Carousel


class Sliding(Carousel):
	pass


class HomeScreen(MDScreen):
	individual_chat = StringProperty(None)
	
	def __init__(self, **kwargs):
		super(HomeScreen, self).__init__(**kwargs)
			
	def change_active_tab(self, start, end, *args):
		anim = Animation(start_index=start, end_index=end, d=0.2)
		anim.start(self.ids.active_tab_bar)


class CustomChat(ButtonBehavior, MDFloatLayout):
	
	def __init__(self, **kwargs):
		super(CustomChat, self).__init__(**kwargs)
		
	def on_release(self, *args):
		self.md_bg_color = (1, 1, 1, 1)


class ChatBox(MDBoxLayout):
	chatbox, box = ObjectProperty(None), int(Window.width)
	move_x, move_y = [], []
	def __init_(self, **kwargs):
		super(ChatBox, self).__init__(**kwargs)

			
class ChatsList(ScrollView):
	def __init__(self, **kwargs):
		super(ChatsList, self).__init__(**kwargs)
		self.grid_layout = GridLayout(cols=1, spacing=1, size_hint_y=None, padding=(10, 0, 10, 0))
		self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
		for i in range(50):
			self.grid_layout.add_widget(CustomChat())
			NameMessage.name = f"Praveen{i}"
		self.add_widget(self.grid_layout)


class ProfilePicture(ButtonBehavior, MDBoxLayout):
	def __init__(self, **kwargs):
		super(ProfilePicture, self).__init__(**kwargs)
		
	def on_release(self, *args):
		self.colors = (0, 1, 1, 1)
		
		
class NameMessage(ButtonBehavior, MDBoxLayout):
	def __init__(self, **kwargs):
		super(NameMessage, self).__init__(**kwargs)