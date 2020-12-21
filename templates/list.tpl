## coding: utf-8
<!DOCTYPE html>
<html>
   <head>
      <title>Web-Teams</title>
      <meta charset="UTF-8" />
      <link rel="stylesheet" href="/webteams.css"/>
      <script type="text/javascript" src="/webteams.js"></script>
   </head>
   <body>
      <table>
         <tr>
            <th>Name (1)</th>
                <th>Vorname (1)</th>
                <th>Matr.-Nr. (1)</th>
                <th>Semesterzahl (1)</th>
                <th>Name (2)</th>
                <th>Vorname (2)</th>
                <th>Matr.-Nr. (2)</th>
                <th>Semesterzahl (2)</th>
                <th>Aktion</th>

         </tr>
         % for key_s in data_o:
         <tr>
            <td>${data_o[key_s][0]}</td>
            <td>${data_o[key_s][1]}</td>
            <td>${data_o[key_s][2]}</td>
	    <td>${data_o[key_s][3]}</td>
            <td>${data_o[key_s][4]}</td>
            <td>${data_o[key_s][5]}</td>
            <td>${data_o[key_s][6]}</td>
            <td>${data_o[key_s][7]}</td>

            <td>
		<a href="/edit/${key_s}?listform=${listform}">bearbeiten</a>
		<a href="/delete/${key_s}?listform=${listform}" class="clDelete">Löschen</a>
		
	    </td>

         </tr>
         % endfor
      </table>
      <div>
         <a href="/add?listform=${listform}">erfassen</a>
	 <a href="/?listform=liste">Ansicht ändern</a>
      </div>
   </body>
</html>
