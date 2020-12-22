# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl

# test test
# ----------------------------------------------------------
class Application_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        # seperatie db_o objects to store employees and trainings
        self.db_employee = Database_cl("employee")
        # change add,edit,and other route functions to handle seperate trainings db
        self.db_trainings = Database_cl("trainings")
        self.db_trainingrelations = Database_cl("trainingRelations")
        self.db_employeeparticipation = Database_cl("employeeParticipations")
        self.db_certs = Database_cl("certs")
        self.db_qualifications = Database_cl("quali")
        testdata = self.db_qualifications.read_px()
        self.view_o = View_cl()
    @cherrypy.expose
    def Weiterbildungen(self, **params):
        form = params.get("nothing", "tabelle")
        return self.createAuswertung_Weiterbildung()

    def createAuswertung_Weiterbildung(self):
        data_o = self.db_trainingrelations.read_px()
        # all trainings in data_o
        training_id = []
        sorted_array = []

        # Put all id´s in one array
        for training in data_o.values():
            training_id.append(training[0])

        # Sort the array
        training_id.sort()

        # Fill the new array with ordered entries
        for id_ in training_id:
            for training in data_o.values():
                if id_ == training[0]:
                    sorted_array.append(training)
                    break

        for counter, index in enumerate(data_o):
            data_o[index] = sorted_array[counter]

        return self.view_o.createAuswertungWeiterbildung(data_o)

    @cherrypy.expose
    def Zertifikate(self):
        return self.createAuswertung_Zertifikate()

    def createAuswertung_Zertifikate(self):
        data_o = self.db_certs.read_px()

        certificate_array = []
        sorted_array = []

        for certificate in data_o.values():
            certificate_array.append(certificate[0])

        certificate_array.sort()

        # Fill the new array with ordered entries
        for id_ in certificate_array:
            for training in data_o.values():
                if id_ == training[0]:
                    sorted_array.append(training)
                    break

        for counter, index in enumerate(data_o):
            data_o[index] = sorted_array[counter]

        return self.view_o.createAusertungCerts(data_o)

    @cherrypy.expose
    def Mitarbeiter(self, **params):
        form = params.get("nothing", "tabelle")
        return self.createAuswertung_Mitarbeiter()

    def createAuswertung_Mitarbeiter(self, id_spl=None):
        # data_o = self.db_employee.read_px(id_spl)
        data_o = self.db_employeeparticipation.read_px()
        trainings = self.db_trainings.read_px()
        res = []
        temp_array = {}
        for counter, key in enumerate(data_o.values()):
            res.append(key[1])  # 1 weil 1 = Nachname
        res.sort()
        for name in res:
            for _ in data_o:
                if data_o[_][1] == name:
                    temp_array[_] = data_o[_]

        for person in temp_array.values():
            if type(person[-1]) == list:
                for training in person[-1]:
                    for trai in trainings.values():
                        if training[0] == trai[0]:
                            person[-1][person[-1].index(training)].append(trai[1])
                            person[-1][person[-1].index(training)].append(trai[2])
            else:
                person.append([])

        # Sort the dates

        for person in temp_array.values():
            sorted_trainings = []
            dates = []
            for training in person[-1]:
                dates.append(training[3])
            dates.sort()
            for date in dates:
                for training in person[-1]:
                    if training[3] == date:
                        sorted_trainings.append(training)
            person[-1] = sorted_trainings
        return self.view_o.createFormauswertungMitarbeiter(temp_array)

    @cherrypy.expose
    # -------------------------------------------------------
    def index(self, **params):
        # -------------------------------------------------------
        form = params.get("index", "Startseite")
        return self.createContent_p(form)

    @cherrypy.expose
    # -------------------------------------------------------
    def add(self, **params):
        # -------------------------------------------------------
        form = params.get("nothing", "tabelle")
        #deliver htmlform to add employee
        return self.createForm_p(listform=form)

    @cherrypy.expose
    def addtrainings(self, **params):
        form = params.get("nothing", "tabelle")
        return self.createForm_trainings(listform=form)

    @cherrypy.expose
    def showtrainingsdetail(self, id_spl, **params):
        form = params.get("index", "tabelle")

        return self.createDetail(id_spl)

    @cherrypy.expose
    def showdetailt(self, id_t, **params):
        # get the training we need details for
        training = self.db_trainingrelations.read_px(id_t)
        # get list of participants( if there is no list we dont get a list)
        # so check if participants is list
        participants = training[len(training)-1]
        if isinstance(participants, list):
            # data present

            data_o = training
            data_p = participants
            return self.view_o.createDetailTrainings(data_o, data_p)
        else:
            data_o = training
            data_p = []
            return self.view_o.createDetailTrainings(data_o, data_p)


    @cherrypy.expose
    # -------------------------------------------------------
    def edit(self, id_spl, **params):
        # -------------------------------------------------------
        listform = params.get("listform", "tabelle")
        return self.createForm_p(id_spl=id_spl, listform=listform)

    @cherrypy.expose
    def edittrainings(self, id_spl, **params):
        listform = params.get("listform", "tabelle")
        return self.createForm_trainings(id_spl=id_spl, listform=listform)

    @cherrypy.expose
    # -------------------------------------------------------
    def save(self, id_spa, name_spa, vorname_spa, akademic_spa, tatigkeit_spa, **params):
        # -------------------------------------------------------
        id_s = id_spa
        data_a = [name_spa, vorname_spa, akademic_spa, tatigkeit_spa]
        if id_s != "None":
            self.db_employee.update_px(id_s, data_a)
        else:
            self.db_employee.create_px(data_a)
        listform = params.get("listform", "tabelle")
        raise cherrypy.HTTPRedirect("/?index=Pflege_Mitarbeiterdaten")
        #return self.createContent_p(listform)

    @cherrypy.expose
    # -------------------------------------------------------
    def default(self, *arguments, **kwargs):
        # -------------------------------------------------------
        msg_s = "unbekannte Anforderung: " + \
                str(arguments) + \
                ' ' + \
                str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)

    default.exposed = True

    @cherrypy.expose
    # -------------------------------------------------------
    def delete(self, id_spl, **params):
        # -------------------------------------------------------
        listform = params.get("listform", "tabelle")
        if self.db_employee.delete_px(id_spl):
            raise cherrypy.HTTPRedirect("/?index=Pflege_Mitarbeiterdaten")
        else:
            raise cherrypy.HTTPError(500, "Existiert nicht")

    # -------------------------------------------------------
    @cherrypy.expose
    def canceltraining(self, training, employee):
        if self.db_trainingrelations.delete_employee_px(training, employee):
            raise cherrypy.HTTPRedirect("/?index=Sichtweise_Weiterbildungen")
        else:
            raise cherrypy.HTTPError(500, "Existiert nicht")

    @cherrypy.expose
    def deletetrainings(self, id_spl, **params):
        listform = params.get("listform", "tabelle")
        if self.db_trainings.delete_px(id_spl):
            raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")
        else:
            raise cherrypy.HTTPError(500, "Existiert nicht")

    def createList_p(self, listform):
        # -------------------------------------------------------
        data_o = self.db_employee.read_px()
        return self.view_o.createList_px(data_o, listform)

    # -------------------------------------------------------
    def createForm_p(self, listform, id_spl=None):
        # -------------------------------------------------------
        if id_spl != None:
            data_o = self.db_employee.read_px(id_spl)
        else:
            data_o = self.db_employee.getDefault_px()
        return self.view_o.createForm_px(id_spl=id_spl, data_opl=data_o, listform=listform)

    @cherrypy.expose
    def savetraining(self, id_spa, bezeichnung_spa, Von_spa, Bis_spa, beschreibung_spa, maxteilnehmer_spa, minteilnehmer_spa, **params):
        # -------------------------------------------------------
        id_s = id_spa
        data_a = [bezeichnung_spa, Von_spa, Bis_spa, beschreibung_spa, maxteilnehmer_spa, minteilnehmer_spa]
        if id_s != "None":
            self.db_trainings.update_px(id_s, data_a)
        else:
            self.db_trainings.create_px(data_a)
            self.db_trainingrelations.create_px(data_a)
        listform = params.get("listform", "tabelle")
        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")
        # return self.createContent_p(listform)

    def createForm_trainings(self, listform, id_spl=None):
        if id_spl != None:
            data_o = self.db_trainings.read_px(id_spl)
        else:
            data_o = self.db_trainings.getDefault_px()
        return self.view_o.createForm_trainings(id_spl=id_spl, data_opl=data_o, listform=listform)

    @cherrypy.expose
    def showdetailpflegeemploy(self, id_spl):
        # get participations of employee
        participations = self.db_employeeparticipation.read_px(id_spl)
        employeeparticipations = participations[4]
        employee = self.db_employee.read_px(id_spl)
        # get certifications of employee
        certs = self.db_certs.read_px()
        certsofemployee = []
        for key_s in certs:
            for x in certs[key_s][3]:# x[0] is the name of employee, x[2] id
                 if x[2] == id_spl:
                     certsofemployee.append(certs[key_s][0])

        data_o = employeeparticipations
        data_c = certsofemployee
        data_p = employee
        return self.view_o.createDetailPflegeMitarbeiter(data_o, data_c, data_p)

    @cherrypy.expose
    def showdetailtrainings(self, id_spl):

        training = self.db_trainingrelations.read_px(id_spl)
        teilnehmer = training[len(training) - 1]

        quali = self.db_qualifications.read_px()
        qualifizierungen = []
        for key_s in quali:
            if quali[key_s][2] == id_spl:
                qualifizierungen.append(quali[key_s][0])

        certs = self.db_certs.read_px()
        certsoftraining = []
        for key_s in certs:
            if certs[key_s][2] == id_spl:
                certsoftraining.append(certs[key_s][0])

        data_c = certsoftraining
        data_o = training
        data_p = teilnehmer
        data_b = qualifizierungen
        return self.view_o.createDetailPflegeWeiterbildungen(data_o, data_p, data_c, data_b)

    def createDetail(self, id_spl):
        # here we need to read all trainings from this employee(with the ID)

        # reading employee data
        data_o = self.db_employee.read_px(id_spl)
        data_o.append(id_spl)

        # reading training data for that employee
        data_p = self.db_trainingrelations.data_o

        # get name of employee
        name = data_o[0]
        sure_name = data_o[1]

        # arrays
        applied_trainings = []
        non_applied_trainings = []

        # for each training in database
        for training in data_p.values():
            # participants are set located in the last entry of each training
            participants = training[-1]

            participated_in_training = False

            # Check for every person whether he or she participated in the training
            for person in participants:
                if sure_name in person and name in person:
                    participated_in_training = True
                    break

            # Check the boolean and act accordingly
            if participated_in_training:
                applied_trainings.append(training)
            else:
                non_applied_trainings.append(training)

        return self.view_o.createDetail(data_o, applied_trainings, non_applied_trainings)

    def createStartSeite(self):
        # get maxID of employee
        Employe = self.db_employee.read_px()
        # get maxID of trainings
        Trainings = self.db_trainings.read_px()
        # get number of participations
        participations = self.db_employeeparticipation.read_px()
        num = 0
        for key_s in participations:
            num = num + len(participations[key_s][4])
        data_e = len(Employe)
        data_t = len(Trainings)
        data_p = num
        return self.view_o.createStartseite(data_e, data_t, data_p)

    def createContent_p(self, form):
        if form == "Pflege_Weiterbildungen":
            data_o = self.db_trainings.read_px()
        elif form == "Pflege_Mitarbeiterdaten":
            data_o = self.db_employee.read_px()
        elif form == "Sichtweise_Mitarbeiter":
            data_o = self.db_employee.read_px()
        elif form == "Sichtweise_Weiterbildungen":
            data_o = self.db_trainings.read_px()
        elif form == "Startseite":
            return self.createStartSeite()
        else:
            data_o = self.db_employee.getDefault_px()

        return self.view_o.createContent_px(data_o, form)
# EOF
