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
         <h2>Mitarbeiterdaten</h2>
         <table>
            <tr>
               <th>Name</th>
               <th>Vorname</th>
               <th>akademische Grade</th>
               <th>Tätigkeit</th>
            </tr>
            % for key_s in data_o:
            <tr>
               <td>${data_o[key_s][0]}</td>
               <td>${data_o[key_s][1]}</td>
               <td>${data_o[key_s][2]}</td>
               <td>${data_o[key_s][3]}</td>
               <td>
                  <a href="/edit_employee/${key_s}">bearbeiten</a>
                  <a href="/delete_employee/${key_s}" class="clDelete">Löschen</a>
                  <a href="/show_detail_employee/${key_s}" >Anzeigen</a>
               </td>
            </tr>
            % endfor
         </table>
         <div>
            <a href="/add_employee">erfassen</a>
         </div>
      </article>
   </section>
</body>
</html>

