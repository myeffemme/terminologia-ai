# Programma del progetto

Data di consolidamento: 16 agosto 2026

## 1. Obiettivo

Il Catalogo terminologico AI è un progetto editoriale tecnico bilingue IT/EN. La prima fase sviluppa la versione italiana. Ogni lemma deve offrire una spiegazione comprensibile, un eventuale approfondimento tecnico, esempi concreti e fonti autorevoli.

Il catalogo privilegia precisione, accessibilità e neutralità. Non è una semplice raccolta alfabetica: le voci formano percorsi di apprendimento e diramazioni tematiche.

## 2. Corpus canonico

I file YAML in `entries/` costituiscono l'unica fonte canonica delle voci. Sito, EPUB e altri prodotti vengono generati automaticamente dal corpus e non mantengono copie editoriali indipendenti.

La relazione tecnica è quindi:

```text
entries/ (corpus canonico)
        ├── sito continuamente aggiornato
        └── edizione EPUB congelata e revisionata
```

Git conserva storia, differenze e possibilità di ripristino. Le edizioni del libro devono corrispondere a tag Git stabili, per esempio `edition-2027.1`.

## 3. Rapporto tra sito e libro

### Sito

Il sito è il punto di consultazione corrente. Offre ricerca per termine, alias e categoria, collegamenti tra lemmi, stato editoriale, data di revisione e strumenti per segnalare problemi.

Per tutte le voci pubblica almeno:

- termine italiano e inglese;
- alias;
- categoria e tag;
- definizione sintetica;
- termini correlati;
- fonti principali;
- data dell'ultima revisione;
- indicazione dell'edizione che contiene la trattazione completa.

Una voce selezionata viene presentata integralmente come **voce in evidenza**. La selezione è editoriale e ruota periodicamente; non coincide necessariamente con l'ultima modifica effettuata.

La configurazione della voce in evidenza appartiene al prodotto sito, non al lemma. Deve quindi essere conservata separatamente dal contenuto terminologico, con una struttura equivalente a:

```yaml
featured_entry:
  id: logit
  starts_on: 2027-01-08
  ends_on: 2027-01-21
```

### Libro

Il libro è un'edizione revisionata e datata del corpus, non una sequenza automatica di pagine web. Il suo valore risiede in:

- ordine pedagogico;
- percorsi tematici;
- introduzioni e raccordi tra le voci;
- mappe concettuali e box di disambiguazione;
- indici IT/EN ed EN/IT;
- bibliografia consolidata;
- lettura offline, qualità tipografica e citabilità;
- changelog rispetto all'edizione precedente.

Il libro include tutte le voci `published` comprese nel tag dell'edizione. Dal libro, link o codici QR rimandano alla versione corrente delle voci e alla pagina di errata corrige. Dal sito, ogni voce indica le edizioni nelle quali è inclusa.

Poiché il repository è pubblico, il libro non viene presentato come accesso esclusivo a contenuti segreti. Il suo valore commerciale è la completezza organizzata, revisionata e resa comoda da consultare.

## 4. Due livelli di lettura

Ogni lemma distingue due livelli senza duplicare il corpus.

### Livello 1 — Capire il concetto

È destinato a un lettore interessato all'AI senza preparazione matematica o informatica specialistica. Comprende:

- definizione sintetica;
- spiegazione in linguaggio comune;
- esempio concreto;
- motivo per cui il concetto è importante.

Regole di scrittura:

- una sola idea nuova per paragrafo;
- nessun termine tecnico usato per definirne un altro senza spiegazione;
- sigle sempre sciolte alla prima occorrenza;
- esempi prima delle classificazioni astratte;
- formule e dettagli sull'hardware esclusi salvo necessità;
- semplicità senza perdita di correttezza.

### Livello 2 — Approfondimento tecnico

È facoltativo ed è destinato al lettore che vuole comprendere più precisamente il funzionamento. Può introdurre terminologia specialistica, relazioni tra componenti, dettagli implementativi, casi particolari e formule realmente utili. Prosegue la spiegazione di primo livello senza ripeterla.

La struttura editoriale di riferimento è:

```yaml
short_def_it: definizione in una o due frasi
explanation_it: spiegazione accessibile
example_it: esempio concreto
why_it_matters: utilità e contesto
technical_it: approfondimento facoltativo
disambiguation_it: distinzione da concetti vicini, quando necessaria
```

Lo schema formale verrà adeguato a questa struttura prima di ampliare significativamente il corpus. Anche `logit` e `prefill` verranno riscritti come lemmi modello a due livelli.

## 5. Neutralità su pensiero e ragionamento

Il catalogo distingue tre piani:

1. **meccanismo di addestramento e generazione:** molti LLM autoregressivi vengono addestrati con un obiettivo di predizione del token successivo e producono output token per token;
2. **capacità osservabili:** i modelli possono risolvere problemi in più passaggi, confrontare alternative, utilizzare rappresentazioni intermedie e mostrare comportamenti di pianificazione;
3. **interpretazione:** stabilire se queste capacità costituiscano pensiero, comprensione o ragionamento nello stesso senso umano è una questione scientifica e filosofica aperta.

La predizione del token successivo descrive un obiettivo di addestramento e un'interfaccia di generazione; non esaurisce necessariamente i processi interni sviluppati dal modello. Allo stesso tempo, una spiegazione passo per passo prodotta dal modello non prova che il testo rappresenti fedelmente il processo interno che ha determinato la risposta.

Formulazione editoriale di riferimento:

> Il catalogo descrive il ragionamento degli LLM in termini operativi, senza ridurlo alla sola predizione del token successivo e senza attribuire automaticamente ai modelli pensiero, comprensione o coscienza in senso umano.

Sono preferite espressioni come:

- «mostra capacità di ragionamento»;
- «risolve compiti che richiedono più passaggi»;
- «utilizza passaggi intermedi»;
- «sviluppa strategie interne»;
- «mostra un comportamento compatibile con una forma di pianificazione».

Sono evitate come affermazioni assolute:

- «è soltanto un predittore del token successivo»;
- «non fa altro che imitare»;
- «pensa come una persona»;
- «possiede una comprensione propria»;
- «la chain of thought mostra ciò che il modello pensa realmente».

## 6. Sviluppo per percorsi

Le voci vengono costruite seguendo percorsi specifici. Ogni percorso possiede una spina dorsale accessibile dalla quale possono crescere diramazioni tecniche. Ogni lemma rimane comprensibile autonomamente.

Il primo percorso è **La creazione di un LLM: dai dati al modello utilizzabile**.

### Prima sequenza di lavorazione

1. LLM;
2. token;
3. tokenizzazione;
4. corpus;
5. addestramento;
6. parametro;
7. transformer;
8. attention;
9. pretraining;
10. predizione del token successivo;
11. logit;
12. funzione di perdita;
13. backpropagation;
14. checkpoint;
15. post-training.

La prima voce è `LLM`, perché definisce l'oggetto dell'intero percorso. È una voce panoramica: presenta ciò che viene costruito senza anticipare tutti i meccanismi.

Identità terminologica iniziale:

```yaml
id: llm
term_it: modello linguistico di grandi dimensioni
term_en: large language model
aliases:
  - LLM
```

La seconda voce è `token`, primo elemento concreto necessario per spiegare come il testo viene elaborato dal modello. Da essa si aprono le diramazioni su tokenizzazione, tokenizer, vocabolario, embedding, costi e finestra di contesto.

`prefill`, `decode` e `kv-cache` appartengono più naturalmente a un successivo percorso autonomo: **Come un LLM genera una risposta**.

## 7. Flusso editoriale e responsabilità

Ogni modifica passa tramite pull request e controllo automatico. Il flusso è:

```text
proposta o bozza
→ validazione dello schema e del corpus
→ verifica delle fonti e della coerenza trasversale
→ decisione dell'editore
→ pubblicazione
```

Il proprietario `myeffemme` è l'unico editore e può integrare personalmente una pull request dopo il superamento del controllo GitHub Actions `validate`. Non è richiesta l'approvazione di un secondo account. Force-push e cancellazione di `main` restano vietati.

Solo l'editore umano porta una voce allo stato `published`.

## 8. Prossimo passo

Prima di scrivere la voce `LLM`:

1. adeguare lo schema ai due livelli di lettura;
2. aggiornare le policy editoriali con la regola di neutralità;
3. riscrivere `logit` e `prefill` come esempi di riferimento;
4. redigere `LLM` come prima voce panoramica del percorso.
