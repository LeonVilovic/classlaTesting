# pip install classla

import classla

# Download Serbian models (only first time)
# This downloads all processors, including NER
#classla.download("sr")

# Load Serbian pipeline
nlp = classla.Pipeline("sr")

text = ("      Sebastian Thrun je zvezda ove priče. Kada  je Sebastian Thrun počeo da radi na automobilima bez vozača "
        "u Google-u 2007. godine, malo ljudi van kompanije ga je shvatalo "
        "ozbiljno. „Mogu da vam kažem da su vrlo visoki direktori velikih "
        "američkih automobilskih kompanija stiskali moju ruku i okretali se "
        "jer nisam bio vredan razgovora,“ rekao je Thrun u intervjuu ove "
        "nedelje. Sebastian Thrun je dobra osoba. Sebastian Thrunova genetska "
        "predispozicija je povećala šansu da bude kolekcionar knjiga.")

# Process text
doc = nlp(text)

# Extract noun phrases (approximation using NOUN/PROPN tags)
noun_phrases = [
    " ".join(w.text for w in sent.words if w.upos in ["NOUN", "PROPN"])
    for sent in doc.sentences
]
print("Noun phrases:", noun_phrases)

# Extract verbs
verbs = [w.lemma for sent in doc.sentences for w in sent.words if w.upos == "VERB"]
print("Verbs:", verbs)

# Named entities
for ent in doc.ents:
    print(ent.text, ent.type, ent.start_char, ent.end_char)
