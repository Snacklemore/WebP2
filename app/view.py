import codecs
import os.path

from mako.lookup import TemplateLookup


class View_cl(object):

    def __init__(self):
        self.lookup_o = TemplateLookup('./templates')

    def create_form_add_qualification(self, training_id):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildung_Qualification_Add.tpl')
        markup_s = template_o.render(t_id=training_id, listform="Pflege_Weiterbildungen_QZVerwaltung")
        return markup_s

    def create_form_add_certificate(self, training_id):
        template_p = self.lookup_o.get_template('Pflege_Weiterbildungen_Certificate_Add.tpl')
        markup_s = template_p.render(t_id=training_id, listform="Pflege_Weiterbildungen_QZVerwaltung")
        return markup_s

    def create_form_training(self, training_id, training_data):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildung_Add.tpl')
        markup_s = template_o.render(data_o=training_data, key_s=training_id, listform='Pflege_Weiterbildung')
        return markup_s

    def create_form_employee(self, employee_id, employee_data):
        template_o = self.lookup_o.get_template("Pflege_Mitarbeiter_Add.tpl")
        markup_s = template_o.render(data_o=employee_data, key_s=employee_id, listform="Pflege_Mitarbeiter")
        return markup_s

    def create_pflege_weiterbildung_qz_verwaltung(self, training_id, qualifications, certificates):
        template_o = self.lookup_o.get_template("Pflege_Weiterbuldung_QZ_Verwaltung.tpl")
        markup_s = template_o.render(data_o=qualifications, data_t=certificates, t_id=training_id, listform="Pflege_Weiterbildung")
        return markup_s

    def create_detail_pflege_mitarbeiter(self, data_o):
        template_o = self.lookup_o.get_template('Pflege_Mitarbeiter_Detail.tpl')
        markup_s = template_o.render(data_o=data_o)
        return markup_s

    def create_detail_pflege_weiterbildungen(self, data_o):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildung_Detail.tpl')
        markup_s = template_o.render(data_o=data_o)
        return markup_s

    def create_form_auswertung_mitarbeiter(self, employee):
        template_o = self.lookup_o.get_template('Mitarbeiter.tpl')
        markup_s = template_o.render(employee=employee)
        return markup_s

    def create_form_auswertung_weiterbildung(self, training):
        template_o = self.lookup_o.get_template('Weiterbildungen.tpl')
        markup_s = template_o.render(training=training)
        return markup_s

    def create_form_auswertung_zertifikat(self, certificate):
        template_o = self.lookup_o.get_template('Zertifikate.tpl')
        markup_s = template_o.render(certificate=certificate)
        return markup_s

    def create_startseite(self,data_e, data_t, data_p):
        template_o = self.lookup_o.get_template('Startseite.tpl')
        markup_s = template_o.render(data_e=data_e, data_t=data_t, data_p=data_p)
        return markup_s

    def create_detail_employee(self, employee, participated_training, non_participated_training):
        template_o = self.lookup_o.get_template('Sichtweise_Mitarbeiter_Detail.tpl')
        markup_s = template_o.render(data_o=employee, data_t=participated_training, data_p=non_participated_training)
        return markup_s

    def create_form_add_employee_to_training(self, employee_id, training_id, participation_status):
        template_o = self.lookup_o.get_template('Sichtweise_Mitarbeiter_Add_Training.tpl')
        markup_s = template_o.render(data_o=employee_id, data_t=training_id, data_p=participation_status)
        return markup_s

    def create_from_participation_training_detail(self, training_id, finished_employees, not_finished_employees):
        template_o = self.lookup_o.get_template('Sichtweise_Weiterbildungen_Detail.tpl')
        markup_s = template_o.render(training=training_id, finished_employees=finished_employees, not_finished_employees=not_finished_employees)
        return markup_s

    def create_pflege_mitarbeiter_daten(self, employees):
        template_o = self.lookup_o.get_template('Pflege_Mitarbeiterdaten.tpl')
        markup_s = template_o.render(data_o=employees)
        return markup_s

    def create_pflege_weiterbildung(self, trainings):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildungen.tpl')
        markup_s = template_o.render(data_o=trainings)
        return markup_s

    def create_sichweise_mitarbeiter(self, employee):
        template_o = self.lookup_o.get_template('Sichtweise_Mitarbeiter.tpl')
        markup_s = template_o.render(data_o=employee)
        return markup_s

    def create_sichtweise_weiterbildungen(self, training):
        template_o = self.lookup_o.get_template('Sichtweise_Weiterbildungen.tpl')
        markup_s = template_o.render(data_o=training)
        return markup_s

    def create_error_page(self, error_msg):
        template_o = self.lookup_o.get_template('Error.tpl')
        markup_s = template_o.render(data_o=error_msg)
        return markup_s