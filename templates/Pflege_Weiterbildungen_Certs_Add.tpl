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
         <form id="idWTForm" action="/savecert" method="POST">
           
	    
	<h1>Zertifikat hinzufügen</h1>	
		
		 	
            <div>
               <label for="bezeichnungc_spa">Bezeichnung</label>
               <input type="text"
                  value=" "
                  id="bezeichnungc_spa"
                  name="bezeichnungc_spa" required />
            </div>
            <div>
               <label for="beschreibung_spa">Beschreibung</label>
               <input type="text"
                  value=" "
                  id="beschreibung_spa"
                  name="beschreibung_spa" required />
            </div>
	    <div>
               <label for="berechtigung_spa">Berechtigt zu</label>
               <input type="text"
                  value=" "
                  id="berechtigung_spa"
                  name="berechtigung_spa" required />
            </div>
	
	

		<div>
               <input type="submit" value="Speichern"/>
            </div>	
	
         </form>
      </article>
   </section>
</body>
</html>

