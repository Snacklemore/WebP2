# coding: utf-8

import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup


# ----------------------------------------------------------
class View_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.lookup_o = TemplateLookup('./templates')

    def createPflegeWeiterbildungVerwaltung(self, data_certs, data_qual, t_id):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildungen_QZVerwaltung.tpl')
        markup_s = template_o.render(data_c=data_certs, data_q=data_qual, t_id=t_id)
        return markup_s
    # -------------------------------------------------------
    def createFormAddQual(self, t_id):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildungen_Qual_Add.tpl')
        markup_s = template_o.render(t_id=t_id)
        return markup_s

    def createFormAddCert(self, t_id):
        template_p = self.lookup_o.get_template('Pflege_Weiterbildungen_Certs_Add.tpl')
        markup_s = template_p.render(t_id=t_id)
        return markup_s

    def createList_px(self, data_opl, listform):
        # -------------------------------------------------------
        if listform == "tabelle":
            template_o = self.lookup_o.get_template('list.tpl')
            markup_s = template_o.render(data_o=data_opl, listform="tabelle")
        else:
            template_o = self.lookup_o.get_template('list2.tpl')
            markup_s = template_o.render(data_o=data_opl, listform="liste")
        return markup_s

    def createForm_trainings(self, id_spl, data_opl, listform):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildung_Add.tpl')
        markup_s = template_o.render(data_o=data_opl, key_s=id_spl, listform=listform)
        return markup_s

    def createAusertungCerts(self, data_o):
        template_o = self.lookup_o.get_template('Zertifikate.tpl')
        markup_s = template_o.render(data_o=data_o)
        return markup_s

    # -------------------------------------------------------
    def createForm_px(self, id_spl, data_opl, listform):
        # -------------------------------------------------------
        template_o = self.lookup_o.get_template('Pflege_Mitarbeiter_Add.tpl')
        markup_s = template_o.render(data_o=data_opl, key_s=id_spl, listform=listform)
        return markup_s
    def createDetailPflegeMitarbeiter(self, data_o, data_c, data_p):
        template_o = self.lookup_o.get_template('Pflege_Mitarbeiter_Detail.tpl')
        markup_s = template_o.render(data_o=data_o, data_c=data_c, data_p=data_p)
        return markup_s

    def createDetailPflegeWeiterbildungen(self, data_o, data_p, data_c, data_b):
        template_o = self.lookup_o.get_template('Pflege_Weiterbildung_Detail.tpl')
        markup_s = template_o.render(data_o=data_o, data_p=data_p, data_c=data_c, data_b=data_b)
        return markup_s

    # -------------------------------------------------------
    def readFile_p(self, fileName_spl):
        # -------------------------------------------------------
        content_s = ''
        with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
        return content_s

    def createDetailTrainings(self, data_o, data_p):
        template_o = self.lookup_o.get_template('Sichtweise_Weiterbildungen_Detail.tpl')
        markup_s = template_o.render(data_o=data_o, data_p=data_p)
        return markup_s

    def createFormauswertungMitarbeiter(self, data_o):
        template_o = self.lookup_o.get_template('Mitarbeiter.tpl')
        markup_s = template_o.render(data_o=data_o)
        return markup_s
    def createAuswertungWeiterbildung(self, data_o):
        template_o = self.lookup_o.get_template('Weiterbildungen.tpl')
        markup_s = template_o.render(data_o=data_o)
        return markup_s
    def createStartseite(self,data_e, data_t, data_p):
        template_o = self.lookup_o.get_template('Startseite.tpl')
        markup_s = template_o.render(data_e=data_e, data_t=data_t, data_p=data_p)
        return markup_s

    def createDetail(self, data_opl, data_t, data_p):
        template_o = self.lookup_o.get_template('Sichtweise_Mitarbeiter_Detail.tpl')
        markup_s = template_o.render(data_o=data_opl, data_t=data_t, data_p=data_p)
        return markup_s

    def createContent_px(self, data_opl, form):
        if form == "Startseite":
            template_o = self.lookup_o.get_template('Startseite.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
            return markup_s
        elif form == "Pflege_Mitarbeiterdaten":
            template_o = self.lookup_o.get_template('Pflege_Mitarbeiterdaten.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        elif form == "Pflege_Weiterbildungen":
            template_o = self.lookup_o.get_template('Pflege_Weiterbildungen.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        elif form == "Sichtweise_Mitarbeiter":
            template_o = self.lookup_o.get_template('Sichtweise_Mitarbeiter.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        elif form == "Sichtweise_Weiterbildungen":
            template_o = self.lookup_o.get_template('Sichtweise_Weiterbildungen.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        elif form == "Mitarbeiter":
            template_o = self.lookup_o.get_template('Mitarbeiter.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        elif form == "Weiterbildungen":
            template_o = self.lookup_o.get_template('Weiterbildungen.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        elif form == "Zertifikate":
            template_o = self.lookup_o.get_template('Zertifikate.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        else:
            template_o = self.lookup_o.get_template('Startseite.tpl')
            markup_s = template_o.render(data_o=data_opl, listform=form)
        return markup_s

# EOF
