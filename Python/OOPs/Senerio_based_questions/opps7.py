'''
7. Hospital Patient Record System
Problem

Create a patient management system.

Requirements

Each patient should contain:

patient id
name
disease
doctor assigned
Functionalities
Display patient details
Change doctor
Count total patients admitted
Additional Task

Create patient from formatted string using class method.

'''
class Patient:
    total_patients = 0
    def __init__(self, patient_id, name, disease, doctor):
        self.__patient_id = patient_id
        self.__name = name
        self.__disease = disease
        self.__doctor = doctor
        Patient.total_patients += 1
    
    def display_details(self):
        print(f"Patient ID: {self.__patient_id}")
        print(f"Name: {self.__name}")
        print(f"Disease: {self.__disease}")
        print(f"Doctor Assigned: {self.__doctor}")
    
    def change_doctor(self, new_doctor):
        self.__doctor = new_doctor
        print(f"Doctor changed to {new_doctor} for patient {self.__name}.")
    
    @classmethod
    def total_patients_count(cls):
        return cls.total_patients
    
    @classmethod
    def from_string(cls, patient_str):
        patient_id, name, disease, doctor = patient_str.split(',')
        return cls(patient_id.strip(), name.strip(), disease.strip(), doctor.strip())
patient1 = Patient("P001", "John Doe", "Flu", "Dr. Smith")
patient1.display_details()
patient1.change_doctor("Dr. Adams")
print(f"Total Patients Admitted: {Patient.total_patients_count()}")
patient_str = "P002, Jane Doe, Cold, Dr. Brown"
patient2 = Patient.from_string(patient_str)
patient2.display_details()
print(f"Total Patients Admitted: {Patient.total_patients_count()}")