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
         <form id="idWTForm" action="/save_certificate" method="POST">
           
	    <input type="hidden" value="${t_id}" id="training_id" name="training_id" />
	<h1>Zertifikat hinzufügen</h1>	
            <div>
               <label for="title">Bezeichnung</label>
               <input type="text"
                  value=" "
                  id="title"
                  name="title" required />
            </div>
            <div>
               <label for="description">Beschreibung</label>
               <input type="text"
                  value=" "
                  id="description"
                  name="description" required />
            </div>
	    <div>
               <label for="entitled_to">Berechtigt zu</label>
               <input type="text"
                  value=" "
                  id="entitled_to"
                  name="entitled_to" required />
            </div>
	
	

		<div>
               <input type="submit" value="Speichern"/>
            </div>	
	
         </form>
      </article>
   </section>
</body>
</html>

