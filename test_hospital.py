import pytest
from hospital import *
import mysql

@pytest.fixture
def return_connection() :
    connection = pymysql.connect(host = 'localhost',
                               user = 'root', password='1234')
    return connection
        

def test_connection(return_connection) :
    
    connection = return_connection
    assert connection is not None
    print( 'connection success !' )

def test_first_query(return_connection) :
    connection = return_connection
    my_cursor = connection.cursor()
    my_cursor.execute('SELECT 1;')
    row = my_cursor.fetchone()
    assert row == (1,)
    print( 'First query Success !' )
    
def test_create_db(return_connection) :
    
    connection = return_connection
    my_cursor = connection.cursor()
    my_cursor.execute('CREATE DATABASE IF NOT EXISTS hospital;')
    my_cursor.execute('SHOW DATABASES;')
    databases = my_cursor.fetchall()
    assert ('hospital',) in databases
    print( 'Creation of the database success !' )
    my_cursor.execute('DROP DATABASE IF EXISTS test;') 

def test_doctor():
    doctor= Doctor("kadry","80","dentist")
    assert doctor.get_details()==["kadry","80","dentist"]

def test_doctor_datatype ():
    with pytest.raises(TypeError,match="this is wrong please enter the right format"):
        Doctor(111,12,1)

def test_patient():
    patient=Patient("kadry","80",35,"illness")
    assert patient.get_details_of_patient()==["kadry","80",35,"illness"]

def test_patient_datatype ():
    with pytest.raises(TypeError,match="this is wrong please enter the right format"):
        Patient(111,80,50,10)



def test_permission_error():
    db = return_connection
    with pytest.raises(PermissionError):
      DataEntryAdd.adding_record("Manager_hospital", ["kadry", "999"], db)


#def test_data_entry_search(return_connection):

#    db = DataBase()
#    doctor = Doctor("kadry","100","dentist")

#    DataEntryAdd.adding_record("Doctor_hospital", doctor.get_details(), db)
#    result = DataEntrySearch.search_records("Doctor_hospital", "id=100", db)
#    assert result == [["kadry","100","dentist"]]        

def test_prescription_create(return_connection):
    db = DataBase()
    doctor=Doctor("kadry","ll","kids")
    result = PrescriptionFactory.Prescription_create(db, "000", "lolo", "Twice a day", doctor.Name, datetime.now())

    assert "doctor kadry" in result


def test_data_entry_add(return_connection):
    db = DataBase()
    patient = Patient("kadry", "1010", 45, "Fever")
    re=DataEntryAdd.adding_record("Patient_hospital", patient.get_details_of_patient(), db)
    assert re==[]
