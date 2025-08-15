# pip install classla

import classla

# Download Serbian models (only first time)
# This downloads all processors, including NER
#classla.download("sr")

#input("Press Enter to start...")

# Load Serbian pipeline
nlp = classla.Pipeline("sr")

text = ("Sebastian Thrun je zvezda ove priče. Kada je Sebastian Thrun počeo da radi na automobilima bez vozača "
        "u Google-u 2007. godine, malo ljudi van kompanije ga je shvatalo "
        "ozbiljno. „Mogu da vam kažem da su vrlo visoki direktori velikih "
        "američkih automobilskih kompanija stiskali moju ruku i okretali se "
        "jer nisam bio vredan razgovora,“ rekao je Thrun u intervjuu ove "
        "nedelje. Sebastian Thrun je dobra osoba. Sebastian Thrunova genetska "
        "predispozicija je povećala šansu da bude kolekcionar knjiga."
        "Pera je drugi lik u ovoj priči.")

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

import re
from collections import defaultdict

# --- helpers ---
def deinflect_lastname(token: str) -> str:
    t = token

    # Strip common Serbian possessive forms first (e.g., "Thrunova" -> "Thrun")
    for suf in ("ova", "eva", "ina"):
        if t.lower().endswith(suf) and len(t) > len(suf) + 2:
            t = t[:-len(suf)]
            break

    # Strip possessive stems if present (e.g., "Thrunov" -> "Thrun")
    for suf in ("ov", "ev", "in"):
        if t.lower().endswith(suf) and len(t) > len(suf) + 2:
            t = t[:-len(suf)]
            break

    # Strip common case endings (gentle)
    for suf in ("om", "og", "u", "a", "e", "i"):
        if t.lower().endswith(suf) and len(t) > len(suf) + 2:
            t = t[:-len(suf)]
            break

    return t

def normalize_fullname(ent_text: str) -> str:
    # Normalize only the last token; keep original casing on the rest
    parts = ent_text.split()
    if not parts:
        return ent_text.strip()

    if len(parts) == 1:
        # single token (likely last name or given name)
        return deinflect_lastname(parts[0])

    last_base = deinflect_lastname(parts[-1])
    parts[-1] = last_base
    return " ".join(parts)

# --- build mapping from classla doc ---
people = []
for ent in doc.ents:
    if ent.type != "PER":
        continue
    text = ent.text.strip()
    norm_full = normalize_fullname(text)
    parts = norm_full.split()
    base_last = parts[-1] if parts else norm_full
    people.append({
        "orig": text,
        "norm_full": norm_full,         # e.g., "Sebastian Thrun" or "Thrun"
        "base_last_lc": base_last.lower(),
        "is_full": len(parts) >= 2,
        "start": ent.start_char,
    })

# 1) choose canonical full name per last name: earliest occurrence in text
canonical_full_by_last = {}  # last -> (start, canonical_full)
for p in people:
    if p["is_full"]:
        last = p["base_last_lc"]
        cand = p["norm_full"]
        if last not in canonical_full_by_last or p["start"] < canonical_full_by_last[last][0]:
            canonical_full_by_last[last] = (p["start"], cand)

# 2) build final variant -> canonical map
variant_to_canonical = {}
for p in people:
    last = p["base_last_lc"]
    # Prefer the earliest full-name for this last name, if it exists
    if last in canonical_full_by_last:
        canonical = canonical_full_by_last[last][1]
    else:
        # No known full name for this last: keep normalized form as canonical
        canonical = p["norm_full"]

    variant_to_canonical[p["orig"]] = canonical

# 3) also group into clusters by canonical
clusters = defaultdict(set)
for variant, canon in variant_to_canonical.items():
    clusters[canon].add(variant)

# --- demo prints ---
print("Variant → Canonical:")
for k, v in variant_to_canonical.items():
    print(f"{k!r} -> {v!r}")

print("\nClusters:")
for canon, vars_ in clusters.items():
    print(f"{canon!r}: {sorted(vars_)}")
