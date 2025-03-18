import pytest
from hospital import *



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


