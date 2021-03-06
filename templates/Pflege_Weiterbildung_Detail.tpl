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
         </dl>
      </nav>
      <article>
         <h1>Weiterbildung:</h1>
         <h4>Bezeichnung</h4>
         <p>${data_o[0]}</p>
         <h4>Von</h4>
         <p>${data_o[1]}</p>
         <h4>Bis</h4>
         <p>${data_o[2]}</p>
         <h4>Beschreibung</h4>
         <p>${data_o[3]}</p>
         <table>
            <h1>Teilnehmer</h1>
            % for x in data_p:
            <tr>
               <td>
                  <h4>Vorname</h4>
               </td>
               <td>
                  <h4>Nachname</h4>
               </td>
               <td>
                  <h4>Status</h4>
               </td>
            </tr>
            <tr>
               <td>${x[0]}</td>
               <td>${x[1]}</td>
               <td>${x[2]}</td>
            </tr>
            % endfor
         </table>
         <table>
            <h1>Qualifikationen</h1>
            % for x in data_b:
            <tr>
               <td>
                  <h4>Qualifikation</h4>
               </td>
            </tr>
            <tr>
               <td>${x}</td>
            </tr>
            % endfor
         </table>
         <table>
            <h1>Zertifikate</h1>
            % for x in data_c:
            <tr>
               <td>
                  <h4>Zertifikat</h4>
               </td>
            </tr>
            <tr>
               <td>${x}</td>
            </tr>
            % endfor
         </table>
      </article>
   </section>
</body>
</html>