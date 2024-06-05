import os
class MechFileReader:
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        print(self.file_path)

    def read(self):
        if not self.file_path.endswith('.mtf'):
            raise ValueError('Invalid file type. Must be a MegaMek file ".mtf"')
        with open(self.file_path, 'r') as file:
            return file.read()

class BattleMech:

    def __init__(self, file_path):
        self.file_reader = MechFileReader(file_path)
        self.data = self.file_reader.read()
        self.mech_data = self.parse_data()
        self.createMech()

    def parse_data(self):
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
        self.chassis = self.mech_data['Chassis']
        self.model = self.mech_data['Model']
        self.mul_id = self.mech_data['Mul id']
        self.config = self.mech_data['Config']
        self.tech_base = self.mech_data['Techbase']
        self.era = self.mech_data['Era']
        self.source = self.mech_data['Source']
        self.role = self.mech_data['Role']
