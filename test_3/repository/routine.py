from services.service import Course,Slot

routine_list = []

class Routine:
	courses = [
	 Course(1, 'English Grammar', 'John Smith'),
	 Course(2, 'Mathematics', 'Lara Gilbert'),
	 Course(3, 'Physics', 'Johanna Kabir'),
	 Course(4, 'Chemistry', 'Danniel Robertson'),
	 Course(5, 'Biology', 'Larry Cooper'),
	]

	def __init__(self):
		self.slots=[]

	def append(self,dayIndex,hourIndex,courseIndex):
		newSlot = Slot(dayIndex,hourIndex,self.courses[courseIndex-1])
		self.slots.append(newSlot)

	def __str__(self):
		st = ''
		for slot in self.slots:
			st+=str(slot)+'\n'
		st+='\n\n'
		return st

	def printCourses():
		for course in Routine.courses:
			print(course)

	def save(self):
		routine_list.append(self)