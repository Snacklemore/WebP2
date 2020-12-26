# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl
from .TestDatabase import Database

# test test
# ----------------------------------------------------------
class Application_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        # seperatie db_o objects to store employees and trainings
        self.database = Database("placeholder", "Mitarbeiter", "Weiterbildungen", "Qualifikation", "Zertifikat")
        self.db_employee = Database_cl("employee")
        #self.db_employee = Employee()
        # change add,edit,and other route functions to handle seperate trainings db
        self.db_trainings = Database_cl("trainings")
        #self.db_trainings = Training()
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
    def showtrainingsdetail(self, id_spl, **params):
        form = params.get("index", "tabelle")

        return self.createDetail(id_spl)

    @cherrypy.expose
    def showdetailt(self, id_t, **params):
        # get the training we need details for
        training = self.db_trainingrelations.read_px(id_t)
        # get list of participants( if there is no list we dont get a list)
        # so check if participants is list
        participants = training[len(training) - 1]
        if isinstance(participants, list):
            # data present

            data_o = training
            data_p = participants
            return self.view_o.createDetailTrainings(data_o, data_p)
        else:
            data_o = training
            data_p = []
            return self.view_o.createDetailTrainings(data_o, data_p)

    #@cherrypy.expose
    # -------------------------------------------------------
    def edit(self, id_spl, **params):
        # -------------------------------------------------------
        listform = params.get("listform", "tabelle")
        return self.createForm_p(id_spl=id_spl, listform=listform)

    @cherrypy.expose
    def savecert(self, t_id, bezeichnungc_spa, beschreibung_spa, berechtigung_spa):
        data_a = [bezeichnungc_spa, beschreibung_spa, t_id, berechtigung_spa]
        # id of corresponding training is missing!!
        emptylist = []
        data_a.append(emptylist)
        self.db_certs.create_px(data_a)
        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")

    @cherrypy.expose
    def savequal(self, t_id, bezeichnungq_spa, beschreibung_spa):
        data_a = [bezeichnungq_spa, beschreibung_spa, t_id]
        emptylist = []
        data_a.append(emptylist)
        self.db_qualifications.create_px(data_a)
        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")

    @cherrypy.expose
    def addQual(self, t_id, ):
        return self.view_o.createFormAddQual(t_id)

    @cherrypy.expose
    def addCert(self, t_id):
        # load form for adding cert
        return self.view_o.createFormAddCert(t_id)

    @cherrypy.expose
    def managequalicerts(self, id_spa):
        # id_spa is id of training we look at, get certs and quali of that training
        # search certs for training
        certs = self.db_certs.read_px()
        certlist = []
        quallist = []
        for key_s in certs:
            if certs[key_s][2] == id_spa:
                certlist.append(certs[key_s])
                certlist[len(certlist)-1][2] = key_s
        qual = self.db_qualifications.read_px()
        for key_m in qual:
            if qual[key_m][2] == id_spa:
                quallist.append(qual[key_m])
                quallist[len(quallist)-1][2] = key_m

        if not certlist:
            certlist
        else:
            for y in certlist:
                y.remove(y[len(y) - 1])
        if not quallist:
            quallist
        else:
            for x in quallist:
                x.remove(x[len(x)-1])
        t_id = id_spa
        return self.view_o.createPflegeWeiterbildungVerwaltung(certlist, quallist, t_id)



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
    def canceltraining(self, training, employee):
        if self.db_trainingrelations.delete_employee_px(training, employee):
            raise cherrypy.HTTPRedirect("/?index=Sichtweise_Weiterbildungen")
        else:
            raise cherrypy.HTTPError(500, "Existiert nicht")

    def createList_p(self, listform):
        # -------------------------------------------------------
        data_o = self.db_employee.read_px()
        return self.view_o.createList_px(data_o, listform)

    def createForm_trainings(self, listform, id_spl=None):
        if id_spl != None:
            data_o = self.db_trainings.read_px(id_spl)
        else:
            data_o = self.db_trainings.get_default_px()
        return self.view_o.createForm_trainings(id_spl=id_spl, data_opl=data_o, listform=listform)

    @cherrypy.expose # TODO
    def showdetailpflegeemploy(self, id_spl):
        # get participations of employee
        participations = self.db_employeeparticipation.read_px(id_spl)
        employeeparticipations = participations[4]
        employee = self.db_employee.read_px(id_spl)
        # get certifications of employee
        certs = self.db_certs.read_px()
        certsofemployee = []
        for key_s in certs:
            for x in certs[key_s][3]:  # x[0] is the name of employee, x[2] id
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

    ''' # NEW FUNCTIONS # '''

    # Startseite


    def startseite(self):
        employee_count = self.database.change_count(self.database.employee)
        training_count = self.database.change_count(self.database.training)
        participation_count = self.database.change_participation_count()
        return self.view_o.createStartseite(employee_count, training_count, participation_count)

    ''' # Pflege Mitarbeiterdaten# '''

    def pflege_mitarbeiterdaten(self):
        employees = self.database.get_list(self.database.employee)
        return self.view_o.createContent_px(employees, "Pflege_Mitarbeiterdaten")

    @cherrypy.expose
    def show_detail_employee(self, employee_id):
        try:
            employee = self.database.get_list(self.database.employee, entry_id=employee_id, relations=True)
            return self.view_o.createDetailPflegeMitarbeiter(employee)
        except (KeyError, ValueError) as error:
            print(error)

    @cherrypy.expose
    def edit_employee(self, employee_id):
        try:
            employee = self.database.get_list(self.database.employee, entry_id=employee_id)
            return self.view_o.create_form_employee(employee_id, employee)
        except (KeyError, ValueError) as error:
            pass

    @cherrypy.expose
    def add_employee(self):
        empty_employee_array = self.database.get_empty_employee_array()
        if empty_employee_array is not None:
            return self.view_o.create_form_employee(None, empty_employee_array)
        else:
            pass

    @cherrypy.expose
    def save_employee(self, employee_id, second_name, first_name, academic_degree, occupation):
        employee_data = [first_name, second_name, academic_degree, occupation]
        if employee_id == 'None':
            self.database.add_employee(employee_data)
        else:
            self.database.edit_employee(employee_id, employee_data)
        raise cherrypy.HTTPRedirect("/?index=Pflege_Mitarbeiterdaten")

    # TODO javascript fenster kommt nicht
    @cherrypy.expose
    def delete_employee(self, employee_id):
        if self.database.delete_employee(employee_id) is True:
            raise cherrypy.HTTPRedirect("/?index=Pflege_Mitarbeiterdaten")
        else:
            pass

    ''' # Pflege Weiterbildungen # '''

    def plege_weiterbildung(self):
        training = self.database.get_list(self.database.training)
        return self.view_o.createContent_px(training, "Pflege_Weiterbildungen")

    @cherrypy.expose
    def edit_training(self, training_id):
        try:
            training = self.database.get_list(self.database.training, entry_id=training_id)
            return self.view_o.create_form_training(training_id, training)
        except (KeyError, ValueError) as error:
            pass

    @cherrypy.expose
    def add_training(self):
        empty_training_array = self.database.get_empty_training_array()
        if empty_training_array is not None:
            return self.view_o.create_form_training(None, empty_training_array)
        else:
            pass

    @cherrypy.expose
    def save_training(self, training_id, title, date_begin, date_end, description, max_attendees, min_attendees):
        training_data = [title, date_begin, date_end, description, max_attendees, min_attendees]
        if training_id == 'None':
            self.database.add_training(training_data)
        else:
            self.database.edit_training(training_id, training_data)
        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")

    @cherrypy.expose
    def delete_training(self, training_id):
        if self.database.delete_training(training_id) is True:
            raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")
        else:
            pass

    @cherrypy.expose
    def show_detail_training(self, training_id):
        try:
            training = self.database.get_list(self.database.training, entry_id=training_id, relations=True, relations_true_value=True)
            return self.view_o.createDetailPflegeWeiterbildungen(training)

        except (KeyError, ValueError)as error:
            print(error)


    def show_detail_demployee(self, entry_id):
        try:
            employee = self.database.get_list(self.database.employee, entry_id=entry_id, relations=True,
                                              relations_true_value=True)
            return self.view_o.createDetailPflegeMitarbeiter(employee)
        except (KeyError, ValueError) as error:
            print(error)

    def createContent_p(self, form):
        if form == "Pflege_Weiterbildungen":
            return self.plege_weiterbildung()
        elif form == "Pflege_Mitarbeiterdaten":
            return self.pflege_mitarbeiterdaten()
        elif form == "Sichtweise_Mitarbeiter":
            data_o = self.db_employee.read_px()
        elif form == "Sichtweise_Weiterbildungen":
            data_o = self.db_trainings.read_px()
        elif form == "Startseite":
            return self.startseite()
        else:
            data_o = self.db_employee.getDefault_px()

        return self.view_o.createContent_px(data_o, form)
# EOF

# TODO Weiterbildung  Quali und Zertifikat zuweisen
# TODO Wenn quali oder zert gelöscht bleibt nur noch die Id übrig wodurch früher oder später in get_list nen error kommt

    @cherrypy.expose
    def savetraining(self, id_spa, bezeichnung_spa, Von_spa, Bis_spa, beschreibung_spa, maxteilnehmer_spa,
                     minteilnehmer_spa, **params):
        # -------------------------------------------------------
        id_s = id_spa
        data_a = [bezeichnung_spa, Von_spa, Bis_spa, beschreibung_spa, maxteilnehmer_spa, minteilnehmer_spa, []]
        if id_s != "None":
            self.db_trainings.update_px(id_s, data_a)
        else:
            self.db_trainings.create_px(data_a)
            self.db_trainingrelations.create_px(data_a)
        listform = params.get("listform", "tabelle")
        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")
        # return self.createContent_p(listform)










