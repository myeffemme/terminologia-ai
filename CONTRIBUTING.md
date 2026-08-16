# Contribuire

Grazie per voler migliorare il Catalogo terminologico AI.

## Flusso di lavoro

1. Apri una issue per proporre un nuovo lemma o segnalare un problema.
2. Crea un branch e modifica unicamente i file necessari.
3. Per una voce nuova, aggiungi un solo file `entries/<id>.yaml` conforme allo schema.
4. Esegui `python scripts/validate.py`.
5. Apri una pull request usando il template.

Le modifiche a `main` passano tramite pull request e controlli automatici. Solo l'editore umano può approvare il passaggio di una voce a `published`.

## Regole essenziali

- `entries/` è il corpus canonico: non copiare le voci in cartelle per sito o EPUB.
- Mantieni stabile l'`id` di un lemma pubblicato.
- Scrivi definizioni autosufficienti; le fonti attestano e approfondiscono, non sostituiscono il testo.
- Non forzare traduzioni italiane non attestate.
- Cita materiale altrui senza riprodurlo integralmente.
- Segui le politiche in `docs/`.

## Dipendenze

```bash
python -m pip install -r requirements.txt
```
