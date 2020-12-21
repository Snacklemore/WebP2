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
         <form id="idWTForm" action="/save" method="POST">
            <input type="hidden" value="${key_s}" id="id_spa" name="id_spa" />
            <div>
               <label for="name_spa">Name</label>
               <input type="text"
                  value="${data_o[0]}"
                  id="name_spa"
                  name="name_spa" required />
            </div>
            <div>
               <label for="vorname_spa">Vorname</label>
               <input type="text"
                  value="${data_o[1]}"
                  id="vorname_spa"
                  name="vorname_spa" required />
            </div>
            <div>
               <label for="akademic_spa">akademischer Grad</label>
               <input type="text"
                  value="${data_o[2]}"
                  id="akademic_spa"
                  name="akademic_spa" required />
            </div>
            <div>
               <label for="tatigkeit_spa">Tätigkeit</label>
               <input type="text"
                  value="${data_o[3]}"
                  id="tatigkeit_spa"
                  name="tatigkeit_spa" required />
            </div>
            <div>
               <input type="submit" value="Speichern"/>
            </div>
         </form>
      </article>
   </section>
</body>
</html>

