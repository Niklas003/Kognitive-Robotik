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

== Aufgabe 2 Seitwärtslaufen
Die Lösung bedient sich an dem bereits vorhandenem Code aus den walk_forward controller. Anders als beim Vorwärtslaufen sorgt der x Wert nun dafür dass der Nao nicht im Kreis läuft. Anstatt dass die Beine nach vorne bewegt werden, werden diese zur Seite bewegt. Zusätzlich schwingen die Arme mit um die Seitwärtsbewegung zu stabilisieren. Es ist im Grunde eine recht simple Lösung in welcher die Bewegungslogik an der x-Achse auf die y-Achse übertragen wurde. Die Lösung sorgt aber dennoch dafür dass ohne viel zusätzliche Logik dass sich der Nao lateral bewegen kann.

Instabil wird die Bewegung durch den Ankle Pitch des Beines welches immer wieder herangezogen wird. Der Nao bewegt sich nicht gerade an seiner y-Achse entlang sondern läuft im Kreis (welcher jedoch einen recht großen Radius hat) trotz der x-Wert Korrektur.

Des Weiteren ist der Roboter in einer ständigen Pendelbewegung, was dazu führt dass auch bei kleineren Änderungen der Parameter es zum Sturz kommen kann. Ein abruptes umschalten der Modi könnte ebenfalls zu einer sturzgefährdenden Instabilität führen. Verbesserungspotential gibt es also in folgenden Bereichen:

- Ankle Roll während heranziehen des Beines
- geradlinige Seitwärtsbewegung
- Stabilität herstellen sollte der Modus gewechselt werden
