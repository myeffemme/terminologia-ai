# Catalogo terminologico AI

Catalogo tecnico bilingue IT/EN della terminologia dell'intelligenza artificiale. La prima fase sviluppa le voci in italiano; i campi inglesi potranno essere estesi senza creare un corpus parallelo.

## Principio architetturale

I file YAML in [`entries/`](entries/) sono l'unica fonte canonica dei contenuti. Il sito, l'EPUB e ogni altro formato editoriale devono essere generati automaticamente da questi file: non si mantengono copie delle voci in cartelle separate.

## Struttura

- `entries/`: un file YAML per lemma, corpus canonico;
- `schema/lemma.schema.json`: schema formale delle voci;
- `taxonomy/`: categorie e tag controllati;
- `docs/`: politiche editoriali, terminologiche e delle fonti;
- `scripts/validate.py`: validazione strutturale e trasversale;
- `scripts/build.py`: generazione degli artefatti derivati in `build/`;
- `.github/`: automazione della validazione e modelli di collaborazione.

## Uso locale

Richiede Python 3.11 o successivo.

```bash
python -m pip install PyYAML jsonschema
python scripts/validate.py
python scripts/build.py
```

La build genera rappresentazioni intermedie per sito ed EPUB sotto `build/`, che è esclusa da Git. I generatori finali consumeranno questi dati senza modificare `entries/`.

## Stato del progetto

Il catalogo parte con due lemmi in bozza: `logit` e `prefill`. I collegamenti a lemmi non ancora presenti sono ammessi come avvisi nelle bozze; diventano errori prima della pubblicazione.

## Licenza

Contenuti e metadati sono distribuiti secondo [CC BY 4.0](LICENSE), salvo diversa indicazione per materiali citati o collegati. Le fonti restano soggette alle licenze dei rispettivi titolari.
