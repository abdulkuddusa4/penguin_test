from repository.routine import Routine,routine_list
from services.service import error_message



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
					error_message(['wrong input..',' enter again'])
			routine.append(dayIndex,hourIndex,courseIndex-1)
			continue
		elif cmd == 'B' or cmd == 'b':
			routine.save()
			print(routine)
			break

		elif cmd == 'C' or cmd == 'c':
			for course in Routine.courses:
				print(f'{course.courseName}, {course.teacherName}',end="\n\n\n\n")
			break

		else:
			error_message('wrong input.......')
			continue

		pass

#program starts execution from here.
if __name__ == '__main__':
	main()
