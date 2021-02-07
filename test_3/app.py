from repository.routine import Routine
from services.service import error_message
from termcolor import colored



def main():
	routine = Routine()
	while True:
		msg = "A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name\n\n"
		print(msg)
		cmd = str(input())
		if cmd == 'A' or cmd == 'a':
			Routine.printCourses()
			while True:
				try:
					dayIndex, hourIndex, courseIndex = map(int,input().split(sep=' '))
					break
				except:
					error_message(['wrong input..',' try again'])
			routine.append(dayIndex,hourIndex,courseIndex-1)
			continue
		elif cmd == 'B' or cmd == 'b':
			routine.save()
			print(colored(routine,'blue'))
			break

		elif cmd == 'C' or cmd == 'c':
			for course in Routine.courses:
				print(colored(f'{course.courseName}, {course.teacherName}','green'),end="\n\n")
			break

		else:
			error_message(['wrong input.......','try again'])
			continue

		pass

#program starts execution from here.
if __name__ == '__main__':
	main()
