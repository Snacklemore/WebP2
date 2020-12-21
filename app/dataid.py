# coding: utf-8

import os
import os.path
import codecs
import json


# ----------------------------------------------------------
class DataId_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self, dbtype):
        # -------------------------------------------------------
        self.dbtype = dbtype
        self.maxId_i = 0
        self.readMaxId_p()

    # -------------------------------------------------------
    def create_px(self):
        # -------------------------------------------------------
        self.maxId_i += 1
        self.saveMaxId_p()
        return str(self.maxId_i)

    # -------------------------------------------------------
    def read_px(self):
        # -------------------------------------------------------
        return str(self.maxId_i)

    # -------------------------------------------------------
    def readMaxId_p(self):
        # -------------------------------------------------------

        if self.dbtype == "trainings":
            try:
                fp_o = codecs.open(os.path.join('data', 'MaxIDtrainings.json'), 'r', 'utf-8')
            except:
                self.maxId_i = 0
                self.saveMaxId_p()
            else:
                with fp_o:
                    self.maxId_i = json.load(fp_o)
            return

        elif self.dbtype == "employee":
            try:
                fp_o = codecs.open(os.path.join('data', 'MaxIDemployee.json'), 'r', 'utf-8')
            except:
                self.maxId_i = 0
                self.saveMaxId_p()
            else:
                with fp_o:
                    self.maxId_i = json.load(fp_o)
            return

        elif self.dbtype == "trainingRelations":
            try:
                fp_o = codecs.open(os.path.join('data', 'MaxIDrelations.json'), 'r', 'utf-8')
            except:
                self.maxId_i = 0
                self.saveMaxId_p()
            else:
                with fp_o:
                    self.maxId_i = json.load(fp_o)
            return
        elif self.dbtype == "employeeParticipations":
            try:
                fp_o = codecs.open(os.path.join('data', 'MaxIDemployP.json'), 'r', 'utf-8')
            except:
                self.maxId_i = 0
                self.saveMaxId_p()
            else:
                with fp_o:
                    self.maxId_i = json.load(fp_o)
            return
        elif self.dbtype == "certs":
            try:
                fp_o = codecs.open(os.path.join('data', 'MaxIDcerts.json'), 'r', 'utf-8')
            except:
                self.maxId_i = 0
                self.saveMaxId_p()
            else:
                with fp_o:
                    self.maxId_i = json.load(fp_o)
            return
        elif self.dbtype == "quali":
            try:
                fp_o = codecs.open(os.path.join('data', 'qualiMaxID.json'), 'r', 'utf-8')
            except:
                self.maxId_i = 0
                self.saveMaxId_p()
            else:
                with fp_o:
                    self.maxId_i = json.load(fp_o)
            return



            # -------------------------------------------------------

    def saveMaxId_p(self):
        # -------------------------------------------------------
        if self.dbtype == "trainings":
            with codecs.open(os.path.join('data', 'MaxIDtrainings.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.maxId_i, fp_o)
        elif self.dbtype == "employee":
            with codecs.open(os.path.join('data', 'MaxIDemployee.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.maxId_i, fp_o)
        elif self.dbtype == "trainingRelations":
            with codecs.open(os.path.join('data', 'MaxIDrelations.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.maxId_i, fp_o)
        elif self.dbtype == "employeeParticipations":
            with codecs.open(os.path.join('data', 'MaxIDemployP.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.maxId_i, fp_o)
        elif self.dbtype == "certs":
            with codecs.open(os.path.join('data', 'MaxIDcerts.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.maxId_i, fp_o)
        elif self.dbtype == "quali":
            with codecs.open(os.path.join('data', 'qualiMaxID.json'), 'w', 'utf-8') as fp_o:
                json.dump(self.maxId_i, fp_o)
# EOF
