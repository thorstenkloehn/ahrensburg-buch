# Urheberrecht und Duplicate Content

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Diese Seite beantwortet drei Fragen, die bei einem KI-gestützten Wiki schnell aufkommen: Was schützt das Urheberrecht überhaupt – und was nicht? Wie stellt die Redaktion sicher, dass kein fremder Text ungefragt übernommen wird? Und schadet es der Auffindbarkeit bei Google, wenn sich Passagen mit anderen Websites ähneln (der sogenannte „Duplicate Content")?

## Was das Urheberrecht schützt – und was nicht

Das ist der wichtigste Punkt für ein Lexikon. Geschützt ist die **konkrete Ausdrucksform** eines Textes – Wortwahl, Satzbau, Gliederung –, sofern sie eine gewisse Eigenständigkeit erreicht. Das Gesetz nennt das „Schöpfungshöhe"; § 2 Abs. 2 UrhG verlangt „persönliche geistige Schöpfungen". **Nicht** geschützt sind die zugrunde liegenden Tatsachen, Zahlen, Daten, Ereignisse und Ideen. Das entspricht der allgemeinen Auffassung in der juristischen Literatur.

Vereinfacht gesagt: Die Einwohnerzahl Ahrensburgs ist eine bloße Tatsache und hat keine Schöpfungshöhe – aber *wie* eine Website sie in Sätze fasst, sehr wohl. Das Baujahr des Schlosses oder der Name einer Straße gehören niemandem; solche Angaben darf man aus jeder Quelle entnehmen und frei verwenden. Geschützt ist allein die fremde Formulierung.

Deshalb brauchen viele Seiten dieses Wikis gar keinen Herkunftshinweis: Wo sich lediglich einzelne Tatsachen mit einem Wikipedia-Artikel überschneiden, der Text aber eigenständig formuliert ist, entsteht keine Bearbeitung – und damit auch keine Attributionspflicht.

## Wie dieses Wiki Urheberrechte prüft

Die Prüfung ist ein **manueller redaktioneller Durchgang**, kein automatischer Scanner. Sie gehört zum [Co-Wiki-Prozess](co-wiki.md): Die KI liefert Entwürfe, ein Mensch prüft und gibt frei, die KI veröffentlicht nie eigenständig. Neue und überarbeitete Artikel durchlaufen dabei eine Redaktionspipeline aus mehreren spezialisierten Rollen – darunter ein Faktenchecker und ein Lektor.

Am 3. September 2026 wurden auf diese Weise **alle Inhaltsseiten** des Wikis noch einmal gezielt daraufhin durchgesehen, ob irgendwo fremder Text wörtlich übernommen wurde. Ergebnis: keine wörtliche Übernahme. Wo Seiten sich eng an eine Vorlage angelehnt hatten, wurden sie neu formuliert und mit einem Herkunftshinweis versehen (Beispiele weiter unten).

Eine **automatisierte Ähnlichkeitsprüfung** – etwa ein Abgleich neuer Absätze gegen bekannte Quellen vor jeder Veröffentlichung – ist bisher **nicht** eingebaut. Sie wäre ein denkbarer Ausbau; der Ist-Zustand ist die Kontrolle durch Menschen.

### Worauf die Redaktion achtet

- **Wörtlichkeit:** Stimmt eine Formulierung auffällig genau mit einer bekannten Quelle überein? Dann wird sie umgeschrieben oder als Zitat kenntlich gemacht.
- **Quellenangabe:** Ist belegt, woher eine Information stammt? Der Faktenchecker markiert jede Aussage als belegt, abweichend oder unbelegt.
- **Paraphrase mit zu wenig Abstand:** Auch das bloße Umstellen von Sätzen bei gleichem Aufbau kann zu nah am Original sein. Dann wird der Abschnitt aus eigenständig recherchierten Quellen neu aufgebaut.

Unsichere Stellen bleiben als sichtbarer Kommentar im Text stehen, bis ein Mensch sie geklärt hat – geraten wird nicht.

## Prüf-Prompts zum Selbernutzen

Die folgenden Prompts werden in diesem Wiki für den redaktionellen Durchgang eingesetzt. Sie lassen sich in Claude Code, ChatGPT oder einem anderen KI-Werkzeug verwenden, sobald der zu prüfende Entwurf – und möglichst auch die genannte Quelle – im Kontext liegt. Wer ein eigenes KI-gestütztes Wiki betreibt, kann sie als Prüfschritt vor jedem Commit einbauen.

- **Gesamtdurchgang (der Ausgangspunkt):**
  „Überprüfe alle Inhalte dieses Wikis daraufhin, ob sie fremdes Urheberrecht verletzen – wörtliche Übernahmen, eng angelehnte Paraphrasen, übersetzte Passagen. Gib eine Liste der auffälligen Seiten mit Fundstelle, vermuteter Quelle und Schweregrad." Die folgenden Prompts arbeiten die Treffer dann einzeln ab.

- **Wörtliche Übernahme finden:**
  „Vergleiche den folgenden Entwurf Absatz für Absatz mit dem Artikel *[Titel/URL]*. Markiere jede Stelle, an der Wortwahl oder Satzbau auffällig nah am Original liegen – etwa mehr als vier aufeinanderfolgende Wörter identisch oder nur trivial umgestellt. Gib je Fund den Entwurfssatz, die Vorlage und einen Umformulierungsvorschlag."

- **Faktenüberschneidung von Textbearbeitung unterscheiden:**
  „Dieser Abschnitt überschneidet sich thematisch mit *[Quelle]*. Entscheide begründet: reine Tatsachenüberschneidung – gleiche Zahlen und Ereignisse, aber eigenständige Formulierung, also kein Herkunftshinweis nötig – oder übernommene Struktur bzw. Formulierung, also Herkunftshinweis nötig?"

- **Lizenz der Quellen einordnen:**
  „Liste alle externen Quellen und Weblinks dieser Seite auf. Ordne jede ein: freie Lizenz (CC BY, CC BY-SA, gemeinfrei, amtliches Werk nach § 5 UrhG) oder ‚alle Rechte vorbehalten'. Bei geschützten Quellen: prüfe, ob Text daraus übernommen wurde oder ob nur verlinkt wird."

- **Attributionsblock prüfen:**
  „Diese Seite beruht laut Herkunftshinweis auf einem Wikipedia-Artikel. Prüfe, ob der Abschnitt ‚Wikipedia als Quelle' alle vier Anforderungen der Lizenz CC BY-SA 4.0 erfüllt: Autorennennung mit Link auf den Artikel, Lizenzangabe mit Link, Änderungshinweis, Weitergabe unter gleicher Lizenz."

- **Dopplungen im eigenen Wiki:**
  „Durchsuche alle Seiten dieses Repos auf Textdopplungen – Absätze, die fast wörtlich auf mehreren Seiten stehen. Gib die Fundstellen und einen Vorschlag, welche Seite den Absatz behält und wie die andere ihn durch einen Querverweis ersetzt."

Diese Prompts ersetzen die menschliche Freigabe nicht – sie bereiten sie vor. Jeder Treffer wird von einem Menschen bewertet.

## Texte aus Wikipedia: Attribution richtig machen

Wikipedia-Artikel stehen unter der freien Lizenz CC BY-SA 4.0. Man darf sie weiternutzen und auch bearbeiten – aber nur, wenn man die Lizenzbedingungen einhält. Eine gesonderte Genehmigung braucht es dafür nicht. Nach der Anleitung [Wikipedia:Weiternutzung](https://de.wikipedia.org/wiki/Wikipedia:Weiternutzung) sind vier Dinge nötig:

- **Autoren nennen.** Bei Online-Nutzung genügt ein Link auf den Wikipedia-Artikel, über den die Versionsgeschichte erreichbar ist.
- **Lizenz angeben:** „CC BY-SA 4.0", mit Link.
- **Änderungen kenntlich machen.**
- **Weitergabe unter derselben Lizenz** (dazu unten mehr).

Einige ältere Seiten enthalten noch bearbeitete Wikipedia-Inhalte. Dort dokumentiert ein eigener Quellenabschnitt den Artikel, die Lizenz und die vorgenommenen Änderungen. Neu bearbeitete Seiten sollen stattdessen möglichst auf amtlichen oder lokalen Primärquellen beruhen und einen eigenständigen Aufbau erhalten.

## Eng an einer Vorlage? Dann neu schreiben

Die Seite zur [Verkehrsanbindung](verkehrsanbindung.md) war ursprünglich eine enge Verdichtung des Verkehrs-Abschnitts aus dem Wikipedia-Artikel über Ahrensburg. Sie wurde vollständig neu formuliert. Dabei fiel auch ein Sachfehler auf: Die Regionalexpress-Linie war als „RE 8" bezeichnet, richtig ist „RE 80".

Beim selben Urheberrechts-Durchgang zeigte sich zudem, dass eine Angabe im Wikipedia-Artikel selbst nicht stimmte: die Sitzverteilung der Ahrensburger Stadtvertretung von 2023. Die eigene Recherche ergab Grüne 9, CDU 9, SPD 6, WAB 4, FDP 3 – der Wikipedia-Wert war falsch. Eigenständiges Nacharbeiten schützt also nicht nur vor Urheberrechtsproblemen, es verbessert oft auch die Qualität.

## Geschützte Quellen und amtliche Werke

Nicht jede Quelle im Internet ist frei nutzbar. Proprietäre regionale Facharchive und Lexika stehen oft unter dem Schutz „alle Rechte vorbehalten" und bieten keine freie Lizenz. Für dieses Wiki gilt deshalb die strikte Richtlinie: niemals Text aus solchen geschützten Vorlagen übernehmen, eng paraphrasieren oder übersetzen. Fremde urheberrechtlich geschützte Inhalte dürfen keinesfalls in Artikel einfließen.

Anders liegt der Fall bei **amtlichen Werken** nach [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html). Gesetze, Verordnungen, Erlasse und amtliche Bekanntmachungen genießen keinen Urheberrechtsschutz. Deshalb darf zum Beispiel die amtliche Wappenbeschreibung – die *Blasonierung*, die heraldische Fachbeschreibung eines Wappens – wörtlich zitiert werden; sie ist gemeinfrei und über die Kommunale Wappenrolle Schleswig-Holsteins belegt. Wichtig: § 5 betrifft nur das Urheberrecht am Text. Die *Verwendung* eines Wappens als Hoheitszeichen ist davon unabhängig kommunalrechtlich geregelt (mehr dazu auf der Seite [Wappen und Flagge](stadtwappen.md)).

## Freie Lizenzen verstehen: CC BY-SA

Dieses Wiki steht vollständig unter der [Lizenz CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (siehe [Impressum](impressum.md)). Die beiden Kürzel bedeuten:

- **BY (Namensnennung):** Wer Inhalte weiternutzt, muss die Urheber angemessen nennen, die Lizenz angeben und auf sie verlinken und kenntlich machen, dass etwas geändert wurde. Dieser Änderungshinweis ist in der Version 4.0 ausdrücklich verpflichtend.
- **SA (Share-Alike, „Weitergabe unter gleichen Bedingungen"):** Bearbeitungen müssen wieder unter CC BY-SA 4.0 gestellt werden. Dieses „Copyleft" – die Pflicht, Abgeleitetes unter derselben freien Lizenz weiterzugeben – hält die Inhalte dauerhaft frei.

Praktischer Nebeneffekt: Weil Wikipedia und dieses Wiki dieselbe Lizenz verwenden, passt die Weiternutzung in beide Richtungen ohne Lizenzkonflikt zusammen. Die Share-Alike-Bedingung ist damit automatisch erfüllt.

## Zitatrecht: Fachquellen sauber einbauen

Manchmal soll eine geschützte Quelle nicht nur verlinkt, sondern wörtlich wiedergegeben werden – als Beleg oder um sich mit einer Aussage auseinanderzusetzen. Dafür gibt es das Zitatrecht in [§ 51 UrhG](https://www.gesetze-im-internet.de/urhg/__51.html). Eine Übernahme ist danach zulässig „zum Zweck des Zitats, sofern die Nutzung in ihrem Umfang durch den besonderen Zweck gerechtfertigt ist".

Vereinfacht gesagt müssen dafür mehrere Bedingungen zusammenkommen: Es braucht einen echten **Zitatzweck** (Beleg oder inhaltliche Auseinandersetzung, nicht bloße Ausschmückung), das Zitat muss als solches erkennbar und **unverändert** sein, sein Umfang darf nicht über den Zweck hinausgehen, und es braucht eine **Quellenangabe** (§ 63 UrhG). Ein Zitat ersetzt also keine eigene Darstellung – es stützt sie.

## Duplicate Content und Google

Ähnliche Texte führen nicht automatisch zu einer Sanktion. Google unterscheidet zwischen gewöhnlichen Dopplungen und Inhalten, die Suchergebnisse gezielt beeinflussen sollen. Das erläutert ein Beitrag von [Google Search Central aus dem Jahr 2008](https://developers.google.com/search/blog/2008/09/demystifying-duplicate-content-penalty).

Findet Google mehrere weitgehend gleiche Seiten, bestimmt das System eine davon als hauptsächliche Fassung. Die anderen können seltener durchsucht oder nicht als eigener Treffer angezeigt werden. Die [Google-Dokumentation zur Kanonisierung](https://developers.google.com/search/docs/crawling-indexing/canonicalization) beschreibt dieses Auswahlverfahren. Einen allgemein gültigen Prozentwert, ab dem Texte als Duplikat gelten, nennt Google dort nicht.

### Warum eigenständige Formulierung trotzdem lohnt

Eigenständige Texte geben Suchmaschinen und Lesenden einen Grund, diese Seite neben anderen Quellen zu berücksichtigen. Deshalb setzt das Wiki auf lokale Recherche, eine eigene Gliederung und Querverweise innerhalb des Stadtbuchs.

## Diese Seite ist keine Rechtsberatung

Sie fasst öffentlich zugängliche Informationen allgemeinverständlich zusammen; die rechtlichen Aussagen sind vereinfacht und als solche gekennzeichnet („nach allgemeiner Auffassung", „vereinfacht gesagt"). Ein Hinweis zur Rechtslage: Der früher für die „freie Benutzung" einschlägige § 24 UrhG a. F. ist seit dem 7. Juni 2021 aufgehoben; die Frage des nötigen Abstands zu einer Vorlage richtet sich heute nach [§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html), der einen „hinreichenden Abstand" zum benutzten Werk verlangt.

Stand: 3. September 2026. Angaben ohne Gewähr; Gesetze, Gerichtsentscheidungen und die Praxis von Suchmaschinen können sich ändern. Verbindliche Auskünfte gibt nur eine fachkundige Rechtsberatung. Weitere Angaben zu Betreiber und Lizenz stehen im [Impressum](impressum.md), Hinweise zur Datenverarbeitung unter [Datenschutz](datenschutz.md).

## Verwandte Seiten

- [Co-Wiki: Mensch & KI](co-wiki.md)
- [Neue Artikel aus Rohfassungen erstellen](neue-artikel-erstellen.md)
- [Wissen speichern](wissen-speichern.md)
- [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md)
- [LLM Wiki](llm-wiki.md)
- [Impressum](impressum.md)
- [Datenschutz](datenschutz.md)
- [Wappen und Flagge](stadtwappen.md)
- [Ahrensburger Tunneltal und die Ahrensburger Kultur](ahrensburger-tunneltal.md)
- [Schloss Ahrensburg](schloss-ahrensburg.md)
- [Verkehrsanbindung](verkehrsanbindung.md)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
