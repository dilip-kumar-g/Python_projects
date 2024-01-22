
'''
## Problem Statement##

 Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume.
 Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default
 Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
 Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel
 Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor)
 
 Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV

'''



class Tv:

	def __init__(self,brand):
		self.brand = brand
		self.channel_no = 1
		self.volume = 50
		self.on_off_status = True
		self.price = '$250'
		self.inches = 43
		self.reset_tv()


	def increase_volume(self):
		if self.volume < 100:
			self.volume += 1

	def decrease_volume(self):
		if self.volume > 0:
			self.volume -= 1

	def set_channel_no(self,channel_no):
		if 0 < channel_no <= 50:
			self.channel_no = channel_no

	def reset_tv(self):
		self.channel_no = 1
		self.volume = 50

	def tv_status(self):
		return "{self.brand} is at channel_no {self.channel_no}, volume {self.volume}"


class LED(Tv):

	def __init__(self,brand,screen_thickness,energy_usage,lifespan,display_details):
		super().__init__(brand)
		self.screen_thickness = screen_thickness
		self.energy_usage = energy_usage
		self.lifespan = lifespan
		self.display_details = display_details

	def tv_status(self):
		return f"{self.brand} is at channel_no: {self.channel_no}, volume: {self.volume}, lifespan: {self.lifespan}, energy_usage: {self.energy_usage}"

class Plasma(Tv):

	def __init__(self,brand,screen_thickness,energy_usage,lifespan,display_details,viewing_angle,refresh_rate):
		super().__init__(brand)
		self.screen_thickness = screen_thickness
		self.energy_usage = energy_usage
		self.lifespan = lifespan
		self.display_details = display_details
		self.viewing_angle = viewing_angle
		self.refresh_rate = refresh_rate

	def tv_status(self):
		return f"{self.brand}"



	def tv_status(self):
		return 




if __name__ == "__main__":

	led_tv = LED("SONY",31,0.5,"5 yrs","40W")
	print(led_tv.tv_status())

'''
 Created a TV class with properties like brand, channel , price , inches , OnOFF status and volume in the parent class constructor 

added methods in parent class to set volume, set channel and reset status and the status 

created child classes named LED and plass and Inherited the constructor and used the attributes present in them

'''