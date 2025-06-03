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

= Lidar
== Aufbau
Im folgendem Versuch wird der Thymio II mit einem Lidar an seiner Vorderspitze ausgestattet. Er wird mit drei Wänden umringt und wird durch seine Motoren zum drehen gebracht. Währenddessen wird das Lidar eingeschaltet und die gesammelten Abstandsdaten aufgezeichnet. Das Lidar arbeitet dabei mit einem Blickfeld von ca. 90° nach Vorne, 6 Strahlenschichten und einer horizontalen Auflösung von 512.
== Ergebnisse
#figure(image("result_images/lidarImage1.png"), caption: [Lidarergebniss ohne Wand])
#figure(image("result_images/lidarImage2.png"), caption: [Lidarergebniss mit Wand])
In den gezeigten Bildern ist die "Sicht" des Lidars im 3D-Raum zu erkennen. Wobei die blauen Punkte die maximale Reichweite des Lidar zeigen, ist durch die Roten Punkte im die Wand gekennzeichnet, in dessen Richtung der Thymio II sich dreht. Im Bild lässt sich somit nicht nur die Position des Objektes in Relation zum Roboter entnehmen, sondern auch seine From.
== Physikalische Prinzipien
Ein Lidar funktioniert ähnlich wie ein Sonar oder Radar über das Aussenden eines Signals und das Auswerten der Reflektion des Signals. Wobei das Sonar und Radar, Schall und elekrtomagnetische Strahlung als Signal nutzen, nutzt das Lidar ausgestrahltes Licht. Das Lidar strahlt dabei einen oder mehrere konzentrierte Lichtstrahlen aus. Diese werden dann durch Objekte in der Umgebung reflektiert und in das Lidar zurückgestrahlt. Durch das messen der vergangenen Zeit zwischen Ausstrahlung und Einfangen eines Strahls kann dann die entferung des Objektes ermittelt werden. Mit Hilfe weiteren Strahlen, deren Reflektion und Winkel, kann dann eine sogenannte Punktwolke gebildet werden, die z.B.: die Form eines Objektes wiederspiegelt.  
== Mögliche Szenarien
Mögliche Einsatzgebiete sind die Umgebungs und Objekterkennung. Optimalerweise in Kombination mit weiteren Sensoren, wie zum Beispiel einer Kamera mit Bilderkennung.


= TouchSensor
== Aufbau
In diesem Versuch wurde ein IPR-Roboterarm mit einem TouchSensor ausgestattet. Der Versuchsablauf sieht vor, dass der Roboterarm nacheinander gegen zwei Blöcke drückt: Einer der Blöcke ist starr befestigt und gibt nicht nach, während der andere beweglich ist und sich unter Krafteinwirkung verschiebt.

#figure(image("result_images/touch_sensor.jpg"), caption: [Aufbau des TouchSensor-Experiments mit Roboterarm und Blöcken])

== Ergebnisse
#figure(image("result_images/ForceTime.png"), caption: [Gemessene Kraft des TouchSensors über die Timesteps des Experiments])<forcetime>
#ref(<forcetime>) zeigt den Kraftverlauf, der am TouchSensor ts1 während des Experiments gemessen wurde. Ab Timestep 71 ist ein deutlicher Anstieg der gemessenen Kraft zu erkennen, weil der Roboterarm hier in Kontakt mit dem unbeweglichen Block kommt. Da dieser nicht nachgibt, bleibt die Kraft bis Timestep 123 auf einem konstant hohen Niveau. Anschließend bricht der Roboter den Versuch ab und wechselt seine Position, um auf den zweiten, beweglichen Block zu treffen.

In den Timesteps 125–131 sowie bei Timestep 166 sind kleinere Kraftspitzen zu beobachten, die auf die Bewegung zurückzuführen sind. Danach folgt eine weitere, deutlich erkennbare Spitze: Der Roboterarm trifft auf den beweglichen Block. Da dieser nachgibt, fällt die gemessene Kraft sofort wieder ab. Ein zweiter Kontakt führt zu einer erneuten Spitze, bevor der Block schließlich außer Reichweite gerät und sich die Kraftmessung auf den Ausgangswert zurückpendelt.

== Physikalische Prinzipien
Ein TouchSensor misst Kraft bzw. Druck, indem er mechanische Deformation in ein elektrisches Signal umwandelt. Dies geschieht häufig mittels piezoelektrischer Materialien oder Dehnungsmessstreifen, die ihren elektrischen Widerstand bei Verformung ändern. Das zugrundeliegende physikalische Prinzip ist das Hooke’sche Gesetz, welches einen linearen Zusammenhang zwischen Kraft und Deformation beschreibt (F = k·x), solange die Verformung im elastischen Bereich bleibt.

== Mögliche Szenarien
TouchSensoren sind in der Robotik vielseitig einsetzbar. Ein Anwendungsfeld ist die Erkennung von Kollisionen mit einem Bumper. 

Ein weiteres Anwendungsfeld ist die Erkennung der Materialeigenschaften von Objekten. Ein "weiches" Objekt gibt bei Kontakt nach, bei starren Objekten bleibt die Kraft hingegen konstant.

Zudem können TouchSensoren zur Gewichtsschätzung genutzt werden, wenn ein Roboterarm ein Objekt anhebt und die dabei wirkende Gewichtskraft registriert.

Ein weiterer wichtiger Aspekt ist die Sicherheit: Bei Überschreiten eines definierten Kraftgrenzwertes kann der Roboter automatisch stoppen, um Schäden an sich selbst oder an seiner Umgebung zu vermeiden. Besonders in der Zusammenarbeit mit Menschen. Bei sogenannten kollaborativen Robotern (Cobots) ist diese Fähigkeit essenziell, um eine Sichere Zusammenarbeit von Mensch und Maschiene zu ermöglichen.