import cherrypy
from .view import View_cl
from .Database import Database

class Application_cl(object):

    def __init__(self):
        self.database = Database("database.json", "Mitarbeiter", "Weiterbildungen", "Qualifikation", "Zertifikat")

        self.view_o = View_cl()

    ''' # NEW FUNCTIONS # '''

    @cherrypy.expose
    def index(self):
        return self.Startseite()

    # Startseite

    @cherrypy.expose
    def Startseite(self):
        employee_count = self.database.change_count(self.database.employee)
        training_count = self.database.change_count(self.database.training)
        participation_count = self.database.change_participation_count()
        return self.view_o.create_startseite(employee_count, training_count, participation_count)

    ''' # Pflege Mitarbeiterdaten # '''

    @cherrypy.expose
    def pflege_mitarbeiterdaten(self):
        employees = self.database.get_list(self.database.employee)
        return self.view_o.create_pflege_mitarbeiter_daten(employees)

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
            return self.view_o.create_error_page(error)

    @cherrypy.expose
    def add_employee(self):
        empty_employee_array = self.database.get_empty_employee_array()
        if empty_employee_array is not None:
            return self.view_o.create_form_employee(None, empty_employee_array)
        else:
            return self.view_o.create_error_page("add_employe failed(application.py)")

    @cherrypy.expose
    def save_employee(self, employee_id, second_name, first_name, academic_degree, occupation):
        employee_data = [first_name, second_name, academic_degree, occupation]
        if employee_id == 'None':
            self.database.add_employee(employee_data)
        else:
            self.database.edit_employee(employee_id, employee_data)
        raise cherrypy.HTTPRedirect("/pflege_mitarbeiterdaten")

    # TODO javascript fenster kommt nicht
    @cherrypy.expose
    def delete_employee(self, employee_id):
        if self.database.delete_employee(employee_id) is True:
            raise cherrypy.HTTPRedirect("/pflege_mitarbeiterdaten")
        else:
            return self.view_o.create_error_page("delete_employee in application.py failed")

    ''' # Pflege Weiterbildungen # '''

    @cherrypy.expose
    def pflege_weiterbildungen(self):
        try:
            training = self.database.get_list(self.database.training)
            return self.view_o.create_pflege_weiterbildung(training)
        except(KeyError, ValueError)as error:
            return self.view_o.create_error_page(error)

    @cherrypy.expose
    def edit_training(self, training_id):
        try:
            training = self.database.get_list(self.database.training, entry_id=training_id)
            return self.view_o.create_form_training(training_id, training)
        except (KeyError, ValueError) as error:
            return self.view_o.create_error_page(error)

    @cherrypy.expose
    def add_training(self):
        empty_training_array = self.database.get_empty_training_array()
        if empty_training_array is not None:
            return self.view_o.create_form_training(None, empty_training_array)
        else:
            return self.view_o.create_error_page("add_training in application.py failed")

    @cherrypy.expose
    def save_training(self, training_id, title, date_begin, date_end, description, max_attendees, min_attendees):
        training_data = [title, date_begin, date_end, description, max_attendees, min_attendees]
        if training_id == 'None':
            self.database.add_training(training_data)
        else:
            self.database.edit_training(training_id, training_data)
        raise cherrypy.HTTPRedirect("/pflege_weiterbildungen")

    @cherrypy.expose
    def delete_training(self, training_id):
        if self.database.delete_training(training_id) is True:
            raise cherrypy.HTTPRedirect("/pflege_weiterbildungen")
        else:
            return self.view_o.create_error_page("delete_training in application.py failed")

    @cherrypy.expose
    def show_detail_training(self, training_id):
        try:
            training = self.database.get_list(self.database.training, entry_id=training_id, relations=True, relations_true_value=True)
            return self.view_o.create_detail_pflege_weiterbildungen(training)

        except (KeyError, ValueError)as error:
            return self.view_o.create_error_page(error)

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
            return self.view_o.create_error_page(error)

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
        training_id = kwargs.get("t_id", "")
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

        raise cherrypy.HTTPRedirect("/sichtweise_weiterbildungen")

    @cherrypy.expose
    def save_qualification(self, training_id, title, description):
        qualification = [title, description]

        qualification_id = self.database.add_qualification(qualification)
        if qualification_id is not False:
            self.database.add_qualification_to_training(qualification_id, training_id)

        raise cherrypy.HTTPRedirect("/manage_qualification_and_certificates/" + training_id)

    @cherrypy.expose
    def save_certificate(self, training_id, title, description, entitled_to):
        certificate = [title, description, entitled_to]

        certificate_id = self.database.add_certificate(certificate)
        if certificate_id is not False:
            self.database.add_certificate_to_training(certificate_id, training_id)

        raise cherrypy.HTTPRedirect("/manage_qualification_and_certificates/" + training_id)

    ''' # Teilnahme # '''

    ''' # Sichtweise Mitarbeiter #'''

    @cherrypy.expose
    def sichtweise_mitarbeiter(self):
        employee = self.database.get_list(self.database.employee)
        return self.view_o.create_sichweise_mitarbeiter(employee)

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

        except(KeyError, ValueError) as error:
            self.view_o.create_error_page(error)

    @cherrypy.expose
    def cancel_employee_training(self, employee_id, training_id):
        if self.database.delete_employee_from_training(employee_id, training_id):
            raise cherrypy.HTTPRedirect("/inspect_employee_detail/" + employee_id)
        else:
            self.view_o.create_error_page("cancel_employee_training in application.py failed")

    @cherrypy.expose
    def add_employee_to_training(self, employee_id, training_id):
        return self.view_o.create_form_add_employee_to_training(employee_id, training_id, self.database.get_participation_status_array())

    @cherrypy.expose
    def save_employee_to_training(self, employee_id, training_id, participation_status):
        if self.database.add_training_to_employee(employee_id, training_id, participation_status):
            raise cherrypy.HTTPRedirect("/inspect_employee_detail/" + employee_id)
        else:
            self.view_o.create_error_page("save_employee_to_training in application.py failed")

    ''' # Sichtweise Weiterbildungen # '''

    @cherrypy.expose
    def sichtweise_weiterbildungen(self):
        training = self.database.get_list(self.database.training)
        return self.view_o.create_sichtweise_weiterbildungen(training)

    @cherrypy.expose
    def inspect_training_detail(self, training_id):
        try:
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
        except(KeyError, ValueError)as error:
            return self.view_o.create_error_page(error)

    # This function was used previously but is redefined here for different redirect
    @cherrypy.expose
    def cancel_employee_training_sichtweise_weiterbildung(self, employee_id, training_id):
        if self.database.delete_employee_from_training(employee_id, training_id):
            raise cherrypy.HTTPRedirect("/inspect_training_detail/" + training_id)
        else:
            return self.view_o.create_error_page("cancel_employee_training_sichtweise_weiterbildung in application.py failed")

    ''' # Auswerung Mitarbeiter # '''

    @cherrypy.expose
    def Mitarbeiter(self):
        try:
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
        except (ValueError, KeyError)as error:
            return self.view_o.create_error_page(error)

    ''' # Auswertung Weiterbildungen # '''

    @cherrypy.expose
    def Weiterbildungen(self):
        try:
            training_list = self.database.get_list(self.database.training, relations=True, relations_true_value=True)

            training_list = sorted(training_list.items(), key=lambda x:x[1][0])

            # Filter out successful participants
            for training in training_list:
                training[1][-1] = list(filter(lambda x:x[4] == "erfolgreich beendet", training[1][-1]))

            return self.view_o.create_form_auswertung_weiterbildung(training_list)

        except (ValueError, KeyError)as error:
            return self.view_o.create_error_page(error)

    ''' # Auswertung Zertifiakte # '''

    @cherrypy.expose
    def Zertifikate(self):
        try:
            certificate_list = self.database.get_list(self.database.certificate, relations=True, relations_true_value=True)

            certificate_list = sorted(certificate_list.items(), key=lambda x:x[1][0])

            return self.view_o.create_form_auswertung_zertifikat(certificate_list)

        except (ValueError, KeyError)as error:
            return self.view_o.create_error_page(error)

# TODO richtige redirects mit arbeiter oder training id machen
# TODO Wenn quali oder zert gelöscht bleibt nur noch die Id übrig wodurch früher oder später in get_list nen error kommt








