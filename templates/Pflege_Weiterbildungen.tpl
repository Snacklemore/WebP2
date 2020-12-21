##coding: utf-8
<!DOCTYPE html>
<head>
   <title>Mitarbeiterqualifizierung</title>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="\hauptansicht.css"/>
   <script type="text/javascript" src="/webteams.js"></script>
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
         <h1>Weiterbildungen</h1>
         <table>
            <tr>
               <th>Bezeichnung</th>
               <th>Von</th>
               <th>Bis</th>
               <th>Beschreibung</th>
               <th>maximale Teilnehmerzahl</th>
               <th>minimale Teilnehmerzahl</th>
            </tr>
            % for key_s in data_o:
            <tr>
               <td>${data_o[key_s][0]}</td>
               <td>${data_o[key_s][1]}</td>
               <td>${data_o[key_s][2]}</td>
               <td>${data_o[key_s][3]}</td>
               <td>${data_o[key_s][4]}</td>
               <td>${data_o[key_s][5]}</td>
               <td>
               <td>
               <td>
                  <a href="/edittrainings/${key_s}?index=Pflege_Mitarbeiterdaten">bearbeiten</a>
                  <a href="/deletetrainings/${key_s}?index=Pflege_Mitarbeiterdaten" class="clDelete">Löschen</a>
               </td>
            </tr>
            % endfor
         </table>
         <div>
            <a href="/addtrainings">erfassen</a>
            <a href="?index=Pflege_Mitarbeiterdaten">Ansicht ändern</a>
         </div>
      </article>
   </section>
</body>
</html>

