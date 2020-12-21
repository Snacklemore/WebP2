## coding: utf-8
<!DOCTYPE html>
<html>
<head>
   <title>Web-Teams</title>
   <meta charset="UTF-8" />
 <link rel="stylesheet" href="/webteams.css">
</head>
<body>
   <form id="idWTForm" action="/save?listform=${listform}" method="POST">
      <input type="hidden" value="${key_s}" id="id_spa" name="id_spa" />
      <div>
         <label for="name1_spa">1. Name</label>
         <input type="text"
                value="${data_o[0]}"
                id="name1_spa"
                name="name1_spa" required />
      </div>
      <div>
         <label for="vorname1_spa">1. Vorname</label>
         <input type="text"
                value="${data_o[1]}"
                id="vorname1_spa"
                name="vorname1_spa" required />
      </div>
      <div>
         <label for="matrnr1_spa">1. Matrikelnummer</label>
         <input type="number"
                value="${data_o[2]}"
                id="matrnr1_spa"
                name="matrnr1_spa" required />
      </div>
      <div>
          <label for="semesterzahl1_spa">1. Semesterzahl</label>
          <input type="number"
                 value="${data_o[3]}"
                 id="semesterzahl1_spa"
                 name="semesterzahl1_spa" required />
      </div>

	<div>
         <label for="name2_spa">2. Name</label>
         <input type="text"
                value="${data_o[3]}"
                id="name2_spa"
                name="name2_spa" required />
      </div>
      <div>
         <label for="vorname2_spa">2. Vorname</label>
         <input type="text"
                value="${data_o[4]}"
                id="vorname2_spa"
                name="vorname2_spa" required />
      </div>
      <div>
         <label for="matrnr2_spa">2. Matrikelnummer</label>
         <input type="number"
                value="${data_o[5]}"
                id="matrnr2_spa"
                name="matrnr2_spa" required />
      </div>
	<div>
                <label for="semesterzahl2_spa">2. Semesterzahl</label>
                <input type="number"
                        value="${data_o[7]}"
                        id="semesterzahl2_spa"
                        name="semesterzahl2_spa" required />
            </div>

      <div>
         <input type="submit" value="Speichern"/>
      </div>
   </form>
   <a href="/?listform=${listform}">Abbrechen</a>
</body>
</html>
