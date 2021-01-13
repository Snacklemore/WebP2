from abc import ABCMeta, abstractmethod
from app.view import View_cl
from app.Database import Database

""" # PRAKTIKUM 3  # """
class Application(metaclass=ABCMeta):

    # Static Variables
    database = Database("database.json", "Mitarbeiter", "Weiterbildungen", "Qualifikation", "Zertifikat")
    view_o = View_cl()

    @abstractmethod
    def GET(self, **kwargs):
        pass

    @abstractmethod
    def POST(self, **kwargs):
        pass

    @abstractmethod
    def PUT(self, **kwargs):
        pass

    @abstractmethod
    def DELETE(self, **kwargs):
        pass

class Mitarbeiter(Application):

    def GET(self, employee_id=None):
        return self.database.get_list(self.database.employee, entry_id=employee_id)

    def POST(self, second_name, first_name, academic_degree, occupation):
        employee_data = [first_name, second_name, academic_degree, occupation]
        self.database.add_employee(employee_data)

    def PUT(self, employee_id ,second_name, first_name, academic_degree, occupation):
        employee_data = [first_name, second_name, academic_degree, occupation]
        self.database.edit_employee(employee_id, employee_data)

    def DELETE(self, employee_id):
        self.database.delete_employee(employee_id)

class Weiterbildung(Application):

    def GET(self, training_id=None):
        return self.database.get_list(self.database.training, entry_id=training_id)

    def POST(self, title, date_begin, date_end, description, max_attendees, min_attendees):
        new_training = [title, date_begin, date_end, description, max_attendees, min_attendees]
        self.database.add_training(new_training)

    def PUT(self, training_id, title, date_begin, date_end, description, max_attendees, min_attendees):
        new_training = [title, date_begin, date_end, description, max_attendees, min_attendees]
        self.database.edit_training(training_id, new_training)

    def DELETE(self, training_id):
        self.database.delete_training(training_id)

class Qualifikation(Application):

    def GET(self, qualifikation_id):
        return self.database.get_list(self.database.qualification, entry_id=qualifikation_id)

    def POST(self, training_id, title, description):
        qualification = [title, description]
        qualification_id = self.database.add_qualification(qualification)

        if qualification_id is not False:
            self.database.add_qualification_to_training(qualification_id, training_id)

    def PUT(self, **kwargs):
        # TODO Funktion hängt davon ab wie die Parameter hier ankommen
        pass

    def DELETE(self, qualification_id):
        self.database.delete_qualification(qualification_id)

class Zertifikat(Application):

    def GET(self, certificate_id):
        return self.database.get_list(self.database.certificate, entry_id=certificate_id)

    def POST(self, training_id, title, description, entitled_to):
        certificate = [title, description, entitled_to]
        certificate_id = self.database.add_certificate(certificate)

        if certificate_id is not False:
            self.database.add_certificate_to_training(certificate_id, training_id)

    def PUT(self, **kwargs):
        # TODO Funktion hängt davon ab wie die Parameter hier ankommen
        pass

    def DELETE(self, certificate_id):
        self.database.delete_certificate(certificate_id)

class Teilnahmen(Application):

    def GET(self):
        pass

    def POST(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass

