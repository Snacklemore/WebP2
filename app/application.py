import cherrypy
from .view import View_cl
from .TestDatabase import Database

class Application_cl(object):

    def __init__(self):
        self.database = Database("placeholder", "Mitarbeiter", "Weiterbildungen", "Qualifikation", "Zertifikat")

        self.view_o = View_cl()

    @cherrypy.expose
    def index(self, **params):
        form = params.get("index", "Startseite")
        return self.createContent_p(form)

    ''' # NEW FUNCTIONS # '''

    # Startseite

    def startseite(self):
        employee_count = self.database.change_count(self.database.employee)
        training_count = self.database.change_count(self.database.training)
        participation_count = self.database.change_participation_count()
        return self.view_o.create_startseite(employee_count, training_count, participation_count)

    ''' # Pflege Mitarbeiterdaten # '''

    def pflege_mitarbeiterdaten(self):
        employees = self.database.get_list(self.database.employee)
        return self.view_o.createContent_px(employees, "Pflege_Mitarbeiterdaten")

    @cherrypy.expose
    def show_detail_employee(self, employee_id):
        try:
            employee = self.database.get_list(self.database.employee, entry_id=employee_id, relations=True)
            return self.view_o.create_detail_pflege_mitarbeiter(employee)
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
            return self.view_o.create_detail_pflege_weiterbildungen(training)

        except (KeyError, ValueError)as error:
            print(error)

    @cherrypy.expose
    def manage_qualification_and_certificates(self, training_id):
        try:
            training = self.database.get_list(self.database.training, entry_id=training_id, relations=True, relations_true_value=False)

            certificate = []

            if training[6] is not None:
                certificate.append(self.database.get_list(self.database.certificate, entry_id=training[6]))
                certificate[0].append(training[6])

            qualification = []

            for counter, qualification_id in enumerate(training[7]):
                 qualification.append(self.database.get_list(self.database.qualification, entry_id=qualification_id))
                 qualification[counter].append(qualification_id)


            return self.view_o.create_pflege_weiterbildung_qz_verwaltung(training_id, qualification, certificate)

        except (KeyError, ValueError)as error:
            print(error)

    @cherrypy.expose
    def add_qualification(self, training_id):
        return self.view_o.create_form_add_qualification(training_id)

    @cherrypy.expose
    def add_certificate(self, training_id):
        return self.view_o.create_form_add_certificate(training_id)

    # Take custom amount of arguments
    @cherrypy.expose
    def save_qualification_and_certificate(self, **kwargs):
        qualification_ids = kwargs.get("id_qualification")
        title = kwargs.get("qualification_title")
        description = kwargs.get("qualification_description")

        if qualification_ids and title and description:
            for counter, id_ in enumerate(qualification_ids):
                self.database.edit_qualification(id_, [title[counter], description[counter]])

        certificate_id = kwargs.get("certificate_id")
        title = kwargs.get("certificate_title")
        description = kwargs.get("certificate_description")
        entitled_to = kwargs.get("certifiacte_entitled_to")

        if certificate_id and title and description and entitled_to:
            self.database.edit_certificate(certificate_id, [title, description, entitled_to])

        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")

    @cherrypy.expose
    def save_qualification(self, training_id, title, description):
        qualification = [title, description]

        qualification_id = self.database.add_qualification(qualification)
        if qualification_id is not False:
            self.database.add_qualification_to_training(qualification_id, training_id)

        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")

    @cherrypy.expose
    def save_certificate(self, training_id, title, description, entitled_to):
        certificate = [title, description, entitled_to]

        certificate_id = self.database.add_certificate(certificate)
        if certificate_id is not False:
            self.database.add_certificate_to_training(certificate_id, training_id)

        raise cherrypy.HTTPRedirect("/?index=Pflege_Weiterbildungen")

    ''' # Teilnahme # '''

    ''' # Sichtweise Mitarbeiter #'''

    def sichtweise_mitarbeiter(self):
        employee = self.database.get_list(self.database.employee)
        return self.view_o.createContent_px(employee, "Sichtweise_Mitarbeiter")

    @cherrypy.expose
    def inspect_employee_detail(self, employee_id):
        try:
            employee = self.database.get_list(self.database.employee, entry_id=employee_id, relations=True, relations_true_value=False)

            participated_training = []
            participated_training_ids = []
            not_participated_training = []

            for counter, training in enumerate(employee[4]):
                participated_training.append(self.database.get_list(self.database.training, entry_id=training[0]))

                # Add the participation status and the training id
                participated_training[counter].append(training[1])
                participated_training[counter].append(training[0])

                # Add participated training id array for comparison later
                participated_training_ids.append(training[0])

            # Filter out non participated trainings
            trainings_list = self.database.get_list(self.database.training)

            for training_id in trainings_list:
                if training_id not in participated_training_ids:
                    entry = trainings_list[training_id][0:6]
                    entry.append(training_id)
                    not_participated_training.append(entry)



            # Add employee id to the of the employee array
            employee.append(employee_id)
            return self.view_o.create_detail_employee(employee, participated_training, not_participated_training)

        except(KeyError, ValueError):
            pass

    @cherrypy.expose
    def cancel_employee_training(self, employee_id, training_id):
        if self.database.delete_employee_from_training(employee_id, training_id):
            raise cherrypy.HTTPRedirect("/inspect_employee_detail/" + employee_id)
        else:
            pass

    @cherrypy.expose
    def add_employee_to_training(self, employee_id, training_id):
        return self.view_o.create_form_add_employee_to_training(employee_id, training_id, self.database.get_participation_status_array())

    @cherrypy.expose
    def save_employee_to_training(self, employee_id, training_id, participation_status):
        if self.database.add_training_to_employee(employee_id, training_id, participation_status):
            raise cherrypy.HTTPRedirect("/inspect_employee_detail/" + employee_id)
        else:
            pass

    ''' # Sichtweise Weiterbildungen # '''

    def sichtweise_weiterbildungen(self):
        training = self.database.get_list(self.database.training)
        return self.view_o.createContent_px(training, "Sichtweise_Weiterbildungen")

    @cherrypy.expose
    def inspect_training_detail(self, training_id):
        training = self.database.get_list(self.database.training, entry_id=training_id, relations=True, relations_true_value=False)

        # Lists for employees who have/not finished the training
        finished_employees = []
        not_finished_employees = []

        # List with all the finished states of a training
        finished_participation_status = self.database.get_participation_status_array(finished=True)

        for employee in training[-1]:
            entry = self.database.get_list(self.database.employee, entry_id=employee[0])

            # Add status and id to the entry
            entry.append(employee[-1])
            entry.append(employee[0])

            # If employee has finished the training
            if employee[-1] in finished_participation_status:
                finished_employees.append(entry)

            else:
                not_finished_employees.append(entry)

        # Get no relations list and add training id
        training = self.database.get_list(self.database.training, entry_id=training_id)
        training.append(training_id)

        return self.view_o.create_from_participation_training_detail(training, finished_employees, not_finished_employees)

    # This function was used previously but is redefined here for different redirect
    @cherrypy.expose
    def cancel_employee_training_sichtweise_weiterbildung(self, employee_id, training_id):
        if self.database.delete_employee_from_training(employee_id, training_id):
            raise cherrypy.HTTPRedirect("/inspect_training_detail/" + training_id)
        else:
            pass

    ''' # Auswerung Mitarbeiter # '''

    @cherrypy.expose
    def Mitarbeiter(self):
        employee_list = self.database.get_list(self.database.employee, relations=True, relations_true_value=True)

        # Sort the dictionary by its first value(last name) -> note sorted returns a tuple
        # x = ('1', ['Hoffmann', 'Hans', ...]])
        #     x[0]  x[1][0]      x[1][1].....
        employee_list = sorted(employee_list.items(), key=lambda x:x[1][0])

        for employee in employee_list:
            # employee[1][4] = training list eg:
            # ['C++', '2020-11-30', '2020-12-24', 'C++ Anfaenger Kurs', '3000', '20', 'erfolgreich beendet'],
            # ['Python', '2020-12-10', '2020-12-25', 'Python Anfaenger Kurs', '20', '2', 'nimmt teil']
            #  x[0]         x[1]            x[2]...

            employee[1][4] = sorted(employee[1][4], key=lambda x:x[1])

        return self.view_o.create_form_auswertung_mitarbeiter(employee_list)

    ''' # Auswertung Weiterbildungen # '''

    @cherrypy.expose
    def Weiterbildungen(self):
        training_list = self.database.get_list(self.database.training, relations=True, relations_true_value=True)

        training_list = sorted(training_list.items(), key=lambda x:x[1][0])

        # Filter out successful participants
        for training in training_list:
            training[1][-1] = list(filter(lambda x:x[4] == "erfolgreich beendet", training[1][-1]))

        return self.view_o.create_form_auswertung_weiterbildung(training_list),

    ''' # Auswertung Zertifiakte # '''

    @cherrypy.expose
    def Zertifikate(self):
        certificate_list = self.database.get_list(self.database.certificate, relations=True, relations_true_value=True)

        certificate_list = sorted(certificate_list.items(), key=lambda x:x[1][0])



        return self.view_o.create_form_auswertung_zertifikat(certificate_list)

    def createContent_p(self, form):
        if form == "Pflege_Weiterbildungen":
            return self.plege_weiterbildung()
        elif form == "Pflege_Mitarbeiterdaten":
            return self.pflege_mitarbeiterdaten()
        elif form == "Sichtweise_Mitarbeiter":
            return self.sichtweise_mitarbeiter()
        elif form == "Sichtweise_Weiterbildungen":
            return self.sichtweise_weiterbildungen()
        elif form == "Startseite":
            return self.startseite()
        else:
            data_o = self.db_employee.getDefault_px()

        return self.view_o.createContent_px(data_o, form)

# TODO richtige redirects mit arbeiter oder training id machen
# TODO Wenn quali oder zert gelöscht bleibt nur noch die Id übrig wodurch früher oder später in get_list nen error kommt








