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
        <form id="idWTForm" action="/save_employee_to_training" method="POST">
        <input type="hidden" value="${data_o}" id="employee_id" name="employee_id"/>
        <input type="hidden" value="${data_t}" id="training_id" name="training_id"/>
        <h1>Bitte wählen sie einen Trainingsstatus aus</h1>
        <br>
        <select name="participation_status" id="participation_status" form="idWTForm">
            <option>${data_p[0]}</option>
            <option>${data_p[1]}</option>
            <option>${data_p[2]}</option>
            <option>${data_p[3]}</option>
            <option>${data_p[4]}</option>
            <option>${data_p[5]}</option>
        <div>
            <input type="submit" value="Speichern"/>
        </div>
        </form>
    </article>
   </section>
</body>
</html>

