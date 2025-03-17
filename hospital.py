from abc import ABC , abstractmethod
from datetime import datetime
import pymysql
            
class Employee (ABC):
    
    def __init__(self ,Name:str ,id:str ,Job:str)->None :
        self.Name=Name
        self.Job=Job
        self.id=id
    @abstractmethod
    def get_details(self)->str:
        pass
    
class Manager(Employee):
    def __init__(self, Name:str, id:str)->None :
        self.Name=Name
        self.id=id
        
    def get_details(self) -> str:
        return f"Manager Name ({self.Name})"
    
class Doctor (Employee):
    def __init__(self, Name:str, id:str, specialization:str)->None:
        self.specialization=specialization
        self.Name=Name
        self.idd=id
        
    def get_details(self) ->str:
        
        return f"doctor ({self.Name}) , specialization:({self.specialization}) "
    
class Patient:
    
    def __init__(self , Name:str ,id:str ,  Age:int , Ailment:str)->None:
        self.Name=Name
        self.Age=Age
        self.Ailment=Ailment
        self.id=id
        
    def get_details_of_patient (self)->str:
        return f"Patient name ({self.Name}, Age ({self.Age}), Ailment ({self.Ailment}))"
    
class DataEntry(Employee):
    def __init__(self, Name:str, Id:str)->None:
            self.connection=pymysql.connect(host="localhost",
                            user="root"
                            ,password="1234"
                            ,database="hospital1")
            self.cursor=self.connection.cursor()
            self.Name=Name
            self.Id=Id
        
    def get_details(self)->str:
        return f"Name of reception:({self.Name})"
    
class DataEntryAdd():
    @staticmethod
    def adding_record (table:str , data:list,db:DataEntry)->tuple:
        if table=="Manager_hospital":
            raise PermissionError ("you don't have access here")
        placeholders = ', '.join(['%s'] * len(data))
        
        db.cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", data)
        db.connection.commit()
        return db.cursor.fetchall()
        #self.db.connection.close()
class DataEntryDelete:
    @staticmethod
    def delete_record( table:str, record_id:str,db:DataEntry)->tuple:
            if table=="Manager_hospital":
                raise PermissionError ("you don't have access here")
            
            db.cursor.execute(f"DELETE FROM {table} WHERE id = %s", (record_id,))
            db.connection.commit()
            return db.cursor.fetchall()
            #self.db.connection.close()
class DataEntrySearch:
    @staticmethod
    def search_records(table:str, way_to_search:str,db:DataEntry)->tuple:
                if table=="Manager_hospital":
                    raise PermissionError ("you don't have access here")
                
                db.cursor.execute(f"SELECT * FROM {table} WHERE {way_to_search}")
                db.connection.commit()
                return db.cursor.fetchall()
            
class DataEntryPrintPrescription:
    @staticmethod
    def print_prescription(prescription_id:str,db:DataEntry)->tuple:
            db.cursor.execute("SELECT * FROM prescriptions WHERE id = %s", (prescription_id,))
            db.connection.commit()
            return db.cursor.fetchall()
        
class PrescriptionFactory:
    @staticmethod
    def Prescription_create(db:DataEntry,id:str,medication:str,dosage:str,doctor:str,time:datetime)->str:
        db.cursor.execute("INSERT INTO prescriptions (id, medication, dosage,doctor,date_prescribed) VALUES (%s, %s, %s, %s,%s)",
                        (id,medication, dosage,doctor,time))
        db.connection.commit()
        return f"doctor {doctor}"
        
                
                
per1=DataEntry("kadry","033")
#per1.adding_record("Patient_hospital",("kadry","108",95,"illness"),db)
#per1.adding_record("Patient_hospital",("kadry","5",6,"illness2"),db)
#per1.adding_record("Patient_hospital",("kadry","100",5,"illness1"),db)
#per1.adding_record("Patient_hospital",("mohamed","800",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","8",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","900",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","1100",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","1800",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","8100",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","8010",9,"illness0"),db)
#per1.adding_record("Patient_hospital",("mohamed","8001",9,"illness0"),db)

print(PrescriptionFactory.Prescription_create(per1,"88","lolo","8 times","kadry",datetime.now()))




