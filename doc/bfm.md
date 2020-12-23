<span style="font-family:Arial ">

# Webanwendung - Mitarbeiterqualifizierung 

 > Dieses Projekt wurde bearbeitet von
 >
 >
 > - Nicholas Kroh |  1108804
 > - Leon Weinmann | 1288414
 > - Hendrik Högden | 1308109
 >
 > Projektstand vom 17.12.2020

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
  Gibt den HTML-Code der Startseite zurück

- **`Weiterbildungen()`** und **`createAuswertung_Weiterbildung()`**:
  Die Funktionen sind dazu da den HTML-Code für die Auswertung der Weiterbildungen zurück zu geben.
  Dabei wird die Ausbage alphabetisch sortiert.

- **`Mitarbeiter()`** und **`createAuswertung_Mitarbeiter()`**:
  diese beiden Funktionen sind dazu da
  den HTML-Code für die Auswertung der Mitarbeiter zurück zu geben. Dabei wird die Ausbage alphabetisch sortiert.

- **`addtrainings()`**:
  wird aufgerufen, wenn eine neue Weiterbildung eingetragen werden soll
  sie ruft **`createForm_trainings()`** auf, welche wiederum den HTML-Code für
  das Formular zum Eintragen einer neuen Weiterbildung zurück gibt

- **`showtrainingsdetail()`**:
  wird aufgerufen um in der Sichtweise einen Mitarbeiter detaillierter anzuzeigen,
  wobei sie **`creatDetail()`** aufruft und diese dann die nötigen database- und view-
  Funktionen aufruft
 

- **`showdetailt()`**:
  gibt den HTML-Code für die Detailansichten der Weiterbildungen zurück

- **`canceltrainings()`**:
  wird aufgerufen wenn eine Teilnahme stroniert werden soll, sie leitet die 
  Löschung des Eintrag über die Database ein und leitet den Benutzer dann
  an wieder an die Übersicht zurück

- **`edittrainings()`**, **`deletetrainings()`** und **`savetraining()`**:
  diese Funktionen leiten die Operationen in der Pflege der Weiterbildungen ein

- **`createForm_p()`**:
  gibt den HTML-Code zurück der das Formular anzeigt um einen neuen Mitarbeiter
  einzutragen, dabei leitet sie auch die Speicherung über die database ein

- **`add()`**, **`edit()`** und **`delete()`**:
  diese Funktionen realisieren die Operationen in der Pflege der Mitarbeiter

- **`createForm_trainings()`**:
  gibt den HTML-Code zurück der das Formular anzeigt um eine neue Weiterbildung
  einzutagen und leitet die SPeicherung dieser über  die database ein

- **`createDetail()`**:
  gibt die Detailansicht der Mitarbeiter zurück und filtert vorher heraus an welchen
  Weiterbildungen er bereits teilnimmt und an welchen er noch teilnehmen kann

- **`createContent_p()`**:
  ist dazu da einen Teil der Routden, der Webanwendung aufzurufen. Dabei holt sie 
  sich zuerst die Daten aus der databse und im Anschluss wird die view aufgerufen
  
- **`Zertifikate()`** und **`createAuswertung_Zertifikate()`**:
  diese beiden Funktionen dienen dazu, die Auswertung der Zertifikate auszugeben. 
  Dabei wird die Ausbage alphabetisch sortiert. 
  
- **`showdetailpflegeemploy()`**:
  diese Funktion erstellt die Detailansicht für einen Mitarbeiter. Dazu ruft er die nötigen
  Funktionen in der **`database.py`** und in der **`view.py`**
  
- **`createStartSeite()`**:
  die Funktion wird benötigt im die Startseite zu erstellen


Die Komponenten, mit der die **`application.py`** zusammenwirkt, ist zum einen der Browser. Von Ihm kommen die Anfragen an den Server an. Nachdem die **`application.py`** diese Anfragen bearbeitet hat gibt sie den gerenderten HTML-Code an den Browser zurück.
Bei dieser Umsetzung kommen die zwei weiteren Komponenten dazu, mit denen der Controller zusammen arbeitet. Zum einen die **`database.py`**, die er nutzt um auf die Datenablage zuzugreifen und zum anderen die **`view.py`**, die aus dem Template den HTML-Code rendert.
Die Antworten der beiden Komponenten werden zusammen gelegt. Also das gerenderte Template der **`view.py`** wird mit den Daten der **`database.py`** gefüllt und 
dann an den Browser zurückgegeben.

---

### **`database.py`**
Die **`database.py`** bietet Zugang zu den Daten, der Webanwendung. Die Daten, die in JSON-Dateien gesichert sind können mithilfe von verschiedenen Operationen verändert/bearbeitet werden. Die **`database.py`** wird dafür von der **`application.py`**, genutzt um an die benötigten Daten zu gelangen und um diese zu verändern.
Die Bestandteile sind folgende:

- **`delete_employee_px()`**:
  wenn ein Mitarbeiter gelöscht wird, führt diese Funktion alle nötigen Operationen
  aus

- **`getDefault_px()`**:
  wird benutzt wenn die Formulare ausgefüllt werden, damit die Einträge leer sind
  und die Anwendung weiß wie groß die neuen Einträge sein müssen

- **`saveData_p()`**:
  speichert alle Änderungen oder neuen Einträge in den `.json`-Dateien ab

- **`readData_p()`**:
  liefert Daten aus den `.json`-Dateien aus falls diese benötigt werden 
  

Wie bereits beschrieben wird die **`database.py`** ausschließlich von der
**`application.py`** aufgerufen. Zum einen wenn der Browser Daten aus der
Datenablage abrufen will und sie deshalb in das gerenderte Template
geschrieben müssen. Zum anderen aber auch wenn der Browser Daten ändern
möchte und diese in der Datenablage angepasst werden müssen. Die Funktionen 
und Bestandteile des Scripts greifen auf die Daten, die in den vier 
JSON-Dateien sind  gespeichert sind ab und geben sie an den Controller zurück.


---

### **`dataid.py`**
Die **`dataid.py`** dient dazu den höchsten Indexwert von den **`.json`**-Dateien, die als Datenablage dienen der **`database.py`** zurück zugeben oder ihn zu speichern.
Die Bestandteile sind folgende:

- **`create_px()`**:
  diese Funktion zählt die MaxID einen hoch wenn in einer der `.json`-Dateien ein
  neuer Eintrag hinzu gekommen ist

- **`readMaxId_p()`**:
  diese Funktion wird aufgerufen um die MaxID einer der `.json`-Dateien auszulesen

- **`saveMaxId_p()`**:
  wird von **`create_px()`** aufgerufen um die neue MaxID nachdem sie hochgezählt wurde
  abzuspeichern

Wie oben bereits beschrieben, arbeitet die **`dataid.py`** zum einen mit Datenablagen 
**`MaxIDemployee.json`**, **`MaxIDrelations.json`** und **`MaxIDtrainings.json`**, wenn sie 
aufgerufen wird um den höchsten Indexwert einer der Ablagen zurück zugeben oder 
neu zu speichern. Zum andere interargiert sie mit der **`database.py`**, von der
dieser Aufruf kommt.

---

### **`view.py`**
Die **`view.py`** ist dazu da, das zum Aufruf des Browsers passende Template zu rendern. 
Die Bestandteile sind folgende:

- **`createForm_trainings()`**:
  rendert den HTML-Code für das Formular, dass aufgrufen wird wenn eine neue
  Weiterbildung eingetragen werden soll und gibt diesen an die `application.py`weiter

- **`createForm_px()`**:
  rendert den HTML-Code für das Formular, dass aufgerufen wird wenn ein neuer Mitarbeiter
  eingretragen werden soll und gibt diesen an die `application.py` zurück
  
- **`createDetailTrainings()`**:
  gibt den HTMl-Code zurück, der für die detaillierte Ansicht einer Weiterbildung
  benötigt wird

- **`createFormauswertungMitarbeiter()`**:
  gibt den HTML-Code für die Auswertungsseite der Mitarbeiter zurück

- **`createAuswertungWeiterbildung()`**:
  liefert den HTML-Code für die Auswertungsseite der Weiterbildungen zurück

- **`createDetail()`**:
  gibt den HTML-Code zurück, der für die detaillierte Ansicht eines Mitarbeiters
  benötigt wird

- **`createContent_px()`**:
  wird beim Aufruf mancher Routen aufgerufen. Diese sind: [Pflege Mitarbeiter],
  [Pflege Weiterbildungen], [Sichtweise_Mitarbeiter], [Sichtweise_Weiterbildungen]
  und [Startseite]

Die **`application.py`** ruft die um an den gerenderten HTML-Code zu kommen und
ist daher die erste Komponente mit der die **`view.py`** zusammenwirkt. Um diese "Aufgabe"
zu erfüllen, greift die **`view.yp`** auf die **`.tpl`**-Files zu und rendert mit diesen den
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



### Content

Zusätzlich benutzen wird ein **`.css`**-Stylsheet (**`../content/hauptansicht.css`**) um unsere **`.tpl`**-Dateien zu formatieren.
Dazu kommt noch ein **`.js`**-Skript, dass eine Bestätigungsabfrage beim Löschen eines
Eintrages ermöglicht. (**`../content/hauptansicht.js`**)

---

---

## Datenablage

Die Datenablage für die Webanwendung haben wir wie im ersten Praktikum der Einfachheit
halber mit Hilfe von acht **`.json`**-Dateien realsiert. Die Struktur sieht wie folgt aus:

### **`employee.json`**

 > Speicherung aller Mitarbeiter, dabei hat jeder Eintrag vier 
 > Komponenten: 
 >  - Nachname
 >  - Vorname
 >  - akademischen Grad
 >  - Tätigkeit

### **`trainings.json`**

 > Speicherung aller Weiterbildungenmit folgenden 
 > Komponenten: 
 >  - Bezeichnung
 >  - Von/Bis
 >  - Beschreibung
 > - min/max Teilnehmerzahl 


### **`MaxIDemployee.json`**

 > Speichert den höchsten Indexwert der **`employee.json`**


### **`MaxIDtrainings.json`**

 > Speichert den höchsten Indexwert der **`trainings.json`**


### **`employeeparticipations.json`**

 > Speichert die Information von jedem Mitarbeiter so wie in der **`employee.json`**, allerdings 
 > werden hier die Teilnahmen zusätzlich mit einbezogen. Diese Information werden benötigt um 
 > die Detailansichten und Auswertungen bei Mitarbeitern zu ermöglichen


### **`employeetrainings.json`**

 > Speichert alle Weiterbildungen wie in der **`trainings.json`**, allerdings kommt
 > in dieser Datenablage ein zusätzlicher Eintrag hinzu, der speichert welche 
 > Mitarbeiter an dieser Weiterbildung teilnehmen oder teilgenommen haben
 > Diese Tabelle gibt uns genauso wie die **`employeeparticipations.json`** eine Referenz 
 > zwischen Mitarbeitern und Weiterbildungen, die wir benötigen um Detailansichten
 > zur Verfügung stellen zu können


### **`MaxIDrelations.json`**

 > Speichert den höchsten Indexwert der **`employeetrainings.json`**


### **`MaxIDemployP.json`**

 > Speichert den höchsten Indexwert der **`employeeparticipations.json`**



---

---

## Durchführung und Ergebnis der geforderten Prüfungen

### Überprüfung markup

 >|Route                          				|Anzahl Fehler |Anzahl Warnings |
 >|---------------------------------------------|--------------|----------------|
 >|/?index=Startseite			 				|    12        |    0        	|
 >|/?index=Pflege_Mitarbeiterdaten				|     10   	   |     8       	|
 >|/add       	 	 			 				|		10 	   |       3        |
 >|/edit/1?listform=Pflege_Mitarbeiterdaten 	|  10	       |         3      |
 >|/?index=Pflege_Weiterbildungen 				|  	10	       |  10            |
 >|/addtrainings	 	 			 			|  		10     |         3      |
 >|/edittrainings/2?index=Pflege_Mitarbeiterdaten|  	10	   |      3         |
 >|/?index=Sichtweise_Mitarbeiter 				|  		 10    |     8          |
 >|/showtrainingsdetail/1		 				| 12	       |           1    |
 >|/?index=Sichtweise_Weiterbildungen			|  	10	       |9               |
 >|/showdetailt/3 	 			 				|  	12	       |          1     |
 >|/Mitarbeiter 	 	 			 			|  	28	       |         3      | 
 >|/Weiterbildungen 	 			 			|  13	       |          1     | 
 >|/Zertifikate	 	 			 				|  	13	       |      1         | 



### Überprüfung css

 > `hauptansicht.css` -  0 Fehler



</span>