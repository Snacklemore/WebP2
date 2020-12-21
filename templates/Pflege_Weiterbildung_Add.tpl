##coding: utf-8
<!DOCTYPE html>
<head>
   <title>Mitarbeiterqualifizierung</title>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="\hauptansicht.css"/>
</head>
<body>
   <header>
      <span style="float:right;">Nicholas Kroh | 1108804</span>
      <span style="float:left;">  Mitarbeiterqualifizierung</span>
      <br>
      <span style="float:right;">Leon Weinmann | 1288414</span>
      <span style="float:left;">  Version 1.0 / 17.12.2020</span>
      <br>
      <span style="float:right;">Hendrik Högden | 1308109</span>
      <br>
   </header>
   <section>
      <nav>
         <dl>
         <dt><a href="/?index=Startseite">Startseite</a></dt>
         <dl>
            <hr>
            <dt><a href="/?index=Pflege_Mitarbeiterdaten">Pflege Mitarbeiterdaten</a></dt>
            <dt><a href="/?index=Pflege_Weiterbildungen">Pflege Weiterbildungen</a></dt>
         </dl>
         <hr>
         <dl>
            <dt>Teilnahme</dt>
            <dd><a href="/?index=Sichtweise_Mitarbeiter">- Sichtweise Mitarbeiter</a></dd>
            <dd><a href="/?index=Sichtweise_Weiterbildungen">- Sichtweise Weiterbildungen</a></dd>
         </dl>
         <hr>
         <dl>
            <dt>Auswertung</dt>
            <dd><a href="/Mitarbeiter">- Mitarbeiter</a></dd>
            <dd><a href="/Weiterbildungen">- Weiterbildungen</a></dd>
            <dd><a href ="/Zertifikate">- Zertifikate</a></dd>
         </dl>
         <hr>
      </nav>
      <article>
         <form id="idWTForm" action="/savetraining" method="POST">
            <input type="hidden" value="${key_s}" id="id_spa" name="id_spa" />
            <div>
               <label for="bezeichnung_spa">Bezeichnung</label>
               <input type="text"
                  value="${data_o[0]}"
                  id="bezeichnung_spa"
                  name="bezeichnung_spa" required />
            </div>
            <div>
               <label for="Von_spa">Von</label>
               <input type="date"
                  value="${data_o[1]}"
                  id="Von_spa"
                  name="Von_spa" required />
            </div>
            <div>
               <label for="Bis_spa">Bis Grad</label>
               <input type="date"
                  value="${data_o[2]}"
                  id="Bis_spa"
                  name="Bis_spa" required />
            </div>
            <div>
               <label for="beschreibung_spa">Beschreibung</label>
               <input type="text"
                  value="${data_o[3]}"
                  id="beschreibung_spa"
                  name="beschreibung_spa" required />
            </div>
            <div>
               <label for="maxteilnehmer_spa">Max. Teilnehmer</label>
               <input type="number"
                  value="${data_o[4]}"
                  id="maxteilnehmer_spa"
                  name="maxteilnehmer_spa" required />
            </div>
            <div>
               <label for="minteilnehmer_spa">Min. Teilnehmer</label>
               <input type="number"
                  value="${data_o[5]}"
                  id="minteilnehmer_spa"
                  name="minteilnehmer_spa" required />
            </div>
            <div>
               <input type="submit" value="Speichern"/>
            </div>
         </form>
      </article>
   </section>
</body>
</html>

