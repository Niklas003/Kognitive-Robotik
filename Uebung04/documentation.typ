#import "@preview/ilm:1.4.1": *

#set text(lang: "de")

#show: ilm.with(
  title: [Kognitive Robotik Übung IV],
  author: "
Dennis Podkolsin
Malte Eisermann 
Niklas Labitzke",
  date: datetime(year: 2025, month: 07, day: 02),
  figure-index: (enabled: true),
  table-index: (enabled: true),
  listing-index: (enabled: true),
)
= Ergebnisdiskussion

== Aufgabe 1 Neue Parameter für schnellere Bewegung

Der erste Schritt zur Lösung dieser Aufgabe war es, den Effekt der vorhandenen Parameter zu erkennen und festzuhalten. Dadurch wurde, als erste Verbesserung der Laufgeschwindigkeit, der Parameter "f" identifiziert. Er regelt die Frequenz der Schritte des Nao. Durch das alleinige Erhöhen dieses Wertes, konnte Laufgeschwindigkeit von 01:53:76 (f = 4) auf 01:18:56 (f = 6) gesteigert werden.
Bei einer weiteren Steigerung von "f" (auf Werte höher als 6) endete die Bewegung des Naos im Verlust seiner Stabilität und einem Sturz auf den Boden. 
Folgende Experimente dienten der Klarstellung einiger weiterer Tatsachen. Wie dass, das alleinige Erhöhen anderer Werte ebenfalls keine Erfolg darstellte. Sowie als auch das gemeinsame, gleichmäßige Steigern aller Parameter via eines Multiplikators.

[MALTE hier deinen Workflow eingeben]

== Aufgabe 2 Seitwärtslaufen
Die Lösung bedient sich an dem bereits vorhandenem Code aus den walk_forward controller. Anders als beim Vorwärtslaufen sorgt der x Wert nun dafür dass der Nao nicht im Kreis läuft. Anstatt dass die Beine nach vorne bewegt werden, werden diese zur Seite bewegt. Zusätzlich schwingen die Arme mit um die Seitwärtsbewegung zu stabilisieren. Es ist im Grunde eine recht simple Lösung in welcher die Bewegungslogik an der x-Achse auf die y-Achse übertragen wurde. Die Lösung sorgt aber dennoch dafür dass ohne viel zusätzliche Logik dass sich der Nao lateral bewegen kann.

Instabil wird die Bewegung durch den Ankle Pitch des Beines welches immer wieder herangezogen wird. Der Nao bewegt sich nicht gerade an seiner y-Achse entlang sondern läuft im Kreis (welcher jedoch einen recht großen Radius hat) trotz der x-Wert Korrektur.

Des Weiteren ist der Roboter in einer ständigen Pendelbewegung, was dazu führt dass auch bei kleineren Änderungen der Parameter es zum Sturz kommen kann. Ein abruptes umschalten der Modi könnte ebenfalls zu einer sturzgefährdenden Instabilität führen. Verbesserungspotential gibt es also in folgenden Bereichen:

- Ankle Roll während heranziehen des Beines
- geradlinige Seitwärtsbewegung
- Stabilität herstellen sollte der Modus gewechselt werden


== Aufgabe 3 Drehbewegung auf der Stelle

== Aufgabe 4 Aktive Stabilisierung mit Hilfe von IMU Sensoren
Aufbauend auf der Lösung von Aufgabe 1, wurde der Code um einige Funktionen erweitert. Als Erstes wurde die vorhandene Logik, zur Stabilisierung des Roboters, entfernt. Sie beinhaltete eine einfache Armschwungbewegung, die zeitgleich zur Beinbewegung durchgeführt wurde. Anschließend wurde die Entscheidung getroffen die Daten des, sich an Bord des Nao befindlichen, Gyroskopes zu Nutzen, um eine aktive Stabilisierung des Roboters verwirklichen.

Der Controller wurde um drei neue Funktionen erweitert, die gemeinsam die Daten des Gyroskops speichern, vergleichen und für eine Entscheidungsfindung nutzen.
Die Gyroskopdaten werden in einem "Kurzzeitgedächnis" gespeichert (ein Tupel mit den neusten Datensätzen des Gyroskops). Nachfolgend wird die Differenz der Yaw Werte, der zwei jüngsten Datensätze, errechnet. Aus dieser Differenz lässt sich die aktuelle Drehbewegung des Naos ermitteln. Diese Drehbewegung kann nun mit der richtigen Armbewegung neutralisiert werden.

- Bewegung nach Links:
    - Linker Arm nach Vorne
    - Rechter Arm nach Hinten
- Bewegung nach Rechts:
    - Linker Arm nach Hinten
    - Rechter Arm nach Vorne

Nachdem der Nao jetzt stabil laufen konnte, wurde bei dem Ausführen des Codes ein starker Linksdrall in der Laufbewegung entdeckt. Der Nao war zwar in der Lage, die Welt stabil zu durchqueren, jedoch konnte das Ende der Rennstrecke nicht erreicht werden. Beim Laufen stolperte der Nao und kam etwas ins Wanken, dadurch änderte sich die Laufrichtung und die Strecke wurde verlassen. Um dies zu beheben wurden die Parameter, die aus der Lösung der ersten Aufgabe hervorkamen, weiter bearbeitet. Trial and Error verfeinerten das Ergebis, bis der Nao schließlich das Ende der Strecke mit einer Zeit von 00:16:55 erreichte. Seine Zeit konnte sogar etwas verbessert werden, wenn auch die Laufspur im Eifer des Gefechts einmal gewechselt wurde.

Als Mögliche Verbesserung des Controllers, wäre eine adaptive Armbewegung möglich. Diese Armbewegung könnte durch die Stärke der Drehbewegung des Naos beinflusst werden und so eine effektivere Neutraliesierung erzeugen. 
