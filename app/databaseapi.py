import json
import codecs
import os
import copy

class Database:

    # Constructor

    def __init__(self, database_file, data_id_file):
        self.data_id_file = data_id_file
        self.database_file = database_file
        self.data_o = {}
        self.maxId_i = 0
        self.read_max_id_p()
        self.read_data_o()

    # MAX ID Functions

    def create_data_id(self):
        self.maxId_i += 1
        self.save_max_id()
        return str(self.maxId_i)

    def save_max_id(self):
        with codecs.open(os.path.join("data", self.data_id_file), 'w', "utf-8") as file:
            json.dump(self.maxId_i, file)

    def read_max_id_p(self):
        try:
            with codecs.open(os.path.join('data', self.data_id_file), 'r', 'utf-8')as file:
                self.maxId_i = json.load(file)
        except (FileNotFoundError, PermissionError):
            self.maxId_i = 0
            self.save_max_id()

    def get_max_id(self):
        return str(self.maxId_i)

    # DATABASE Functions

    def read_px(self, id_spl=None):
        if id_spl is None:
            return copy.deepcopy(self.data_o)
        else:
            if id_spl in self.data_o:
                return copy.deepcopy(self.data_o[id_spl])

    def create_px(self, data_opl):
        id_s = self.create_data_id()
        self.data_o[id_s] = data_opl
        self.save_data_o()
        return id_s

    def update_px(self, id_spl, data_opl):
        if id_spl in self.data_o:
            self.data_o[id_spl] = data_opl
            self.save_data_o()
            return True
        return False

    def delete_px(self, id_spl):
        try:
            self.data_o.pop(id_spl)
            self.save_data_o()
            return True
        except KeyError:
            return False

    def save_data_o(self):
        with codecs.open(os.path.join("data", self.database_file), 'w', "utf-8")as file:
            json.dump(self.data_o, file, indent=3)

    def read_data_o(self):
        try:
            with codecs.open(os.path.join("data", self.database_file), 'r', "utf-8") as file:
                self.data_o = json.load(file)
        except (FileNotFoundError, PermissionError):
            self.data_o = {}
            self.save_data_o()

    # Virtual Methods

    def get_default_px(self):
        pass

    def delete_employee(self, id_spl):
        pass

    def delete_training(self, id_spl):
        pass

# Employee Class

class Employee(Database):

    def __init__(self, database_file="employee.json", data_id_file="MaxIDemployee.json"):
        super().__init__(database_file, data_id_file)

    def get_default_px(self):
        return ['', '', '', '']

    def delete_employee(self, id_spl):
        return self.delete_px(id_spl)

# Trainings Class

class Training(Database):

    def __init__(self, database_file="trainings.json", data_id_file="MaxIDtrainings.json"):
        super().__init__(database_file, data_id_file)

    def get_default_px(self):
        return ['', '', '', '', '', '']

    def delete_training(self, id_spl):
        return self.delete_px(id_spl)

class Certificates(Database):

    def __init__(self, database_file="certificates.json", data_id_file="MaxIDcerts.json"):
        super().__init__(database_file, data_id_file)

    def delete_employee(self, id_spl):
        passed = False
        # For every certificate in the database
        for certificate in self.data_o:
            # for every employee in a certificate
            for employee in self.data_o[certificate][-1]:
                # If employee in database matches given employee remove it
                if employee is id_spl:
                    certificate[-1].remove(employee)
                    passed = True
                    # Break to loop over the next certificate
                    break

        return passed

    def delete_training(self, id_spl):
        # For every certificate in the database
        for certificate in self.data_o:
            # If Trainings ID matches given ID then set it to
            if self.data_o[certificate][2] is id_spl[4]:
                # -1 stands for Training no longer exists
                # Certificate is not deleted because someone could already own it even tho the training was deleted
                self.data_o[certificate][2] = "-1"

    def delete_certificate(self, id_spl):
        return self.delete_px(id_spl)












































