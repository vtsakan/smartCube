# smartCube

Α. Σκοπόςhh

Σκοπός του έργου "SmartCube" είναι η κατασκευή ενός έξυπνου κύβου, ο οποίος θα μπορεί να "εκφωνήσει" διάφορες πληροφορίες σχετικές με το περιβάλλον, όπως την θερμοκρασία και η βαρομετρική πίεση. Ο έξυπνος κύβος θα λειτουργεί συνεχώς και θα συλλέγει τα απαραίτητα δεδομένα, ενώ θα ανακοινώνει τις πληροφορίες ανα τακτά χρονικά διαστήματα.

Β. Υλικό

Για την εκτέλεση του παραπάνω έργου, απαιτείται το εξής hardware:

Ένα Raspberry Pi 3, για να φιλοξενήσει την υπηρεσία κείμενο - σε - ήχο, στο πλαίσιο που περιγράφηκε παραπάνω..
Ένας ασύρματος αισθητήρας SensorTag CC2650 για την συλλογή των απαραίτητων δεδομένων περιβάλλοντος.
Ένα ηχείο.

SensorTag CC2650

Το κόστος του εξοπλισμού αναλύεται ως εξής:

~33.5 ευρώ για την αγορά του raspberry pi 3
(https://www.ebay.com/itm/Original-Raspberry-Pi-3-Model-B-Quad-Core-1-2GHz-64-bit-CPU-wifi-bluetooth/192099353359?epid=24019970648&hash=item2cba03830f:g:C~wAAOSw0ABankhY:rk:6:pf:0)

~28 ευρώ για την συσκευή αισθητήρων SensorTag.
(https://uk.farnell.com/texas-instruments/cc2650stk/evaluation-mod-simplelink-sensor/dp/2470181#)

~1 ευρώ για ένα μικρόφωνο
(https://www.ebay.com/itm/Mini-USB-Microphone-Professional-Mini-USB-External-Mic-Microphone-With-Clip/253700094909?hash=item3b11b43bbd:g:9XQAAOSwllpbKgAR:rk:2:pf:0)

Το συνολικό κόστος των υλικών ανέρχεται στα 62.5 ευρώ.

Γ. Λογισμικό

Το λογισμικό που θα αναπτυχθεί στα πλαίσια του έργου θα είναι γραμμένο σε Python. Οι βιβλιοθήκες που θα απαιτηθούν για την ολοκλήρωση των διαφόρων υποσυστημάτων θα είναι:

Βιβλιοθήκη οδήγησης του ασύρματου αισθητήρα
https://github.com/OrestisEv/SensorTag-Pi3

Βιβλιοθήκη για την μετατροπή κείμενου σε ομιλία (text to speech)
https://pythonprogramminglanguage.com/text-to-speech/

Δ. Github

Ο σύνδεσμος του github για το έργο βρίσκεται εδώ: https://github.com/vtsakan/smartCube

Ε. Εκπαιδευτικό σενάριο

Κατά την φάση υλοποίησης του έργου, οι μαθητές αναμένεται να ασχοληθούν με τα παρακάτω αντικείμενα:

Προγραμματισμός Python

Ακολουθιακός προγραμματισμός
Εισαγωγή στον τμηματικό προγραμματισμό

Φυσική
Θερμοκρασία, βαρομετρικό, επιτάγχυνση

Η υλοποίηση του έργου αναμένενται να στηριχθεί απο αρκετές εκπαιδευτικές ώρες, σε διάστημα 4 μηνών. Η πρώτη έκδοση του OER φαίνεται εδώ: OER_SMARTCUBE_v01. 
Φυσικά, μετά την ολοκλήρωση της κατασκευής, θα συμπληρωθεί με τις λεπτομέρειες του έργου, καθώς και με χρήσιμη πληροφορία σχετικά με την εκπαιδευτική διαδικασία απο την οποία προήλθε.

ΣΤ. Προγραμματισμός υλοποίησης

Το project θα έχει τις εξής φάσεις:

Σχεδιασμός - Εκπαίδευση

Καταγραφή των λειτουργιών που θα εκτελεί ο έξυπνος κύβος. Οι μαθητές θα πρέπει να υλοποιήσουν σίγουρα τις λειτουργίες (α) θερμοκρασία, (β) μέρα ή νύχτα, καθώς και ανίχνευση κίνησης μέσω accelerometer τοy CC2650. Απο εκεί και πέρα θα γίνει συζήτηση για το τι άλλες λειτουργίες θα υλοποιηθούν.

Οι μαθητές θα χωριστούν σε 4 ομάδες. Η πρώτη ομάδα θα αναλάβει την λειτουργία (α), η δεύτερη την λειτουργία (β), ενώς οι δύο άλλες θα μελετήσουν τα σήματα του επιταχυνσιόμετρου και γυροσκοπίου.

Η πρώτη ομάδα θα συναρμολογήσει το εσωτερικό του έξυπνου κύβου. Σε αυτό το στάδιο, θέματα όπως η σύνδεση του ηχείου με το Raspberry PI καθώς και σύνδεση του Raspberry Pi με τον CC2650.

H δεύτερη ομάδα θα εξοικειωθεί με τον driver του CC2650(βασικές εντολές) και θα αναλάβει να δημιουργήσει μία παρουσίαση για να εκπαιδεύσει τις άλλες 2 ομάδες.

Η τρίτη ομάδα θα σχεδιάσει τον τρόπο με τον οποίο θα συνδεθεί το ηχείο και θα εξεερευνήσει την βιβλιοθήκες text2speech. Επίσης θα αναλάβει να δημιουργήσει μία παρουσίαση για να εκπαιδεύσει τις άλλες 2 ομάδες.

Η τέταρτη ομάδα θα κατεσκευάσει απο χαρτόνι τον κύβο μέσα στον οποίο θα στερωθεί το raspberry και το ηχείο.

Υλοποίηση - Προγραμματισμός
Η υλοποίηση του έργου θα ακολουθήσει την λογική της σπειροειδούς ανάπτυξης. Σε αυτή την φάση οι μαθητές συνεχίζουν να δουλεύουν σε 4 ομάδες, και ασχολούνται με τις εργασίες που αναφέρθηκαν στο (1.2)

Φάση 1: Οι μαθητές συνδέουν τον πολυαισθητήρα με το raspberry, συλλέγουν δεδομένα και τα επεξεργάζονται.

Φάση 2: Οι μαθητές χρησιμοποιούν την βιβλιοθήκη text2speech και δημιουργούν τα κατάλληλα μηνύματα.

Φάση 3: Οι μαθητές εκτελούν τα πρώτα ολοκληρωμένα σενάρια και επιστρέφουν στον κώδικα για διορθώσεις.

Φάση 4: Οι μαθητές βάζουν σχόλια σε όλο τον κώδικα.

Σε όλη την διάρκεια του έργου ένας μαθητής απο κάθε ομάδα θα έχει πρόσβαση στο "Ημερολόγιο Κατασκευής", ένα ημερολόγιο που θα καταγράφεται η δουλειά κάθε συνάντησης καθώς και τα προβλήματα που αντιμετωπίστηκαν, και πως αυτά ξεπεράστηκαν.
