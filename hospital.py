from abc import ABC , abstractmethod
from datetime import datetime
import pymysql
from typing import Union


class DataBase:
    def __init__(self)->None:
            self.connection=pymysql.connect(host="localhost",
                            user="root"
                            ,password="1234"
                            ,database="hospital1")
            self.cursor=self.connection.cursor()
            
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
        if isinstance(Name,str) and isinstance(id,str) and isinstance(specialization,str):
             self.specialization=specialization
             self.Name=Name
             self.id=id

        else:
             raise TypeError ("this is wrong please enter the right format")
        
    def get_details(self) ->str:
        
        return [self.Name , self.id , self.specialization] 
    
class Patient:
    
    def __init__(self , Name:str ,id:str ,  Age:int , Ailment:str)->None:
        if isinstance(Name,str) and isinstance(id,str) and isinstance(Age,int) and isinstance(Ailment,str) :
              self.Name=Name
              self.Age=Age
              self.Ailment=Ailment
              self.id=id
        else:
             raise TypeError ("this is wrong please enter the right format")
        
    def get_details_of_patient (self)->list:
        return [self.Name , self.id, self.Age, self.Ailment]
    
class DataEntryAdd:
    @staticmethod
    def adding_record (table:str , data:Union [Patient,Doctor] ,db:DataBase)->tuple:
        if table=="Manager_hospital":
            raise PermissionError ("you don't have access here")
        placeholders = ', '.join(['%s'] * len(data))
        
        db.cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", data)
        db.connection.commit()
        db.connection.close()
        return db.cursor.fetchall()
        

class DataEntryDelete:
    @staticmethod
    def delete_record( table:str, record_id:int,db:DataBase)->tuple:
            if table=="Manager_hospital":
                raise PermissionError ("you don't have access here")
            
            db.cursor.execute(f"DELETE FROM {table} WHERE id = %s", (record_id,))
            db.connection.commit()
            db.connection.close()
            return db.cursor.fetchall()
            

class DataEntrySearch:
    @staticmethod
    def search_records(table:str, way_to_search:str,db:DataBase)->tuple: #db --------> Database
                if table=="Manager_hospital":
                    raise PermissionError ("you don't have access here")
                
                db.cursor.execute(f"SELECT * FROM {table} WHERE {way_to_search}")
                db.connection.commit()
                db.connection.close()
                return db.cursor.fetchall()
    
class DataEntryPrintPrescription:
    @staticmethod
    def print_prescription(prescription_id:str,db:DataBase)->tuple:
            
            db.cursor.execute("SELECT * FROM prescriptions WHERE id = %s", (prescription_id,))
            db.connection.commit()
            db.connection.close()
            return db.cursor.fetchall()
    
class DataEntry(Employee,DataEntryAdd,DataEntryDelete,DataEntrySearch,DataEntryPrintPrescription):
    def __init__(self, Name:str, Id:str)->None:
            if isinstance(Name,str) and isinstance(Id,str):
                self.Name=Name
                self.Id=Id
            else:
               raise TypeError ("this is wrong please enter the right format")
        
    def get_details(self)->str:
        return f"Name of reception:({self.Name})"
    

    
class PrescriptionFactory:
    @staticmethod
    def Prescription_create(db:DataBase,id:str,medication:str,dosage:str,doctor:str,time:datetime)->str:
        db.cursor.execute("INSERT INTO prescriptions (id, medication, dosage,doctor,date_prescribed) VALUES (%s, %s, %s, %s,%s)",
                        (id,medication, dosage,doctor,time))
        db.connection.commit()
        return f"doctor {doctor}"
                        
#db=DataBase()
#per1=DataEntry("kadry","033")
#pa1=Patient("name","1100",66,"illness")
#doc1=Doctor("uu",'12',"feet")

#DataEntry.adding_record("Patient_hospital", pa1.get_details_of_patient()  ,db)
#print(DataEntry.search_records("Patient_hospital","id=10000",db))
#DataEntry.delete_record("Patient_hospital",1100,db)
#PrescriptionFactory.Prescription_create(db,"10","hemoclar","3 times daily",doc1.Name,datetime.now())
#print(DataEntry.print_prescription("10",db))




