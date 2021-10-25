from kivymd.uix.screen import MDScreen


class WelcomeScreen(MDScreen):
	def __init__(self, **kwargs):
		super(WelcomeScreen, self).__init__(**kwargs)
		
	def change_screen(self, *args):
		self.manager.current = "phone_number_screen"
		self.manager.transition.direction = "left"