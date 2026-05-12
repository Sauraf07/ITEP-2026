'''
6. Hospital Management
Parent:
HospitalStaff
Child:
Doctor
Nurse
Receptionist
Implement duties().
'''
class HospitalStaff:
    def duties(self):
        pass
class Doctor(HospitalStaff):
    def duties(self):
        print("Diagnose and treat patients.")
class Nurse(HospitalStaff):
    def duties(self):
        print("Assist doctors and care for patients.")
class Receptionist(HospitalStaff):
    def duties(self):
        print("Manage appointments and patient records.")

d = Doctor()
d.duties()  
n = Nurse()
n.duties()
r = Receptionist()
r.duties()

