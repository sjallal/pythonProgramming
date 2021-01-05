# class Slot:
#     def __init__(self, day, start, end):
#         self.day = day
#         self.start = start
#         self.end = end
#
#
# class Doctor:
#     def __init__(self, name, category, slot):
#         self.name = name
#         self.category = category
#         self.slot = slot

from ThoughtWorks.Doctor import Doctor
from ThoughtWorks.Slot import Slot

docs = [Doctor("docA", "PED", Slot(1, 2.0, 4.0)),
        Doctor("docB", "PED", Slot(1, 1.0, 4.0)),
        Doctor("docC", "PED", Slot(0, 1.0, 4.0)),
        Doctor("docD", "ENT", Slot(2, 1.0, 4.0)),
        Doctor("docE", "ENT", Slot(3, 1.0, 4.0)), ]

numOfPat = int(input("Enter number of Patients: "))
while numOfPat > 0:
    flag = False
    pName = input()
    category = input()
    date = input()
    day = date
    startTime = float(input())
    endTime = float(input())

    for i in range(5):
        if docs[i].category == category:
            if docs[i].slot.day == day:
                if docs[i].slot.start <= startTime and docs[i].slot.end >= endTime:
                    docs[i].slot.start = endTime
                    print("Appointment has been booked for patient " + pName + " with Doctor " + docs[
                        i].name + " for " + date + ", " + str(day) + " from " + startTime + " to " + endTime)
                    flag = True
                    break

    if not flag:
        print("No doctor available for checkup on the given date and time. Please check back with a different "
              "date/time.")

    numOfPat -= 1

"""
3
p1
PED
Jun 9,2020
2.00
2.30
p2
PED
Jun 9,2020
2.00
2.30
p3
PED
Jun 9,2020
2.00
2.30

"""
