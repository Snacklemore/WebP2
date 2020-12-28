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
         <dt><a href="?index=Startseite">Startseite</a></dt>
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
         <h2>Auswertung Weiterbildungen</h2>
         % for x in training:
         <table>
            <tr>
               <th>Bezeichnung</th>
               <th>Von</th>
               <th>Bis</th>
               <th>Beschreibung</th>
            </tr>
            <tr>
               <td>${x[1][0]}</td>
               <td>${x[1][1]}</td>
               <td>${x[1][2]}</td>
               <td>${x[1][3]}</td>            
            </tr>
            <td></td>
               <tr>
                  <th>Mitarbeiter</th>
                  <th>Vorname</th>
                  <th>akademische Grade</th>
                  <th>Status</th>
               </tr>   
               % for i in x[1][8]:
               <tr>
                  <td>${i[0]}</td>
                  <td>${i[1]}</td>
                  <td>${i[2]}</td>
                  <td>${i[4]}</td>
               </tr>
               % endfor
            % endfor
         </table>
      </article>
   </section>
</body>
</html>

