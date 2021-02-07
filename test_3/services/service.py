import time

class Course:
	def __init__(self,courseIndex, courseName, teacherName):
		self.courseIndex = courseIndex
		self.courseName = courseName
		self.teacherName = teacherName

	def __str__(self):
		return f'{self.courseIndex}. {self.courseName}'


class Slot:
	def __init__(self,dayIndex,hourIndex,course):
		self.dayIndex = dayIndex
		self.hourIndex = hourIndex
		self.course = course
		pass

	def __str__(self):
		return f'{self.dayIndex} {self.hourIndex} {self.course.courseName}'


def error_message(*msgs):
	#this function will print error msg on screen
	for msg in msgs:
		print(msg)
		time.sleep(.8)
	print()

