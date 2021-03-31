import logging
import os
import zipfile
import json

# User Interface
zipf: zipfile.ZipFile = None
def init(archive_name = "Python.zip"):
    global zipf
    zipf = zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED)
def add(name: str, path: str): 
    if(zipf): zip_entity(path, zipf, name)
def finalize(): 
    if(zipf): zipf.close()


def from_iterator(archive_name, it):
    exceptions = []
    init(archive_name)
    for entity in it:
        logging.debug(f"Attempting to zip: {str(entity)}")
        try: add(*entity)
        except Exception as e: 
            logging.exception(f"Could not process entity '{entity}'")
            exceptions.append(f"Could not process entity '{entity}'")
    finalize()
    return exceptions if len(exceptions) > 0 else None




# Utils
def zip_entity(entity: str, zip_handle: zipfile.ZipFile, name_in_archive: str = None):
    name_in_archive = name_in_archive if name_in_archive else str(entity)
    if type(entity) == dict: zip_string(name_in_archive, json.dumps(entity, indent = 4, sort_keys=True), zip_handle)
    elif os.path.isdir(entity): zip_dir(entity, zip_handle)
    elif os.path.isfile(entity): zip_file(name_in_archive, entity, zip_handle)

def zip_dir(dirpath: str, zip_handle: zipfile.ZipFile):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(dirpath):
        for file in files:
           zip_handle.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(dirpath, '..')))

def zip_file(name_in_archive: str, filepath: str, zip_handle: zipfile.ZipFile): zip_handle.write(filepath, name_in_archive)
def zip_string(name_in_archive: str, data: str, zip_handle: zipfile.ZipFile): zip_handle.writestr(name_in_archive, data)




