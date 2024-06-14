import math
import os
class MechFileReader:
    def __init__(self, file_path_mech):
        self.file_path_mech = os.path.abspath(file_path_mech)
        print(self.file_path_mech)

    def read_mech_file(self):
        if not self.file_path_mech.endswith('.mtf'):
            raise ValueError('Invalid file type. Must be a MegaMek file ".mtf"')
        with open(self.file_path_mech, 'r') as file:
            return file.read()

    def read_internal_structure(self):
        pass

class BattleMech:

    def __init__(self, file_path):
        self.file_reader = MechFileReader(file_path)
        self.data = self.file_reader.read_mech_file()
        self.mech_data = self.parse_mech_data()
        self.createMech()

    def parse_mech_data(self):
        # parse the data from the file
        lines = self.data.split('\n')
        mech_data = {}
        last_key = None
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().capitalize()
                value = value.strip()
                if key in mech_data:
                    if isinstance(mech_data[key], list):
                        mech_data[key].append(value)
                    else:
                        mech_data[key] = [mech_data[key], value]
                else:
                    mech_data[key] = value
                last_key = key
            elif last_key is not None:
                mech_data[last_key] += ' ' + line.strip()
        return mech_data

    def createMech(self):
        # parse the data and create the mech
        #Basic information from the file
        self.basic_info()
        self.quirks = self.mech_data['Quirk']
        pass

    def basic_info(self):
        self.tonnage = self.mech_data['Mass']
        self.chassis = self.mech_data['Chassis']
        self.model = self.mech_data['Model']
        self.mul_id = self.mech_data['Mul id']
        self.config = self.mech_data['Config']
        self.tech_base = self.mech_data['Techbase']
        self.era = self.mech_data['Era']
        self.source = self.mech_data['Source']
        self.role = self.mech_data['Role']

    def basic_structure(self):
        self.engine = self.mech_data['Engine']
        self.structure = self.mech_data['Structure']
        self.myomer = self.mech_data['Myomer']
        self.heatsinks = self.mech_data['Heat sinks']
        self.walk = self.mech_data['Walk mp']
        self.run = math.ceil(self.walk * 1.5)
        self.jump = self.mech_data['Jump mp']
        # need a section for the internal structure


