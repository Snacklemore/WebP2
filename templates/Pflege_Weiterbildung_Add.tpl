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
      <span style="float:left;">Version 2.0 / 29.12.2020</span>
      <br>
      <span style="float:right;">Hendrik Högden | 1308109</span>
      <br>
   </header>
   <section>
      <nav>
         <dl>
         <dt><a href="/Startseite">Startseite</a></dt>
         <dl>
            <hr>
            <dt><a href="/pflege_mitarbeiterdaten">Pflege Mitarbeiterdaten</a></dt>
            <dt><a href="/pflege_weiterbildungen">Pflege Weiterbildungen</a></dt>
         </dl>
         <hr>
         <dl>
            <dt>Teilnahme</dt>
            <dd><a href="/sichtweise_mitarbeiter">- Sichtweise Mitarbeiter</a></dd>
            <dd><a href="/sichtweise_weiterbildungen">- Sichtweise Weiterbildungen</a></dd>
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
         <form id="idWTForm" action="/save_training" method="POST">
            <input type="hidden" value="${key_s}" id="training_id" name="training_id" />
            <div>
               <label for="title">Bezeichnung</label>
               <input type="text"
                  value="${data_o[0]}"
                  id="title"
                  name="title" required />
            </div>
            <div>
               <label for="date_begin">Von</label>
               <input type="date"
                  value="${data_o[1]}"
                  id="date_begin"
                  name="date_begin" required />
            </div>
            <div>
               <label for="date_end">Bis Grad</label>
               <input type="date"
                  value="${data_o[2]}"
                  id="date_end"
                  name="date_end" required />
            </div>
            <div>
               <label for="description">Beschreibung</label>
               <input type="text"
                  value="${data_o[3]}"
                  id="description"
                  name="description" required />
            </div>
            <div>
               <label for="max_attendees">Max. Teilnehmer</label>
               <input type="number"
                  value="${data_o[4]}"
                  id="max_attendees"
                  name="max_attendees" required />
            </div>
            <div>
               <label for="min_attendees">Min. Teilnehmer</label>
               <input type="number"
                  value="${data_o[5]}"
                  id="min_attendees"
                  name="min_attendees" required />
            </div>
            <div>
               <input type="submit" value="Speichern"/>
            </div>
         </form>
      </article>
   </section>
</body>
</html>

