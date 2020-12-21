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
  <span style="float:right;">Gruppe / Team angeben</span>
  Mitarbeiterqualifizierung
  <br>
  Version xx / xx.xx.xxxx
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
    <h1>Zertifikate</h1>
	% for key_s in data_o:
        <table>
         <tr>
          <th>Name</th>
          <th>Kurzbeschreibung</th>
        
         </tr>
	  <td>${data_o[key_s][0]}</td>
          <td>${data_o[key_s][1]}</td>
	<h1>Zertifikat</h1>
	
		<tr>
		<th>Vorname</th>
		<th>Name</th>
            	</tr>
	 	% for x in data_o[key_s][3]:
	<table>
		
		
		
		<td> ${x[0]}</td>
		<td> ${x[1]}</td>
		
		<tr>
		 % endfor
		  
		
		 
		  
		
		
			
			
		
          </tr>
	</table>
        
	% endfor
      </table>
  </article>
</section>

</body>
</html>
