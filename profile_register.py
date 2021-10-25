from kivymd.uix.screen import MDScreen


class ProfileRegister(MDScreen):
	def __init__(self, **kwargs):
		super(ProfileRegister, self).__init__(**kwargs)
		
	def change_screen(self, *args):
		self.manager.current = "home_screen"
		self.manager.transition.direction = "left"