# Patient Class
class Patient:
    def __init__(self, name, patient_id, age, gender, diagnosis):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n***** Patient Information *****")
        print(f"ID:{self.patient_id}")    
        print(f"ID:{self.age}")    
        print(f"ID:{self.name}")    
        print(f"ID:{self.gender}")   
        print(f"ID:{self.diagnosis}")    