import pydicom
import os

path='F:\BIBLIOTHEQUE BASSIN DICOM\BASSIN DEGENERATIF\Beauvais_Chantal\Bassin - 31295\Bassin_Os_2'
print(os.listdir('F:\BIBLIOTHEQUE BASSIN DICOM\BASSIN DEGENERATIF\Bernard_Chantal\Bassin - 20545\OS_2')[0])
ds = pydicom.filereader.dcmread(os.path.join(path,os.listdir(path)[0]))
cc = ds

print(f'''
Name : {type(cc.PatientName)}
ID : {type(cc.PatientID)}
Sex : {type(cc.PatientSex)}
Birth_Date : {type(cc.PatientBirthDate)}
Age : {type(cc.PatientAge[:-1])}
Modality : {type(cc.Modality)}
manufacturer : {type(cc.Manufacturer.replace(" ","_"))}
Institution_Name : {type(cc.InstitutionName.replace(" ","_"))}
Study_Description : {type(cc.StudyDescription.replace(" ","_"))}
Slice_Thickness : {type(float(cc.SliceThickness))}

''')

# dicom2nifti.dicom_series_to_nifti('D:\Data dicom\\28251\study\OS', 'D:\Data dicom\out\\28251.nii')



# conn = sqlite3.connect('D:\out\metadata.db') 
# cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE metadata(
#      Patient_ID INTEGER PRIMARY KEY ,
#      Sex TEXT,
#      Birth_Date TEXT,
#      Age TEXT,
#      Modality TEXT,
#      Manufacturer TEXT,
#      Institution_Name TEXT,
#      Study_Desciprion TEXT,
#      Slice_Thickness TEXT
# )
# """)
# conn.commit()