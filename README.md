<span style="font-family:Arial ">

# Webanwendung - Mitarbeiterqualifizierung 

 > Dieses Projekt wurde bearbeitet von
 >
 >
 > - Nicholas Kroh |  1108804
 > - Leon Weinmann | 1288414
 > - Hendrik Högden | 1308109
 >
 > Projektstand vom 04.01.2020

## Einleitung
Die Webanwendung Mitarbeiterqualifizierung  soll dazu dienen die Weiterbildungen innerhalb einer Firma möglichst strukturiert zu organisieren und übersichtlich darzustellen. Zudem können neue Qualifikationen von Mitarbeitern sowie Weiterbildungen an sich im System neu erfasst werden. Die Anwendung berücksichtigt außerdem neben freiwilligen Weiterbildungen auch Weiterbildungen mit Abschlüssen und Zertifikaten.

---

---

## Aufgabenstellung
Um die Aufgabenstellung und Anforderungen an die Webanwendung zu beschrieben, werden wir zuerst auf die Datenstruktur hinter der Anwendung eingehen, danach gehen wir auf den Aufbau der Benutzerschnittstelle ein.


### Aufbau der Datenstruktur
Aufgebaut soll die Anwendung so sein, dass ein Mitarbeiter an Weiterbildungen teilnehmen kann. Diese Teilnahme gibt dem Mitarbeiter Verfügung über Zertifikate und Qualifikationen, sofern die Teilnahme an einer Weiterbildung diese ausstellt. Weiterbildungen sollen nach erfolgreicher Teilnahme mindestens eine Qualifikation ausstellen, wohingegen Zertifikate nicht unbedingt erworben werden.
Eine bessere Übersicht über die Vorgabe bietet hier ein Datenmodell (Abb.1).

![(Abb.1)](p2_datenmodell.png)



Die einzelnen Bestandteile der Anwendung soll mit verschiedenen Attributen gespeichert werden. Die wie folgt aussehen

 - **Mitarbeiter**
	 - Name
	 - Vorname
	 - akademische Grade
	 - Tätigkeit
- **Weiterbildung**
	- Bezeichnung
	- VonBis
	- Beschreibung
	- maximale und minimale Teilnehmerzahl
- **Zertifikat**
	- Bezeichnung
	- Beschreibung
	- Berechtigungen durch das Zertifikat
- **Qualifikation**
	- Bezeichnung
	- Beschreibung

### Aufbau der Benutzeroberfläche
Die Benutzeroberfläche soll wie in Abb.2 dargestellt, aufgebaut werden.

![(Abb.2)](p2_wireframe.png)


Der Kopfbereich stellt die Namen und Version der Webanwendung, sowie die Namen unserer Gruppe da. Darunter befindet sich link die Sidebar, welche als Navigationsbereich für die Anwendung benutzt wird. Diese beiden Bereiche verändern sich bei der Benutzung der Webseite nicht. 
Rechts neben der Sidebar befindet sich der Inhaltsbereich in die aufgerufenen Seiten angezeigt werden. Die in der Navigation bedienbaren Einträge und somit einen neuen Inhalt aufrufen sind folgende

- **[Startseite]**
	- Die Startseite zeigt die Anzahl aller Mitarbeiter, Weiterbildungen und Teilnahmen
- **[Pflege Mitarbeiterdaten]**
	- dieser Bereich ist dazu da neue Mitarbeiter anzulegen oder bestehende Einträge von Mitarbeiter zu bearbeiten, außerdem soll sich von jedem Mitarbeiter eine Detailansicht anzeigen lassen
- **[Pflege Weiterbildungen]**
	- dieser Bereich ist dazu da neue Weiterbildungen anzulegen oder bestehende Weiterbildungen zu bearbeiten, auch hier gibt es zu jedem Eintrag die Möglichkeit sich eine Detailansicht anzeigen zu lassen
- **Teilnahme - [Sichtweise Mitarbeiter]**
	- hier kann man die Daten zu einem Mitarbeiter noch detaillierter angezeigt bekommen, bspw. an welche Teilnahmen er hat und an welchen Weiterbildungen er teilnehmen könnte
- **Teilnahme - [Sichtweise Weiterbildungen]**
	-  hier gelangt man durch die Auswahl einer bestimmten Weiterbildung zu einer detaillierteren Ansicht, die unter anderem die Teilnehmer angezeigt werden, deren Teilnahme auch unterbrochen werden kann
- **Auswertungen - [Mitarbeiter]**
	- hier befindet sich eine alphabetisch sortierte Liste der Mitarbeiter, mit allen Teilnahmen des Mitarbeiters
- **Auswertungen [Weiterbildungen]**
	- hierbefindet sich eine alphabetische Liste der Weiterbildungen, mit deren erfolgreichen Teilnehmern
- **Auswertungen [Zertifikate]**
	- alphabetische Anzeige der vergebenen Zertifikate aller Mitarbeiter

---

---

## Unsere Lösung
Bei der Beschreibung unserer Lösung werden wir zuerst die serverseitige Umsetzung
erläutern, in dem wir alle Komponenten des Servers einzeln beschreiben, diese
befinden sich in **`../MarbtrQualifizierung/app`**. 
Anschließend werden wir auf die Datenablage eingehen, die sich in 
**`../MarbtrQualifizierung/data`**.

---

### **`application.py`**
Die **`application.py`** dient als Controller der Anwendung. Er liefert die gerenderten Templates an den Browser, welche er vorher mit Daten befüllt, die er sich aus den JSON-Dateien holt. Zudem leitet er ÄnderungenLöschung in den Daten, wenn sie vom Browser angefordert werden.

Die Bestandteile sind folgende:

- **`index()`**:
 ruft die Funktion Startsseite() auf

- **`Startseite():`** :
 
  gibt den HTML-Code für die Startseite der Webanwendung zurück, auf der die aktuelle
  Anzahl aller Mitarbeiter, Weiterbildungen und Teilnahmen angezeigt wird
  

- **`pflege_mitarbeiterdaten()`**, **`show_detail_employee()`**, **`edit_employee()`**,**`add_employee()`**, **`save_employee()`** und **`delete_employee(self, employee_id)`**:
  
  diese Funktionen stellen die Operationen rund um den Menüpunkt [Pflege Mitarbeiterdaten]
  zur Verfügung, zum einen die generelle Übersicht aller Mitarbeiter aber auch die 
  detailansicht jedes einzelnen sowie die Formulare um neue Mitarbeiter einzupflegen
  oder bestehende Mitarbeiterdaten zu ändern 


- **`pflege_weiterbildungen()`**, **`edit_training()`**, **`add_training()`**, **`save_training()`**, **`delete_training()`** und **`show_detail_training()`**:
  
  diese Funktionen realsieren das gleiche wie im letzen Abschnitt beschrieben
  allerdings für den Bereich [Pflege Weiterbildungen]. Die Funktionen ermöglichen
  einen das Löschen, Erfassen und Bearbeiten von Weiterbildungen sowie das Anzeigen
  einer Detailansicht für jede Weiterbildunge 
  

- **`manage_qualification_and_certificates()`**, **`add_qualification()`**, **`add_certificate()`**, **`save_qualification_and_certificate()`**, **`save_qualification()`** und **`save_certificate()`**:
  
  diese Funktionen sind ebenfalls Teil des Bereichs [Pflege Weiterbildungen]. Sie 
  stellen die benötigten Formulare um die Qualifikationen und Zertifikate der einzelnen
  Weiterbildungen zu verwalten
 
- **`sichtweise_mitarbeiter()`**, **`inspect_employee_detail()`**, **`cancel_employee_training()`**, **`add_employee_to_training()`** und **`save_employee_to_training()`**:
  
  diese Funktionen stellen die Operationen des Bereichs [Sichtweise Mitarbeiter] zur
  Verfügung. Zum einen die Überischt über aller Mitabrbeiter zm anderen aber auch
  die Detailansicht für jeden einzelnen Mitarbeiter in der es die Möglichkeit gibt
  Teilnahmen des entsprechenden Mitarbeiter abzubrechen 

- **`sichtweise_weiterbildungen()`**, **`inspect_training_detail()`** und **`cancel_employee_training_sichtweise_weiterbildung()`**:
  
  diese Funktionen stellen genau das gleiche wie im letzten Abschnitt zur Verfügung
  allerdings für den Teil [Sichtweise Weiterbildungen]. Dementsprechend gibt es hier
  eine Übersicht über alle Weiterbildungen und zusätzlich zu jedem eine Detailansicht
  in der Teilnahmen storniert werden können 

- **`Mitarbeiter()`*t*:
  
  Mitarbeiter() gib den HTML-Code für den Bereich [Auswertung Mitarbeiter] zurück
  der eine detaillierte Komplettansicht aller Mitarbeiter anzeigt

- **`Weiterbildungen()`**:
  
  Weiterbildungen() gib den HTML-Code für den Bereich [Auswertung Weiterbildungen] zurück 
  der eine detaillierte Komplettansicht aller Weiterbildungen anzeigt

- **`Zertifikate()`**:
  
  Zertifikate() gib den HTML-Code für den Bereich [Auswertung Zertifikate] zurück
  der eine detaillierte Komplettansicht aller Zertifikate anzeigt

Die Komponenten, mit der die **`application.py`** zusammenwirkt, ist zum einen
der Browser. Von Ihm kommen die Anfragen an den Server an. Nachdem die 
**`application.py`** diese Anfragen bearbeitet hat gibt sie den gerenderten HTML-Code
an den Browser zurück. Bei dieser Umsetzung kommen die zwei weiteren Komponenten dazu,
mit denen der Controller zusammen arbeitet. Zum einen die **`database.py`**, die er
nutzt um auf die Datenablage zuzugreifen und zum anderen die **`view.py`**, die aus
dem Template den HTML-Code rendert. Die Antworten der beiden Komponenten werden
zusammen gelegt. Also das gerenderte Template der **`view.py`** wird mit den Daten
der **`database.py`** gefüllt und dann an den Browser zurückgegeben.

---

### **`database.py`**
Die **`database.py`** bietet Zugang zu den Daten, der Webanwendung. Die Daten, die in JSON-Dateien gesichert sind können mithilfe von verschiedenen Operationen verändert/bearbeitet werden. Die **`database.py`** wird dafür von der **`application.py`**, genutzt um an die benötigten Daten zu gelangen und um diese zu verändern.
Die Bestandteile sind folgende:

- **`__reset_json_file()`**, **`read_json_file()`** und **`write_json_file()`**:
  
  diese drei Funktionen ermöglichen den anderen folgenden Funktionen den Zugriff
  auf die `.json`-Datei in der alle Daten gespeichert sind. Zum einen um Daten nur auszulesen (read)
  zum anderen um Daten zu ergänzen oder zu bearbeiten (write) 

- **`get_list()`**:
  
  diese Funktion ist das dazu da die richtigen Einträge aus der Datenablage bekommt
  sie fragt ab welcher dictionary-name übergeben wurde um so die zum Aufruf 
  passenden Daten zurück zu geben. Bspw wenn der Name "employee" übergeben wurde such
  die Funktionen den Teil der `.json`.Datei heraus in der die Mitarbetier gespeichert
  sind und gibt diese zurück 

- **`raise_max_id()`**:
  
  wird aufgerufen wenn ein neuer Eintrag hinzugefügt wurde und erhöht dann die MaxID
  um 1 und gibt den neuen Wert zurück 

- **`change_count()`**:
  
  diese Funktion erhöht die allgmeine Anzahl des entsprechenden Eintrags zurück

- **`add_employee()`**, **`delete_employee()`**, **`edit_employee()`** und **`get_empty_employee_array()`**:
  
  diese Funktion ermöglichen die Datenzugriffe bei der Pflege der Mitarbeiter unter
  dem Bereich [Pflege Mitarbeiter] 
 
- **`add_training_to_employee()`**, **`delete_employee_from_training()`**, **`delete_training_from_employees()`**, **`change_participation_count()`** und **`get_employee_participation_status()`**:
  
  diese Funktionen führen die benötigten Datenzugriffe durch, wenn Teilnahmen von 
  Mitarbeitern and Weiterbildungen hinzugefügt oder storniert werden sollen 

- **`add_training()`**, **`delete_training()`**, **`edit_training()`**, **`get_empty_training_array()`** und **`get_participation_status_array()`**:
  
  diese Funktion ermöglichen die Datenzugriffe bei der Pflege der Weiterbildungen unter
  dem Bereich [Pflege Weiterbildungen] 

- **`add_qualification_to_training()`**, **`remove_qualification_from_training()`** und **`remove_qualification_from_all_trainings()`**:
  
  diese Funktionen führen die benötigten Datenzugriffe durch, wenn Qualifikationen von 
  Weiterbildungen hinzugefügt oder storniert werden sollen 

- **`add_qualification_to_employee()`** und **`remove_employee_from_qualification()`**:
  
  diese Funktionen führen die benötigten Datenzugriffe durch, wenn Qualifikationen von 
  Mitarbeitern hinzugefügt oder entfernt werden sollen 

- **`add_qualification()`**, **`delete_qualification()`** und **`edit_qualification()`**:
  
  diese Funktionen dienen zur Pflege der Qualfikationen, wenn sie gelöscht, bearbeitet 
  oder neu hinzugefügt werden sollen. Diese Funktione ist Teil des Bereichs 
  [Pflege Weiterbildungen] 

- **`add_certificate_to_training()`**, **`remove_certificate_from_training()`** und **`remove_certificate_from_all_trainings()`**:
  
diese Funktionen führen die benötigten Datenzugriffe durch, wenn Zertifikate zu 
  Weiterbildungen hinzugefügt oder entfernt werden sollen 
 
- **`add_certificate_to_employee()`** und **`remove_employee_from_certificate()`**:

  diese Funktionen führen die benötigten Datenzugriffe durch, wenn Zertifikate zu 
  Mitabreitern hinzugefügt oder entfernt werden sollen 
 
- **`add_certificate()`**, **`delete_certificate()`** und **`edit_certificate()`**:
  
  diese Funktionen dienen zur Pflege der Zertifikate, wenn sie gelöscht, bearbeitet 
  oder neu hinzugefügt werden sollen. Diese Funktione ist Teil des Bereichs 
  [Pflege Weiterbildungen] 

Wie bereits beschrieben wird die **`database.py`** ausschließlich von der
**`application.py`** aufgerufen. Zum einen wenn der Browser Daten aus der
Datenablage abrufen will und sie deshalb in das gerenderte Template
geschrieben müssen. Zum anderen aber auch wenn der Browser Daten ändern
möchte und diese in der Datenablage angepasst werden müssen. Die Funktionen 
und Bestandteile des Scripts greifen auf die Daten, die in der **`databsae.json`** 
gespeichert sind ab und geben sie an den Controller zurück.

---

### **`view.py`**
Die **`view.py`** ist dazu da, das zum Aufruf des Browsers passende Template zu rendern. 

Sie besteht daher aus 19 Funktionen die alle einen verschiedene Inahlt im Inhaltbereich
darstellen. Je nachdem was der User aufruft, wird in der **`application.py`** die
entsprechende Funktion aufgerufen.

Die **`application.py`** ist die erste Komponente, die mit der **`view.py`** zusammen
arbeitet, da sie die **`view.py`** aufruft um an den gerenderten HTML-Code zu kommen.
Um diese "Aufgabe" zu erfüllen, greift die **`view.yp`** auf die **`.tpl`**-Files zu und rendert mit diesen den
passenden HTML-Code.

### Templates

Damit die **`view.py`** den HTML-Code für die einzelnen Routen rendern kann, 
benötigt sie Templates. Diese sind in **`../MarbtrQualifizierung/templates`** als
**`.tpl`**-Dateien gespeichert:

- **`Startseite.tpl`**: Startseite
- **`Pflege_Mitarbeiterdaten.tpl`**: Liste aller Mitarbeiter
- **`Pflege_Mitarbeiter_Add.tpl`**: Formular zum Erfassen eines neuen Mitarbeiters
- **`Pflege_Mitarbeiter_Detail.tpl`**: Detailansicht einen Mitarbeiter
- **`Pflege_Weiterbildungen.tpl`**: Liste aller Weiterbildungen
- **`Pflege_Weiterbildungen_Add.tpl`**: Formular zum Erfassen einer neuen Weiterbildung
- **`Pflege_Weiterbildung_Detail.tpl`**: Detailansicht einer Weiterbildung
- **`Sichtweise_Mitarbeiter.tpl`**: Liste aller Mitarbeiter
- **`Sichtweise_Mitarbiter_Detail.tpl`**: Detailansicht eines Mitarbeiter
- **`Sichtweise_Weiterbildungen.tpl`**: Liste aller Weiterbildungen
- **`Sichtweise_Weiterbildungen_Detail.tpl`**: Detailansicht einer Weiterbildung
- **`Weiterbildungen.tpl`**: Auswertung der Weiterbildungen
- **`Zertifikate.tpl`**: Auswertung der Zertifikate
- **`Mitarbeiter.tpl`**: Auswertung der Mitarbeiter
- **`Error.tpl`**: Fehleranzeige falls ein Fehker auftritt
- **`Pflege_Weiterbildung_Qualification_Add.tpl`**: Formular für neue Quali
- **`Pflege_Weiterbildungen_Certificate_Add.tpl`**: Formular für neues Zertifikat
- **`Pflege_Weiterbildungen_QZ_Verwalten.tpl`**: Verwaltung der Quali's
- **`Sichtweise_Mitarbeiter_Add_Training.tpl`**: Auswahl um Mitarbeiter an Training anzumelden




### Content

Zusätzlich benutzen wird ein **`.css`**-Stylsheet (**`../content/hauptansicht.css`**) um unsere **`.tpl`**-Dateien zu formatieren.
Dazu kommt noch ein **`.js`**-Skript, dass eine Bestätigungsabfrage beim Löschen eines
Eintrages ermöglicht. (**`../content/hauptansicht.js`**)

---

---

## Datenablage

Die Datenablage für die Webanwendung haben wir im Gegensatz zum ersten Praktikum
etas anders umgesetzt. Statt mehrerer **`.json`**-Dateien benutzen wir für diese 
Webanwendung nur eine einzige: **`database.json`**.

Diese ist in 4 Dictionaries aufgeteilt: Mitarbeiter, Weiterbildungen, Zertifikate und
Qualifikationen. In allen Dictionaries sind neben dem Count, MaxID und Informationen 
zum jeweiligen Eintrag auch noch alle weiteren Informationen gespeichert, die bei 
Operationen der Webanwendung benötigt werden

In den einzelnen Dictionaries werden die einzelnen Einträgen mit einer indivduellen ID
versehen über die man sie immer wieder genau identifizieren kann.

---

---

## Durchführung und Ergebnis der geforderten Prüfungen

### Überprüfung markup

 >|Route                          				|Anzahl Fehler |Anzahl Warnings |
 >|---------------------------------------------|--------------|----------------|
 >|/Startseite			 				        |    12        |    1        	|
 >|/Pflege_Mitarbeiterdaten			        	|     10   	   |     7       	|
 >|/add_employee      	 	 			 		|		10 	   |       3        |
 >|/edit_employee/1                            	|  10	       |         3      |
 >|/show_detail_employee/1                      |          12  |      1         |
 >|/Pflege_Weiterbildungen 		        		|  	10	       |  10            |
 >|/add_training	 	 			 			|  		10     |         3      |
 >|/edit_training/1                             |  	10	       |      3         |
 >|/show_detail_training/1                      |      10      |     1          | 
 >|/manage_qualification_and_certificates/1     |    15        |   7            | 
 >|/add_certificate/1                           |     10       |     3          |
 >|/sichtweise_mitarbeiter			           	|  		 10    |     7          |
 >|/inspect_employee_detail/1	 				| 12	       |           1    |
 >|/sichtweise_weiterbildungen      			|  	10	       |  9             |
 >|/inspect_training_detail/1	 				|  	12	       |          1     |
 >|/Mitarbeiter 	 	 			 			|  	28	       |         3      | 
 >|/Weiterbildungen 	 			 			|  13	       |          1     | 
 >|/Zertifikate	 	 			 				|  	13	       |      1         | 



### Überprüfung css

 > `hauptansicht.css` -  0 Fehler



</span>
