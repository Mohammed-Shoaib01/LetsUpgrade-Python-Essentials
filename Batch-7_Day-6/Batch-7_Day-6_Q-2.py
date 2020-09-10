import math
class cone:
	
	def __init__ (self):
		self.radius=int(input("Enter radius for Cone: "))
		self.height=int(input("Enter height for Cone: "))
	def volume(self):
		volumeOfCone=(math.pi*(math.pow(self.radius,2))*self.height)/3
		return volumeOfCone
	def surfaceArea(self):
		base=math.pi*(math.pow(self.radius,2))
		side=math.pi*self.radius*(math.sqrt(math.pow(self.radius,2)+math.pow(self.height,2)))
		return base+side



aCone=cone()
print("Volume of cone is: ",aCone.volume())
print("Surface Area of cone is:",aCone.surfaceArea())

'''
Output:
Enter radius for Cone: 5
Enter height for Cone: 10
Volume of cone is:  261.79938779914943
Surface Area of cone is: 254.160184615763

'''