from patient import Patient

class Hospital:
    def __init__(self):
        self.patients = []

    def admit_patient(self):
        new_patient = Patient()
        self.patients.append(new_patient)

    def discharge_patient(self):
        if self.patients:
            discharged_patient = self.patients.pop()
            print(f"Patient discharged with health: {discharged_patient.health}")