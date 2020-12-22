# coding: utf-8

import os
import os.path
import codecs
import json
import copy
from . import dataid


# ----------------------------------------------------------
# commit to leon
# queries needed: Query for employee, returning trainings
# queries needed: Query
class Database_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self, dbtype):
        # -------------------------------------------------------
        self.dbtype = dbtype
        self.data_o = None
        self.maxId_o = dataid.DataId_cl(self.dbtype)
        self.readData_p()

    # -------------------------------------------------------
    def create_px(self, data_opl):
        # -------------------------------------------------------
        id_s = self.maxId_o.create_px()
        self.data_o[str(id_s)] = data_opl
        self.saveData_p()
        return str(id_s)


    # -------------------------------------------------------
    def read_px(self, id_spl=None):
        # -------------------------------------------------------
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            if id_spl in self.data_o:
                data_o = self.data_o[id_spl]
        data_o = copy.deepcopy(data_o)
        return data_o

    def getMaxID(self):
        return self.maxId_o.read_px()
    # -------------------------------------------------------
    def update_px(self, id_spl, data_opl):
        # -------------------------------------------------------
        status_b = False
        if id_spl in self.data_o:
            self.data_o[id_spl] = data_opl
            self.saveData_p()
            status_b = True
        return status_b

    # -------------------------------------------------------
    def delete_px(self, id_spl):
        # -------------------------------------------------------
        status_b = False
        if self.data_o.pop(id_spl, None) is not None:
            self.saveData_p()
            status_b = True
        return status_b

    def delete_employee_px(self, training, employee):
        # For every Training
        for key in self.data_o.values():
            # If training is equal to given training
            if key[0] == training:
                # If last entry of training is of type list
                if isinstance(key[-1], list):
                    # For every employee in training
                    for _employee in key[-1]:
                        # If employees ID is equal to the id provided
                        if _employee[3] == employee:
                            # Remove the employee from the dictionary and safe it
                            key[-1].remove(_employee)
                            self.saveData_p()
                            return True
        return False

    # -------------------------------------------------------
    def getDefault_px(self):
        # -------------------------------------------------------
        if self.dbtype == "trainings":
            return ['', '', '', '', '', '']
        elif self.dbtype == "employee":
            return ['', '', '', '']

    # -------------------------------------------------------
    def readData_p(self):
        # -------------------------------------------------------
        try:
            if self.dbtype == "trainings":
                fp_o = codecs.open(os.path.join('data', 'trainings.json'), 'r', 'utf-8')
            elif self.dbtype == "employee":
                fp_o = codecs.open(os.path.join('data', 'employee.json'), 'r', 'utf-8')
            elif self.dbtype == "trainingRelations":
                fp_o = codecs.open(os.path.join('data', 'employeetraining.json'), 'r', 'utf-8')
            elif self.dbtype == "employeeParticipations":
                fp_o = codecs.open(os.path.join('data', 'employeeparticipation.json'), 'r', 'utf-8')
            elif self.dbtype == "certs":
                fp_o = codecs.open(os.path.join('data', 'certificates.json'), 'r', 'utf-8')
            elif self.dbtype == "quali":
                fp_o = codecs.open(os.path.join('data', 'qualifications.json'), 'r', 'utf-8')


        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    # -------------------------------------------------------
    def saveData_p(self):
        # -------------------------------------------------------
        # if saving a new training, add training to employeetrainings, so employees can be added there
        if self.dbtype == "trainings":
            with codecs.open(os.path.join('data', 'trainings.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.data_o, fp_o, indent=3)
        elif self.dbtype == "employee":
            with codecs.open(os.path.join('data', 'employee.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.data_o, fp_o, indent=3)
        elif self.dbtype == "trainingRelations":
            with codecs.open(os.path.join('data', 'employeetraining.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.data_o, fp_o, indent=3)
        elif self.dbtype == "employeeParticipations":
            with codecs.open(os.path.join('data', 'employeeparticipation.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.data_o, fp_o, indent=3)
        elif self.dbtype == "certs":
            with codecs.open(os.path.join('data', 'certification.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.data_o, fp_o, indent=3)
        elif self.dbtype == "quali":
            with codecs.open(os.path.join('data', 'qualifications.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.data_o, fp_o, indent=3)





# EOF
