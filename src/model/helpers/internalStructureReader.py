import os

class internalStructureReader:
    file_path_internal_structure = os.path.abspath('../../../../src/model/structure/internalStructure.txt')
    def __init__(self):
        print(self.file_path_internal_structure)
        self.data = self.read_internal_structure()
        self.internal_structure_data = self.parse_internal_structure()

    def read_internal_structure(self):
        with open(self.file_path_internal_structure, 'r') as file:
            return file.read()

    def parse_internal_structure(self):
        # parse the data from the file
        lines = self.data.split('\n')
        internal_structure_data = {}
        last_key = None
        for line in lines:
            tokens = line.split()
            if tokens[0].isalpha():
                continue
            else:
                key = tokens[0]
                value = []
                for i in range(1, len(tokens)):
                    value.append(tokens[i])
                internal_structure_data[key] = value
        return internal_structure_data

    def get_internal_structure(self, tonnage, type, isBiped):
        internal_structure = {}
        data = self.internal_structure_data.get(tonnage)
        if data is None:
            raise ValueError('Invalid tonnage')
        internal_structure.update({'Head': data[2]})
        internal_structure.update({'CTorso': data[3]})
        internal_structure.update({'Torsos': data[4]})
        if isBiped:
            internal_structure.update({'Arms': data[5]})
            internal_structure.update({'Legs': data[6]})
        else:
            internal_structure.update({'Legs': data[6]})
        if type == 'Standard':
            internal_structure.update({'Mass': data[0]})
        else:
            internal_structure.update({'Mass': data[1]})

        return internal_structure