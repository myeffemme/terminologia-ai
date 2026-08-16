# Politica editoriale

## Principi

Il catalogo privilegia precisione, comprensibilità e coerenza. Ogni voce deve essere tecnicamente corretta senza presupporre conoscenze specialistiche non necessarie. La definizione breve è autonoma; quella lunga introduce gradualmente il dettaglio tecnico. I termini indispensabili vengono spiegati o collegati ad altri lemmi.

## Struttura delle voci

I campi definiti nello schema sono obbligatori o opzionali secondo la loro utilità editoriale. Esempi, note, uso e disambiguazione vanno inclusi solo quando aggiungono valore. La storia delle modifiche è affidata a Git e non viene duplicata nei YAML.

## Stati editoriali

- `draft`: bozza in lavorazione;
- `verified`: controllata nelle fonti e rispetto al corpus;
- `reviewed`: approvata editorialmente da una persona;
- `published`: inclusa nei prodotti pubblici.

Solo l'editore umano può portare una voce a `published`. Una voce `reviewed` o `published` deve avere `provenance.human_reviewed: true` e una data `last_reviewed`.

## Controllo trasversale

La verifica riguarda sia la singola voce sia l'intero corpus: alias duplicati, riferimenti inesistenti, definizioni circolari o contraddittorie, categorie incoerenti e uso non uniforme dei termini.

## Prodotti derivati

`entries/` è l'unica fonte dei lemmi. Sito ed EPUB sono generati automaticamente. L'EPUB è una edizione revisionata e datata del corpus, non una copia mantenuta a mano.
