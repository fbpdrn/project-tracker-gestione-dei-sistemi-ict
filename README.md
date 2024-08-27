# Project Tracker

## Descrizione

**Project Tracker** è un modulo per Odoo 17 sviluppato per il corso di Gestione dei Sistemi ICT (37034) 2023/2024 dell'Università degli Studi di Bergamo.

## Dipendenze Odoo

I seguenti moduli di Odoo sono necessari per il funzionamento:

- `odoo.base`
- `odoo.mail`

## Utilizzo

Per utilizzare il modulo Project Tracker, segui questi passaggi:

1. Scarica i codici sorgente di Odoo dalla [pagina di download di Odoo](https://www.odoo.com/page/download);
2. Avvia la suite di Odoo utilizzando il comando seguente, sostituendo `<PATH_CARTELLA_PROJECT_TRACKER>` con il percorso della cartella contenente il modulo e `<DATABASE>` con il nome del database che desideri utilizzare:

   ```zsh
   python3 odoo-bin --addons-path="addons,<PATH_CARTELLA_PROJECT_TRACKER>" -d <DATABASE> -u 'project-tracker' --dev xml
3. Installare il modulo cercandolo dal menù Apps.

## Struttura delle Cartelle

La struttura delle cartelle del modulo è organizzata come segue:

- **views**: contiene i file XML che definiscono le viste necessarie al modulo.
- **models**: include i modelli e la logica associata.
- **security**: contiene le definizioni delle regole di controllo e di accesso ai modelli del modulo.
- **static**: contiene i file di stile per alcuni componenti utilizzati nelle viste.
- **docs**: include la presentazione consegnata per il corso.

