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
      <%
         nr_i = 0
      %>
      <ul>
         % for key_s in data_o:
         <%
            nr_i += 1
         %>
         <li>Team ${nr_i}:
            <a href="/edit/${key_s}?listform=${listform}">bearbeiten</a>
	    <a href="/delete/${key_s}?listform=${listform}" class="clDelete">Löschen</a>
            
            <ul>
                <li>${data_o[key_s][0]}, ${data_o[key_s][1]}, MatNr: ${data_o[key_s][2]}, Semester: ${data_o[key_s][3]}</li>
                <li>${data_o[key_s][4]}, ${data_o[key_s][5]}, MatNr: ${data_o[key_s][6]}, Semester: ${data_o[key_s][7]}</li>
            </ul>
         </li>
         % endfor
      </ul>
      <div>
         <a href="/add?listform=${listform}">Erfassen</a>
      </div>
      <div>
         <a href="/?listform=tabelle">Ansicht wechseln</a>
      </div>
   </body>
</html>
