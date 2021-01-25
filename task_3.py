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

class Routine:
	courses = [
	 Course(1, 'English Grammar', 'John Smith'),
	 Course(2, 'Mathematics', 'Lara Gilbert'),
	 Course(2, 'Physics', 'Johanna Kabir'),
	 Course(3, 'Chemistry', 'Danniel Robertson'),
	 Course(4, 'Biology', 'Larry Cooper'),
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
		return st

	def printCourses():
		for course in Routine.courses:
			print(course)

def main():
	routine = Routine()
	while True:
		msg = "A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name"
		print(msg)
		cmd = str(input())
		if cmd == 'A' or cmd == 'a':
			Routine.printCourses()
			while True:
				try:
					dayIndex, hourIndex, courseIndex = map(int,input().split(sep=' '))
					break
				except:
					print('wrong input.. enter again')
			routine.append(dayIndex,hourIndex,courseIndex)
			continue
		if cmd == 'B' or cmd == 'b':
			print(routine)
			break
		if cmd == 'C' or cmd == 'c':
			for course in Routine.courses:
				print(f'{course.courseName}, {course.teacherName}')
			break
		else:
			print('wrong input.......')
			continue

		pass

if __name__ == '__main__':
	main()
