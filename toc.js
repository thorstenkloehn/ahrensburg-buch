// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded affix "><a href="hauptseite.html">Startseite</a></li><li class="chapter-item expanded affix "><a href="neue-artikel-erstellen.html">Neue Artikel</a></li><li class="chapter-item expanded affix "><a href="llm-wiki.html">LLM Wiki</a></li><li class="chapter-item expanded affix "><a href="wissen-speichern.html">Wissen speichern</a></li><li class="chapter-item expanded affix "><a href="urheberrecht-und-duplicate-content.html">Urheberrecht und Duplicate Content</a></li><li class="chapter-item expanded affix "><a href="wissenssysteme-im-vergleich.html">Wissenssysteme im Vergleich</a></li><li class="chapter-item expanded affix "><a href="wikis-im-vergleich.html">Wiki-Programme im Vergleich</a></li><li class="chapter-item expanded affix "><a href="cms-im-vergleich.html">CMS im Vergleich</a></li><li class="chapter-item expanded affix "><a href="cms-millionen-artikel.html">Wie CMS mit Millionen Artikeln umgehen</a></li><li class="chapter-item expanded affix "><a href="doku-generatoren-im-vergleich.html">Doku-Generatoren im Vergleich</a></li><li class="chapter-item expanded affix "><a href="webframeworks-im-vergleich.html">Webframeworks im Vergleich</a></li><li class="chapter-item expanded affix "><a href="wissenssystem-selbst-bauen.html">Ein Wissenssystem selbst bauen</a></li><li class="chapter-item expanded affix "><li class="part-title">Ahrensburg – Allgemeines</li><li class="chapter-item expanded "><a href="geschichte-allgemeines.html"><strong aria-hidden="true">1.</strong> Geschichte &amp; Allgemeines</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="geschichte-der-stadt-ahrensburg.html"><strong aria-hidden="true">1.1.</strong> Geschichte der Stadt Ahrensburg</a></li><li class="chapter-item expanded "><a href="ortsname-ahrensburg.html"><strong aria-hidden="true">1.2.</strong> Der Ortsname: Von „Arnesvelde“ zu Ahrensburg</a></li><li class="chapter-item expanded "><a href="ahrensburg-ns-zeit.html"><strong aria-hidden="true">1.3.</strong> Ahrensburg in der NS-Zeit</a></li><li class="chapter-item expanded "><a href="stadtwerdung-1949.html"><strong aria-hidden="true">1.4.</strong> Stadtwerdung 1949</a></li><li class="chapter-item expanded "><a href="familie-rantzau.html"><strong aria-hidden="true">1.5.</strong> Die Familie Rantzau als Schlossherren</a></li><li class="chapter-item expanded "><a href="familie-schimmelmann.html"><strong aria-hidden="true">1.6.</strong> Die Familie Schimmelmann als Schlossherren</a></li><li class="chapter-item expanded "><a href="persoenlichkeiten.html"><strong aria-hidden="true">1.7.</strong> Persönlichkeiten der Stadt</a></li><li class="chapter-item expanded "><a href="stadtwappen.html"><strong aria-hidden="true">1.8.</strong> Wappen und Flagge</a></li><li class="chapter-item expanded "><a href="demografie.html"><strong aria-hidden="true">1.9.</strong> Demografie und Bevölkerungsentwicklung</a></li><li class="chapter-item expanded "><a href="geografie.html"><strong aria-hidden="true">1.10.</strong> Geografie</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="gewaesser-und-seen.html"><strong aria-hidden="true">1.10.1.</strong> Gewässer und Seen</a></li><li class="chapter-item expanded "><a href="naturschutzgebiete.html"><strong aria-hidden="true">1.10.2.</strong> Naturschutzgebiete</a></li><li class="chapter-item expanded "><a href="fauna-und-flora.html"><strong aria-hidden="true">1.10.3.</strong> Fauna und Flora</a></li></ol></li><li class="chapter-item expanded "><a href="ahrensburger-tunneltal.html"><strong aria-hidden="true">1.11.</strong> Ahrensburger Tunneltal und die Ahrensburger Kultur</a></li></ol></li><li class="chapter-item expanded "><a href="sehenswuerdigkeiten-kultur.html"><strong aria-hidden="true">2.</strong> Sehenswürdigkeiten &amp; Kultur</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="sehenswuerdigkeiten.html"><strong aria-hidden="true">2.1.</strong> Sehenswürdigkeiten</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="schloss-ahrensburg.html"><strong aria-hidden="true">2.1.1.</strong> Schloss Ahrensburg</a></li><li class="chapter-item expanded "><a href="schlosskirche-ahrensburg.html"><strong aria-hidden="true">2.1.2.</strong> Schlosskirche Ahrensburg</a></li><li class="chapter-item expanded "><a href="gottesbuden.html"><strong aria-hidden="true">2.1.3.</strong> Die Gottesbuden</a></li></ol></li><li class="chapter-item expanded "><a href="musik-und-theater.html"><strong aria-hidden="true">2.2.</strong> Musik und Theater</a></li><li class="chapter-item expanded "><a href="regelmaessige-feste-veranstaltungen.html"><strong aria-hidden="true">2.3.</strong> Regelmäßige Feste &amp; Veranstaltungen</a></li></ol></li><li class="chapter-item expanded "><a href="alltag-leben-in-ahrensburg.html"><strong aria-hidden="true">3.</strong> Alltag &amp; Leben in Ahrensburg</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="die-stadtteile-im-portraet.html"><strong aria-hidden="true">3.1.</strong> Die Stadtteile im Porträt</a></li><li class="chapter-item expanded "><a href="vereinsleben.html"><strong aria-hidden="true">3.2.</strong> Vereinsleben</a></li><li class="chapter-item expanded "><a href="wochenmarkt.html"><strong aria-hidden="true">3.3.</strong> Wochenmarkt</a></li><li class="chapter-item expanded "><a href="gastronomie-fuehrer.html"><strong aria-hidden="true">3.4.</strong> Gastronomie-Führer</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="restaurant.html"><strong aria-hidden="true">3.4.1.</strong> Restaurant</a></li></ol></li><li class="chapter-item expanded "><a href="uebernachtungsmoeglichkeiten-in-ahrensburg-2.html"><strong aria-hidden="true">3.5.</strong> Übernachtungsmöglichkeiten in Ahrensburg</a></li><li class="chapter-item expanded "><a href="einkaufen-in-ahrensburg-2.html"><strong aria-hidden="true">3.6.</strong> Einkaufen in Ahrensburg</a></li><li class="chapter-item expanded "><a href="kirchen-und-religioese-gemeinschaften.html"><strong aria-hidden="true">3.7.</strong> Kirchen und religiöse Gemeinschaften</a></li><li class="chapter-item expanded "><a href="seniorentreff.html"><strong aria-hidden="true">3.8.</strong> Seniorentreff</a></li><li class="chapter-item expanded "><a href="gesundheit.html"><strong aria-hidden="true">3.9.</strong> Gesundheit</a></li><li class="chapter-item expanded "><a href="familie-bildung.html"><strong aria-hidden="true">3.10.</strong> Familie &amp; Bildung</a></li></ol></li><li class="chapter-item expanded "><a href="natur-freizeit.html"><strong aria-hidden="true">4.</strong> Natur &amp; Freizeit</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="naherholungsgebiete.html"><strong aria-hidden="true">4.1.</strong> Naherholungsgebiete</a></li><li class="chapter-item expanded "><a href="wander-und-radwege.html"><strong aria-hidden="true">4.2.</strong> Wander- und Radwege</a></li><li class="chapter-item expanded "><a href="spielplaetze.html"><strong aria-hidden="true">4.3.</strong> Spielplätze</a></li></ol></li><li class="chapter-item expanded "><a href="infrastruktur-wirtschaft.html"><strong aria-hidden="true">5.</strong> Infrastruktur &amp; Wirtschaft</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="verkehrsanbindung.html"><strong aria-hidden="true">5.1.</strong> Verkehrsanbindung</a></li><li class="chapter-item expanded "><a href="wichtige-unternehmen-arbeitgeber.html"><strong aria-hidden="true">5.2.</strong> Wichtige Unternehmen &amp; Arbeitgeber</a></li><li class="chapter-item expanded "><a href="gewerbegebiete.html"><strong aria-hidden="true">5.3.</strong> Gewerbegebiete</a></li><li class="chapter-item expanded "><a href="stadtverwaltung.html"><strong aria-hidden="true">5.4.</strong> Stadtverwaltung</a></li><li class="chapter-item expanded "><a href="buergermeister-und-stadtvertretung.html"><strong aria-hidden="true">5.5.</strong> Bürgermeister und Stadtverordnetenversammlung</a></li></ol></li><li class="chapter-item expanded "><a href="ahrensburg-nachrichten-website.html"><strong aria-hidden="true">6.</strong> Ahrensburg Nachrichten Website</a></li><li class="chapter-item expanded affix "><li class="part-title">Sonstiges</li><li class="chapter-item expanded "><a href="einkaufen-in-ahrensburg.html"><strong aria-hidden="true">7.</strong> Einkaufen in Ahrensburg</a></li><li class="chapter-item expanded "><a href="uebernachtungsmoeglichkeiten-in-ahrensburg.html"><strong aria-hidden="true">8.</strong> Übernachtungsmöglichkeiten in Ahrensburg</a></li><li class="chapter-item expanded "><a href="datenschutz.html"><strong aria-hidden="true">9.</strong> Datenschutz</a></li><li class="chapter-item expanded "><a href="impressum.html"><strong aria-hidden="true">10.</strong> Impressum</a></li><li class="chapter-item expanded affix "><li class="part-title">Wie dieses Wiki entsteht</li><li class="chapter-item expanded "><a href="co-wiki.html"><strong aria-hidden="true">11.</strong> Co-Wiki: Mensch &amp; KI</a></li><li class="chapter-item expanded "><a href="software-fuer-ein-grosses-wissensprojekt.html"><strong aria-hidden="true">12.</strong> Software für ein großes Wissensprojekt</a></li><li class="chapter-item expanded affix "><li class="part-title">OpenWiki – Repository-Dokumentation</li><li class="chapter-item expanded "><a href="openwiki/overview.html"><strong aria-hidden="true">13.</strong> Überblick</a></li><li class="chapter-item expanded "><a href="openwiki/architecture.html"><strong aria-hidden="true">14.</strong> Architektur</a></li><li class="chapter-item expanded "><a href="openwiki/source-map.html"><strong aria-hidden="true">15.</strong> Source-Map</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0].split("?")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
