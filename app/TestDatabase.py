import json
import codecs
import os
import copy
import string

class Database:

    # Constructor

    def __init__(self, database_file_path):

        # Variables
        self.json_file_path = database_file_path
        self.main_data = None

        # Init Functions
        self.read_json_file()

    '''# JSON file methods #'''

    def read_json_file(self):
        try:
            #file = codecs.open(os.path.join('data', self.json_file_path), 'r', 'utf-8')
            file = codecs.open("F:\web\WEBP2\data\database.json", "r", "utf-8")
            try:
                self.main_data = json.load(file)
            finally:
                file.close()
        except (FileNotFoundError, PermissionError):
            # Raise an error if database file could not be opened
            raise Exception("[!] JSON DATABASE FILE NOT FOUND")

    def write_json_file(self):
        if self.main_data is not None:
            try:
                #file = codecs.open(os.path.join('data', self.json_file_path), 'w', 'utf-8')
                file = codecs.open("F:\web\WEBP2\data\database.json", "w", "utf-8")
                try:
                    json.dump(self.main_data, file, indent=3)
                finally:
                    file.close()
            except (FileNotFoundError, PermissionError):
                # Raise an error if database file could not be opened
                raise Exception("[!] JSON DATABASE FILE NOT FOUND")

    '''# Database methods #'''

    # Private -> only used by class internal methods
    def __get_list(self, dict_name, entry_id=None):
        # Get list_name dictionary entry
        data = self.main_data.get(dict_name)
        if data:
            data = data.get("List")
            if data:
                if entry_id:
                   data = data.get(entry_id)

        # Raise an exception if function fails -> easier to filter out errors in calling functions
        if data is None:
            raise KeyError
        # Notice that data is a REFERENCE to the dictionary
        return data

    def get_list(self, dict_name, entry_id=None):
        # Get list_name dictionary entry
        data = self.main_data.get(dict_name)
        if data:
            data = data.get("List")
            if data:
                if entry_id:
                   data = data.get(entry_id)

        # Raise an exception if function fails -> easier to filter out errors in calling functions
        if data is None:
            return None
        # Notice that data is a REFERENCE to the dictionary
        return copy.deepcopy(data)

    # Increases max_id by one and returns new value
    def raise_max_id(self, dict_name):
        # Get employees dictionary entry
        employees = self.main_data.get(dict_name)
        if employees:
            max_id = employees.get("Max-ID")
            if max_id:
                max_id = int(max_id) + 1
                employees["Max-ID"] = str(max_id)
                return str(max_id)
        raise KeyError

    # Method changes count and returns it
    # If amount = 0 only returns the count
    def change_count(self, list_name, amount=0):
        employees = self.main_data.get(list_name)
        if employees:
            count = employees.get("Count")
            if count:
                count = int(count) + amount
                employees["Count"] = str(count)
                return str(count)
        raise KeyError

    '''# General employee methods #'''

    # Method to add new employee | it is assumed that the employee has no trainings, qualifications and certificates
    def add_employee(self, new_employee):
        try:
            employee_id = self.raise_max_id("Mitarbeiter")
            employee_list = self.__get_list("Mitarbeiter")
            self.change_count("Mitarbeiter", amount=1)

            # Append 3 empty list for trainings, qualifications and certificates
            for _ in range(0, 3):
                new_employee.append([])

            employee_list[employee_id] = new_employee
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    def delete_employee(self, employee_id):
        try:
            employee_list = self.__get_list("Mitarbeiter")

            # Get a Value copy of the list because delete_employee_from_training() will change the list
            # which would manipulate the for loop
            employee = copy.deepcopy(self.__get_list("Mitarbeiter", entry_id=employee_id))

            # Delete employee from training
            for training_id in employee[4]:
                self.delete_employee_from_training(employee_id, training_id)

            # Delete employee from qualifications
            for qualification_id in employee[5]:
                self.remove_employee_from_qualification(qualification_id, employee_id)

            # Delete employee from certificates
            for certificate_id in employee[6]:
                self.remove_employee_from_certificate(certificate_id, employee_id)

            employee_list.pop(employee_id)
            self.change_count("Mitarbeiter", amount=-1)
            self.write_json_file()

        except KeyError:
            return False
        else:
            return True

    # This function only edits the employee properties not the references to other objects
    def edit_employee(self, employee_id, changed_employee):
        try:
            employee_list = self.__get_list("Mitarbeiter")

            for i in range(0, 4):
                employee_list[employee_id][i] = changed_employee[i]

            self.write_json_file()

        except KeyError:
            return False
        else:
            return True

    '''# Employee Training methods #'''

    # Adds a training to one employee and checks if it was successful finished
    def add_training_to_employee(self, employee_id, training_id, employee_participation_status):
        try:
            employee = self.__get_list("Mitarbeiter", entry_id=employee_id)
            employee[4].append(training_id)

            training = self.__get_list("Weiterbildungen", entry_id=training_id)
            new_entry = [employee_id, employee_participation_status]
            training[-1].append(new_entry)

            # Check if participation status is successful
            # If so add qualification and certificate to employee
            if employee_participation_status.lower() == "erfolgreich beendet":
                for qualification_id in training[-2]:
                    self.add_qualification_to_employee(qualification_id, employee_id)
                if training[-3] is not None:
                    self.add_certificate_to_employee(training[-3], employee_id)

            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # Cancels an employee trainings participation
    def delete_employee_from_training(self, employee_id, training_id):
        try:
            employee_list = self.__get_list("Mitarbeiter", entry_id=employee_id)
            employee_list[4].remove(training_id)

            training_list = self.__get_list("Weiterbildungen", entry_id=training_id)
            for employee in training_list[-1]:
                if employee_id in employee:
                    training_list[-1].remove(employee)
                    break

            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # Deletes a training for all employees
    def delete_training_from_employees(self, training_id):
        try:
            employee_list = self.__get_list("Mitarbeiter")
            for entry in employee_list:
                # If id is in training array | employee_list[entry][4] = training array
                if training_id in employee_list[entry][4]:
                    employee_list[entry][4].remove(training_id)
        except KeyError:
            return False
        else:
            return True

    '''# General training methods #'''

    # Adds new training
    def add_training(self, new_training):
        try:
            training_id = self.raise_max_id("Weiterbildungen")
            training_list = self.__get_list("Weiterbildungen")
            self.change_count("Weiterbildungen", amount=1)

            # Append certificate, qualification and employee
            new_training.append(None) # None because entry is no list -> there can only be one certificate from a training
            new_training.append([])
            new_training.append([])

            training_list[training_id] = new_training
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        return True

    # Deletes training and all its connections to employees
    def delete_training(self, training_id):
        try:
            employee_list = self.__get_list("Weiterbildungen")
            employee_list.pop(training_id)
            self.delete_training_from_employees(training_id)
            self.change_count("Weiterbildungen", amount=-1)
            self.write_json_file()
        except KeyError:
            return False
        else:
            return True

    # This function should only be used to change title, description, dates and max-min employees of training
    # To change employees, qualifications and certificates regarded to this training use functions in
    # Employee Training methods, Qualification Training methods, Certificates Training methods
    def edit_training(self, training_id, changed_training):
        try:
            training_list = self.__get_list("Weiterbildungen")
            for i in range(0, 6):
                training_list[training_id][i] = changed_training[i]
            self.write_json_file()

        except (KeyError, ValueError):
            return False
        else:
            return True

    ''' # Qualification Training methods # '''

    def add_qualification_to_training(self, qualification_id, training_id):
        try:
            training = self.__get_list("Weiterbildungen", entry_id=training_id)

            # Add to qualification array(second last entry)
            training[-2].append(qualification_id)
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    def remove_qualification_from_training(self, qualification_id, training_id):
        try:
            training = self.__get_list("Weiterbildungen", entry_id=training_id)

            # Add if to qualification array(second last entry)
            training[-2].remove(qualification_id)
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # This method is called by delete_qualification | Also not sure if we need this method
    def remove_qualification_from_all_trainings(self, qualification_id):
        try:
            training_list = self.__get_list("Weiterbildungen")
            for training in training_list:
                if qualification_id in training_list[training][-2]:
                    training_list[training][-2].remove(qualification_id)

        except (KeyError, ValueError):
            return False
        else:
            return True

    ''' # Qualification employee methods # '''

    def add_qualification_to_employee(self, qualification_id, employee_id):
        try:
            employee = self.__get_list("Mitarbeiter", entry_id=employee_id)

            # Add qualification to employee qualification array(second last entry)
            employee[-2].append(qualification_id)

            # Add employee to qualification
            qualification = self.__get_list("Qualifikation", entry_id=qualification_id)
            qualification[2].append(employee_id)

            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    def remove_employee_from_qualification(self, qualification_id, employee_id):
        try:
            employee = self.__get_list("Mitarbeiter", entry_id=employee_id)

            # Remove qualification from employee qualification array(second last entry)
            employee[-2].remove(qualification_id)

            # Remove employee from qualification
            qualification = self.__get_list("Qualifikation", entry_id=qualification_id)
            qualification[2].remove(employee_id)

            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    '''# General qualifications methods #'''

    # This method assumes that new_qualification only has title and description in list form
    def add_qualification(self, new_qualification):
        try:
            qualification_id = self.raise_max_id("Qualifikation")
            qualification_list = self.__get_list("Qualifikation")
            self.change_count("Qualifikation", amount=1)

            # Add array for employee id
            new_qualification.append([])
            qualification_list[qualification_id] = new_qualification
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # This method assumes that an employee keeps his qualification even tho it was deleted
    # Not sure if this method is necessary
    def delete_qualification(self, qualification_id):
        try:
            qualification_list = self.__get_list("Qualifikation")
            qualification_list.pop(qualification_id)
            self.change_count("Qualifikation", -1)
            self.remove_qualification_from_all_trainings(qualification_id)
            self.write_json_file()

        except (KeyError, ValueError):
            return False
        else:
            return True

    # This function should only be used to change description and title of qualification
    # To change employees regarded to this qualification use functions in 'Qualification employee methods'
    def edit_qualification(self, qualification_id, changed_qualification):
        try:
            qualification_list = self.__get_list("Qualifikation")
            # Only change first two entries of array this way relations stay untouched
            for i in range(0, 2):
                qualification_list[qualification_id][i] = changed_qualification[i]
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    '''# Certificates Training methods #'''

    def add_certificate_to_training(self, certificate_id, training_id):
        try:
            training = self.__get_list("Weiterbildungen", entry_id=training_id)

            # Override third last entry with certificate id
            training[-3] = certificate_id
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    def remove_certificate_from_training(self, certificate_id, training_id):
        try:
            training = self.__get_list("Weiterbildungen", entry_id=training_id)

            # Prevent accidental overrides by checking first
            if certificate_id == training[-3]:
                training[-3] = None
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # This method is called by delete_certificate | Also not sure if we need this method
    def remove_certificate_from_all_trainings(self, certificate_id):
        try:
            training_list = self.__get_list("Weiterbildungen")
            for training in training_list:
                if certificate_id is training_list[training][-3]:
                    training_list[training][-3] = None

        except (KeyError, ValueError):
            return False
        else:
            return True

    '''# Certificate Employee methods #'''

    def add_certificate_to_employee(self, certificate_id, employee_id):
        try:
            employee = self.__get_list("Mitarbeiter", entry_id=employee_id)

            # Add certificate to employee certificate array(last entry)
            employee[-1].append(certificate_id)

            # Add employee to certificate
            certificate = self.__get_list("Zertifikat", entry_id=certificate_id)
            certificate[2].append(employee_id)

            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    def remove_employee_from_certificate(self, certificate_id, employee_id):
        try:
            employee = self.__get_list("Mitarbeiter", entry_id=employee_id)

            # Add certificate to employee certificate array(last entry)
            employee[-1].remove(certificate_id)

            # Add employee to qualification
            certificate = self.__get_list("Zertifikat", entry_id=certificate_id)
            certificate[2].remove(employee_id)

            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    ''' # General certificate methods #'''

    # This method assumes that new_certificate only has title and description in list form
    def add_certificate(self, new_certificate):
        try:
            certificate_id = self.raise_max_id("Zertifikat")
            certificate_list = self.__get_list("Zertifikat")
            self.change_count("Zertifikat", 1)

            # Add array for employee id
            new_certificate.append([])
            certificate_list[certificate_id] = new_certificate
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # Deletes certificate itself and removes it from all trainings
    def delete_certificate(self, certificate_id):
        try:
            certificate_list = self.__get_list("Zertifikat")
            certificate_list.pop(certificate_id)
            self.change_count("Zertifikat", -1)
            self.remove_certificate_from_all_trainings(certificate_id)
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

    # This function should only be used to change description and title of certificate
    # To change employees regarded to this qualification use functions in 'certificate employee methods'
    def edit_certificate(self, certificate_id, changed_certificate):
        try:
            certificate_list = self.__get_list("Zertifikat")
            # Only change first two entries of array this way relations stay untouched
            for i in range(0, 2):
                certificate_list[certificate_id][i] = changed_certificate[i]
            self.write_json_file()
        except (KeyError, ValueError):
            return False
        else:
            return True

a = Database("s")

'''# Testing stuff #'''

#b = a.add_employee(["Markus", "Rühl", "NewYorkChamp", "Rentner"])
#b = a.add_qualification(["Bodybuilder", "Hat jahrelang schwer und falsch trainiert"])
#b = a.add_certificate(["Zertifizierte Legende", "Einfach thunfisch"])
#b = a.add_training(["Bodybuilding", "20-10-2000", "25-02-2010", "Bist ne legende wenn de das schaffst", "1", "1"])
#b = a.add_qualification_to_training("4", "22")
#b = a.add_certificate_to_training("6", "22")
#b = a.add_training_to_employee("29", "22", "Erfolgreich beendet")
#c = a.edit_employee("12", ["Felix", "Koch", "Master", "Prinz", [], [], []])
#d = a.delete_employee("13")
#d = a.add_training(["C++ classes", "20-04-2021", "31-04-2021", "Einfuehrung in classes in C++", "1", "50"])
#d = a.delete_training("4")
#d = a.add_training_to_employee("4", "0","Erfolgreich Teilgenommen")
#d = a.add_training_to_employee("4", "20", "Angemeldet")
#os.system("PAUSE")
#d = a.delete_employee_from_training("7", "0")
#a.delete_training("19")
#a.delete_employee("4")
#d = a.add_qualification(["Klemptner", "Hat Klemptner Ausbildung gemacht"])
#d = a.add_qualification_to_training("3", "21")
#d = a.remove_qualification_from_training("2", "21")
#d = a.add_qualification_to_employee("2", "1")
#d = a.remove_employee_from_qualification("2", "1")
#d = a.add_qualification_to_employee("2", "1")
#d = a.delete_qualification("3")
#d = a.add_certificate(["C Zertifikat", "1 Jahr lang C gelernt"])
#d = a.add_certificate_to_training("5", "20")
#a.add_certificate_to_training("2", "20")
#d = a.remove_certificate_from_training("2", "20")
#d = a.add_certificate_to_employee("2", "19")
#d = a.remove_employee_from_certificate("2", "19")
#d = a.remove_employee_from_certificate("19", "1")
#d = a.delete_certificate("5")
#d = a.edit_certificate("3", ["C++ Zertifikat", "2 Jahr lang C++ gelerent"])
#b = a.edit_certificate("6", ["asd", "asd"])
#b = a.edit_training("21", ["Python class", "20-05-2000", "20-06-2000", "Einfuehrung in Python", "2", "100", "200"])
#print(b)
