"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. 
All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. 
At each step:

    - If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    - Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in 
the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial 
queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""

class Solution(object):

    students = []
    sandwiches = []
    
    """
    init(self, students, sandwiches):
        self.students = students
        self.sandwiches = sandwiches
    """

    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        
        # students are in a QUEUE
        # sandwiches are un a STACK
        
        # If the next student prefers the sandwich that is on the TOP of the stack, they take it and leave
        # Else, the student goes back to the end of the queue (doesn't take the sandwich)
        # Sandwiches DON'T ROTATE

        # When none of the remaining students are able to eat, return the num of students remaining


        # Have a function to send students to the back of the queue

        # Function to check if the next student wants the next sandwich

        # Something need to track the students sent to the back of the queue
        # make sure you stop checking if there's no more options for them

        # Function to remove happy student and correct sandwich from arrays


        # send students to the back of the queue
    def sendStudentToTheEnd(self, studentIndex):
        stundet = self.students.pop(studentIndex)
        self.students.append(stundet)


# TESTING
s = Solution()
s.sandwiches = [1, 2, 3, 4]
s.students = [1, 2, 3, 4]
print(f"\nOriginal Students: {s.students}\n")

s.sendStudentToTheEnd(1)
print(s.students)