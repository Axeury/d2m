import dicom2nifti
from dicom2nifti.exceptions import ConversionValidationError
import subprocess
import os
import sqlite3
import pydicom

def get_size(path):
    size = 0
    for x in os.listdir(path):
        if not os.path.isdir(os.path.join(path,x)):
            size += os.stat(os.path.join(path,x)).st_size
        else:
            size += get_size(os.path.join(path,x))
    return size



def d2n(path0,path_out,format,sql):
    path_dirctory0 = path0[path0.rfind('\\'):]
    try:
        os.makedirs(f'{path_out}{path_dirctory0}')
    except:
        pass
    if sql is True:
        conn = sqlite3.connect(f'{path_out}{path_dirctory0}\metadata.db') 
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE metadata(
            Patient_ID TEXT PRIMARY KEY ,
            Sex TEXT,
            Birth_Date TEXT,
            Age TEXT,
            Modality TEXT,
            Manufacturer TEXT,
            Institution_Name TEXT,
            Study_Description TEXT,
            Slice_Thickness TEXT
            )
        """)
        conn.commit()
    for path_patient in sorted(os.listdir(path0)) :
        print(path_patient)
        path_studies = os.path.join(f'{path0}\{path_patient}',os.listdir(f'{path0}\{path_patient}')[0])
        dict={}
        for study in sorted(os.listdir(path_studies)) :
            dict[study]=get_size(f"{path_studies}\{study}")
        print(f'{max(dict, key=dict.get)}')
        metadata = pydicom.filereader.dcmread(os.path.join(f'{path_studies}\{max(dict, key=dict.get)}',os.listdir(f'{path_studies}\{max(dict, key=dict.get)}')[0]))
        try :
            dicom2nifti.dicom_series_to_nifti(f'{path_studies}\{max(dict, key=dict.get)}', f'{path_out}{path_dirctory0}\{metadata.PatientID}{format}')
        except ConversionValidationError :
            print("L'inconcistence de l'incrémentation des tranches ne permet la conversion de la série en fichier nifti")
            pass
        except FileNotFoundError :
            print("Le fichier spécifié est introuvable")
            pass
        except subprocess.CalledProcessError:
            pass
        except IndexError:
            pass
        if sql is True:
            cursor.execute(f"""
            INSERT INTO metadata(Patient_ID,Sex,Birth_Date,Age,Modality,Manufacturer,Institution_Name,Study_Description,Slice_Thickness)
            VALUES('{metadata.PatientID}','{metadata.PatientSex}','{metadata.PatientBirthDate}','{metadata.PatientAge[:-1]}','{metadata.Modality}','{metadata.Manufacturer.replace(" ","_")}','{metadata.InstitutionName.replace(" ","_")}','{metadata.StudyDescription.replace(" ","_")}','{metadata.SliceThickness}') 
            """)
            conn.commit()
