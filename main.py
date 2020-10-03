import datetime as dt 
from collections import defaultdict
import random

class Patient:    
    def __init__(self, first_name, last_name, birth_year, symptoms):
        """
        Parameters
        ----------
        first_name : str
            as in title
        last_name : str
            as in title.
        birth_year : str
            First two digits of PESEL
        symptoms : TYPE
            as in title
            
        Returns
        -------
        None.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.symptoms = symptoms
        
        
class Doctor:
    def __init__(self, first_name, last_name, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty        
        
        
class Illness:
    def __init__(self, patient):
        self.patient = patient
        self.preliminary_specialty = None
    
    @staticmethod
    def find_words_in_sentence(words: list, sentence: str):        
        for word in words:
            if word in sentence:
                return True        
        else:
            return False
        
    def assign_symptoms_to_specialty(self):
        if dt.datetime.today().year - int(self.patient.birth_year) < 18:
            self.preliminary_specialty = "Pediatrics"
        elif self.find_words_in_sentence(
                ["heart", "veins", "infarct", "heartfailure"],
                self.patient.symptoms):
            self.preliminary_specialty = "Cardiology"
        elif self.find_words_in_sentence(
                ["rush", "skin", "burn", "tinea"],
                self.patient.symptoms):
            self.preliminary_specialty = "Dermatology"        
        elif self.find_words_in_sentence(
                ["broken", "dislocated", "swelling", "spine"],
                self.patient.symptoms):
            self.preliminary_specialty = "Orthopeadics"         
        else :
            self.preliminary_specialty = "Internists"
        return self.preliminary_specialty



class Register:
    def __init__(self, doctors: list):
        self.schedule = defaultdict()
        self.doctors = doctors
        for doc in doctors:
            self.schedule[doc.first_name + "_" + doc.last_name] = {}
        
    def add_visit(self, patient):
        doctor = self.pick_doctor(patient)
        print(doctor.first_name)
        visit_date = self.set_date()
        if visit_date in self.schedule[doctor.first_name + "_" + doctor.last_name].keys():
            print("Data zajeta")
            self.add_visit(patient)
        else:            
            self.schedule[doctor.first_name + "_" + doctor.last_name][visit_date] = patient

    def pick_doctor(self, patient: Patient):
        case = Illness(patient)
        demanded_specialty = case.assign_symptoms_to_specialty()
        for doc in self.doctors:
            if demanded_specialty == doc.specialty:
                return doc
        
    @staticmethod
    def set_date():
        visit_date_str = f"2020-10-{random.randrange(1,2)}:{random.randrange(8,15)}" # input("Zaproponuj pacjentowi date w konwencji rok-miesiac-dzien:godzina: ")
        try:
            visit_date = dt.datetime.strptime(visit_date_str,"%Y-%m-%d:%H")
        except ValueError: 
            visit_date = set_date()
        return visit_date
    
    #TODO usuniecie wizyty
 
    
#######################   
#######################         

patients = []
patients.append(Patient("Jan", "Kowal", "2002", "rush on chest")) 
patients.append(Patient("Adam", "Mada", "1980", "rush on face"))               
patients.append(Patient("Nina", "Anin", "2001", "burn on back"))               
             
patients.append(Patient("Emil", "Młynarski", "1978", "ache in heart"))   
patients.append(Patient("Krzysztof", "Fotsz", "1958", "varicose veins"))       
patients.append(Patient("Miłosz", "Szołim", "1948", "three infarcts"))       

patients.append(Patient("Joanna", "Mleczko","2015", "stomach ache"))   
patients.append(Patient("Igor", "Rogi", "2018", "stomach ache"))                 
              
patients.append(Patient("Radosław", "Rydz","1990", "dislocated knee"))          
patients.append(Patient("Mirosław", "Wasłorim","1991", "broken finger"))          

patients.append(Patient("Sylwia", "Aiwlys","2001", "stomach ache"))   
patients.append(Patient("Amelia", "Ailema", "1991", "stomach ache"))   


doctors = []
doctors.append(Doctor("Marcin", "Sercowy", "Cardiology"))               # kardiolog
doctors.append(Doctor("Sebastian", "Gróboskurny", "Dermatology"))       # dermatolog
doctors.append(Doctor("Ewa", "Mniejszo", "Pediatrics"))                 # pediatra
doctors.append(Doctor("Alicja", "Kościejna", "Orthopeadics"))           # ortopeda
doctors.append(Doctor("Andriej", "Bykow", "Internists"))           # internista




register = Register(doctors)

for patient in patients:
    register.add_visit(patient)

import pprint
pprint.pprint(register.schedule)