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
            <dd><a href="sichtweise_weiterbildungen">- Sichtweise Weiterbildungen</a></dd>
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
        <form id="idWTForm" action="/save_qualification_and_certificate" method="POST">
         <h1>Qualifikationen</h1>
         <tr></tr>
         % for x in data_o:
         <input type="hidden" value="${x[2]}" id="id_qualification" name="id_qualification" />
         <div>
            <label for="qualification_title">Bezeichnung</label>
            <input type="text"
               value="${x[0]}"
               id="qualification_title"
               name="qualification_title" required />
         </div>
         <div>
            <label for="qualification_description">Beschreibung</label>
            <input type="text"
               value="${x[1]}"
               id="qualification_description"
               name="qualification_description" required />
         </div>
         <br>
         % endfor
            <a href="/add_qualification/${t_id}">Qualifikation erfassen</a>
            <input type="hidden" value="${t_id}" id="t_id" name="t_id" />
            <h1>Zertifikate</h1>
            % for x in data_t:	
            <input type="hidden" value="${x[3]}" id="certificate_id" name="certificate_id" />	
            <div>
               <label for="certificate_title">Bezeichnung</label>
               <input type="text"
                  value="${x[0]}"
                  id="certificate_title"
                  name="certificate_title" required />
            </div>
            <div>
               <label for="certificate_description">Beschreibung</label>
               <input type="text"
                  value="${x[1]}"
                  id="certificate_description"
                  name="certificate_description" required />
            </div>
            <div>
               <label for="certifiacte_entitled_to">Berechtigt zu</label>
               <input type="text"
                  value="${x[2]}"
                  id="certifiacte_entitled_to"
                  name="certifiacte_entitled_to" required />
            </div>
            <br>

            % endfor
            <div>
               <a href="/add_certificate/${t_id}">Zertifikat erfassen</a>
            </div>

         <div>
            <input type="submit" value="Speichern"/>
         </div>
         </form>
      </article>
   </section>
</body>
</html>

