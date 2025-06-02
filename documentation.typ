#import "@preview/ilm:1.4.1": *

#set text(lang: "de")

#show: ilm.with(
  title: [Kognitive Robotik Übung II],
  author: "
Dennis Podkolsin
Malte Eisermann 
Niklas Labitzke",
  date: datetime(year: 2025, month: 06, day: 04),
  figure-index: (enabled: true),
  table-index: (enabled: true),
  listing-index: (enabled: true),
)
= Gyroskop
== Aufbau
In einem einfachen Versuchsaufbau wird der Thymio II mit einem Gyroskop ausgestattet. Dieses misst über die Timesteps hinweg die Winkelgeschwindigkeit entlang der Z-Achse des Roboters. Um die Funktion des Gyroskops zu veranschaulichen werden im Controller des Thymio II die Geschwindigkeiten der einzelnen Motoren (links und rechts) zufällig Generiert. Dabei bewegen sich die einzelnen Motoren immer in gegengesetzter Richtung.

== Ergebnisse
#figure(
image("result_images/Gyro_plot.svg"), caption: [Beispielhaftes Ergebnis des Versuchsaufbaus mit dem Gyroskop])

Durch das "wackeln" des Roboters entlag der Z-Achse entstehen die entsprechenden Ausschläge. Aufgrund der zufälligen Geschwindigkeiten der einzelnen Räder in jeweils entgegengesetzte Richtungen können die einzelnen Ausschläge größer bzw. kleiner ausfallen. Je nachdem ob sich der Roboter in einem Moment nach links bzw. rechts dreht können Ausschläge im positiven bzw. negativem Messbereich ausgemacht werden. Klar zu erkennen ist auch, dass der Thymio II während des gesamten Versuches sich zu keinem Zeitpunkt linear in eine Richtung bewegt hat. Dies hätte nämlich zu Folge, dass in der Aufzeichnung eine Winkelgeschwindigkeit um die Z-Achse von 0 zu verzeichnen wäre.


== Physikalische Prinzipien
Ein zentrales physikalisches Prinzip, auf dem ein Gyroskop basiert, ist die Erhaltung des Drehimpulses. Der Drehimpuls eines rotierenden Körpers bleibt in einem abgeschlossenen System konstant, sofern keine äußeren Drehmomente wirken. Dies bedeutet, dass ein rotierender Kreisel (wie es z.B. bei einem Gyroskop der Fall ist) seine Ausrichtung im Raum beibehält, was ihn zu einem zuverlässigen Referenzpunkt für die Orientierung macht.

Wie bereits im Versuchsaufbau angedeutet wird mit einem Gyroskop die Winkelgeschwindigkeit um eine Achse (X, Y, Z) gemessen. Beispielswiese in °/s oder rad/seine
== Mögliche Szenarien
Mögliche Anwendungsfelder in der Robotik sind z.B Drohnen. Hier können Gyroskope eingesetzt werden um bestimmte Manöver zu kontrollieren/messen (z.B. Rollen um X/Y-Achse) oder um Kurskorrekturen vorzunehmen.

= Sonar
== Aufbau
In diesem Versuch wurde der Thymio II Roboter mit einem Sonar ausgestattet. Dabei fährt der Roboter unter einer Wand eintlang und fährt anschließend auf eine weitere zu. Hierbei wird die Distanz nach "oben" bzw. nach "vorne" gemessen. Das Sonar hat dabei eine Auflösung von 7, eine Apartur von 1,56 und ist mit 10 Rays ausgestattet. Die Geschwindigkeit mit welcher sich der Roboter bewegt wird mit jedem Timestep zufällig gewählt und bewegt sich zwischen 1 und 0,1.
== Ergebnisse
#figure(image("result_images/Sonar_plot.svg"), caption: [Ergebnis des Versuchsaufbaus mit dem Sonar])
In dem Ergebnisdiagramm wird über die Zeit (Timesteps) hinweg die Distanz zu einem Objekt dargestellt. Im ersten Abschnitt des Diagrammes (bis Timestep 5000) fährt der Roboter auf eine über ihm schwebende Wand zu. Hierbei verrinngert sich die Distanz zum Objekt, welches auch vom Sonar erfasst wird. Ca. ab Timestep 35000 erfasst das Sonar wieder ein sich näherndes Objekt an welches bis auf Distanz = 0 herangefahren wird. Danch steigt die vom Sonar erfasste Distanz stark an, was jedoch an der Positionierung des Sonars liegt. Zu beachten ist, dass in Webots Sonarwellen welche aus weniger als 22,5° auf ein Objekt treffen keinen Distanzwert liefern um den physikalischen Gesetzmäßigkeiten gerecht zu werden. 
== Physikalische Prinzipien
Ein Sonar nutzt die Eigenschaft aus, dass Schallwellen, insbesondere Ultraschallwellen an Objekten reflektiert werden (Beispiel: Echo in einer Höhle). Dabei misst ein Sonar die Zeit wie lange es dauert bis Schallwellen auf ein Objekt treffen und dann zum Ausgangspunkt reflektiert werden. Hieraus kann dann die Entfernung zu dem reflektierenden Objekt errechnet werden. Zu beachten ist, dass Objekte von denen Schallwellen reflektiert werden sich nicht unmittelbar vor/unter/über dem Sonar befinden müssen, da die ausgesendeten Schallwellen sich im Raum Kegelförmig ausbreiten und somit auch von Objekten reflektiert werden können welche sich in einem bestimmten Winkel zum Sonar befinden.
== Mögliche Szenarien
Mögliche Einsatzfelder für Sonare in der Robotik könnten bspw. Roboter sein welche sich unter Wasser bewegen. Sonare könnten zur Kollisionsvermeidung oder auch Kartierung vom Meeresgrund eingesetzt werden.