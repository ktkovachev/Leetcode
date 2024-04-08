class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        took_this_pass = True
        while took_this_pass:
            took_this_pass = False
            for i in range(len(students)):
                student = students[0]
                sandwich = sandwiches[0]
                if student == sandwich:
                    students.popleft()
                    sandwiches.popleft()
                    took_this_pass = True
                else:
                    students.rotate(-1)
        return len(students)
