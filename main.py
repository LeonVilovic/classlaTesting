# pip install classla

import classla

# Download Serbian models (only first time)
# This downloads all processors, including NER
#classla.download("sr")

#input("Press Enter to start...")

# Load Serbian pipeline
nlp = classla.Pipeline("sr")

text2 = ("ЗАПИСНИК"
"о извршеном инспекцијском надзору"
"Дана 31.01.2025. године, у 11.30. часова, овлашћена лица Повереника, Биљана Ненадић, бр."
"службене легитимације 011 и Оља Живковић, бр. службене легитимације 023, извршила су"
"вапредан теренски инспекцијски надзор над применом ЗЗПЛ од стране Предшколске установе"
"Чукарица, Пожешка 28, Београд (у даљем тексту: надзирани субјекат или Руковалац)."
"Надзор је извршен по налогу шефа Одсека за надзор бр. 072-21-26/2025-07 од 22.01.2025. године."
"1. Основи подаци о Надзираном субјекту:"
"Пословно име надзираног субјекта: Предшколска установе Чукарица Адреса званичне веба презентације: ћир :/рисиканса.тв/ Матични број: 07009496 ПИБ: 100974365"
"Адреса: Пожешка 28, Београд"
"Законски заступник Руковаоца је Биљана Гајић, директор установе, бр. личне карте"
"Као представници надзираног субјекта, вршењу надзора присуствовали су:"
"- Биљана Гајић, директор установе"
"- Оливера Јовановић, број личне карте текретар установе, лице за заштиту података"
"о личности."
"ке"
""
"2. Предмет надзора"
"Предмет ванредног теренског инспекцијског надзора је обрада података о личности деце путем"
"аудио видео снимака и пристанак за обраду података о личности деце у предшколској установи."
"3. Ток и садржај предузетих радњи ради утврђивања чињеница и других радњи у"
"поступку"
"Овлашћена лица Повереника су утврдила да је надзирани субјекат доставио Поверснику контакт"
"податке лица за заштиту података о личности, Оливере Јовановић."
"Овлашћена лица Повереника су утврдила да се у представци, на основу које је покренут поступак"
"ванредног инспекцијског надзора, наводи да је Драгана Микић, запослена као васпитачица ПУ"
"Чукарица, фотографисала и снимала дете Лазара Павковића својим приватним телефоном, без"
"одговарајућег правног основа, као и да је дете, у ситуацијама када није желело да спава,"
"уцењивала да ће га снимити и фотографисати."
"4. Изјаве присутних представника надзираног субјекта"
"На питање овлашћеног лица Повереника да ли је васпитачица Драгана Микић фотографисала и"
"снимала дете Лазара Павковића, и ако јесте која је сврха и правни основ обраде, представници"
"надзираног субјекта су се изјаснили на следећи начин:"
"Сви васпитачи имају обавезу да документују свој рад и спровођење прописаног програма и"
"пројеката и да је фотографисање и снимање деце један од начина на који се документовање врши."
"Према изјави представница надзираног субјекта, сврха обраде и правни основ прописани"
"Правилником о основама програма предшколског васпитања и образовања („Службени гласник"
"РС – Просветни гласник“, број 16/2018). Према изјави представника, у акту који представља"
"саставни део Правилника - Основе програма предшколског васпитања и образовања, у поглављу:"
"Праћење, вредновање и документовање, поднаслов: Облици и начин праћења, наведено је:"
"„Процес учења и развоја детета се прати и докумен тује кроз дечји портфолио. Кроз портфолио се"
"документује напредовања детета којим се истиче шта су јаке стране детета, дечја перспектива"
"си' туациј а, активности и дог ађаја, начин пружања подршке детету, нарочито када су у питању деца"
"из осетљивих група."
"за документовање кроз индивидуални портфолио могу се користити: различите скале и друге"
"технике посматрања и праћења, групне и индивидуалне приче за учење; продукти и искази детета"
"настали у консултовању са децом, продукти детета настали у игри и у оквиру теме/пројекта:"
"фотографисање, видео и аудио записи, настали у различитим ситуацијама који су детету посебно"
"важни.“"
"На питање овлашћених лица Повереника који је правни основ за употребу личних телефона."
"васпитача приликом фотографисања и снимања деце, представнице надзираног субјекта су"
"изјавиле да су предшколске установе, приликом извршавања обавеза из оквира својих"
"надлежности, у обавези да примењују Приручник за документовање - Педагошка документација"
"и документовање у Основама програма ПВО „Године узлета“ , аутора проф. др Живка Крњаја"
"2"
""
"проф. др Драгана Павловић Бренеселовић, издавач Министарство просвете, науке и технолошког"
"развоја."
"У приручнику се наводи: „Приручник за документовање настао је на Институту за педагогију и"
"андрагогију Филозофског факултета Универзитета у Београду у оквиру пројекта „Инклузивно"
"предшколско васпитање и образовање“, који реализује Министарство просвете, науке и"
"технолошког развоја Србије у сарадњи са Институтом за педагогију и андрагогију и СМТСЕЕ и уз"
"подршку Светске банке. Приручник за документовање припада серијалу приручника и водича под"
"заједничким називом „Линије лета"" који су припремљени на Институту за педагогију и"
"андрагогију са циљем подршке примени Основа програма предшколског васпитања и образовања"
"„Године узлета,“"
"Представнице надзираног субјекта су истакле, да је правни основ за употребу личних телефона"
"васпитача садржан у наведеном Приручнику за документовање, у којем се на страни 53, наслов"
"Документовање није само фотографисање, наводи следеће:"
"Опо што васпитачи пајпре препознају у овом приступу документовању јесте да је сад потребно"
"фотографисати. Тачно је, фотоографији се придаје велики значај и да бисте документовали у"
"свакодневним ситуацијама потребна вам је опрема ( идеално би било фото апарат, камера,"
"телефон, лапштон, штампач,...). То подразумева да вам је опрема при руци и на располагању у"
"свакој ситуацији коју хоћете да документујете. На жалост, немају сви вртићи ову опрему, нити су"
"васпитачи ти који треба да је обезбеде. Док се не реши питање опреме, увек ћсте користити"
"свој телефон, али то не може бити коначно решење. Поседовање барем минималне опреме"
"мора постати стандард и тај приоритет треба истипати у свакој прилици. Али то не може бити"
"оправдање да документовањс не постанс дсо ваше свакодневне праксе. Не заборавите,"
"документовање обухвата и планирање и развијање и праћење процеса кроз паное и панеле и"
"коришћење низа других техника осим фотографисања."
"На питање овлашћених лица Повереника да ли је васпитачица Драгана Микић, фотографисала и"
"снимала децу само у сврхе које су прописане Правилником о основама програма предшколског"
"васпитања и образовања или их је фотографисала, како се навод у прелставци, како би их"
"уцењивала када не желе да спавају, представнице надзираног субјекта су изјавиле да је у поступку"
"дисциплински поступак у ком се утврђује одговорпост васпитачице Драгапа Микић у вези са"
"наводима из представке, и да поступак није окончан."
"Представници надзираном субјекта су приложиле изјаву родитеља детета Лазара Павковића,"
"којим дају пристанак за обраду података о личности детета, у радној 2021/2022. години. У изјави"
"се између осталог наводи:"
"„Својим потписом одобравам следеће активпости у радпој 2021/2022 години;"
"Фотографисање деце, снимање видео и аудио записа јавних наступа и различитих активности деце и објављивање на сајту ПУ Чукарица и друштвеним мрежама ПУ Чукарица. 2. Слање дечијих радова на изложбе у организацији ПУ Чукарица и објављивање на сајту ПУ 3. Формирање он лајн заједница Вртић у породици“."
"Чукарица, Јутјуб каналу и друштвеним мрежама ПУ Чукарица")

text3 = ("Sebastian Thrun je zvezda ove priče. Kada je Sebastian Thrun počeo da radi na automobilima bez vozača "
        "u Google-u 2007. godine, malo ljudi van kompanije ga je shvatalo "
        "ozbiljno. „Mogu da vam kažem da su vrlo visoki direktori velikih "
        "američkih automobilskih kompanija stiskali moju ruku i okretali se "
        "jer nisam bio vredan razgovora,“ rekao je Thrun u intervjuu ove "
        "nedelje. Sebastian Thrun je dobra osoba. Sebastian Thrunova genetska "
        "predispozicija je povećala šansu da bude kolekcionar knjiga."
        "Pera je drugi lik u ovoj priči.")

text = ("ZAPISNIK"
"o izvršenom inspekcijskom nadzoru"
"Dana 31.01.2025. godine, u 11.30. časova, ovlašćena lica Poverenika, Biljana Nenadić, br."
"službene legitimacije 011 i Olja Živković, br. službene legitimacije 023, izvršila su"
"vapredan terenski inspekcijski nadzor nad primenom ZZPL od strane Predškolske ustanove"
"Čukarica, Požeška 28, Beograd (u daljem tekstu: nadzirani subjekat ili Rukovalac)."
"Nadzor je izvršen po nalogu šefa Odseka za nadzor br. 072-21-26/2025-07 od 22.01.2025. godine."
"1. Osnovi podaci o Nadziranom subjektu:"
"Poslovno ime nadziranog subjekta: Predškolska ustanove Čukarica Adresa zvanične veba prezentacije: ćir :/risikansa.tv/ Matični broj: 07009496 PIB: 100974365"
"Adresa: Požeška 28, Beograd"
"Zakonski zastupnik Rukovaoca je Biljana Gajić, direktor ustanove, br. lične karte"
"Kao predstavnici nadziranog subjekta, vršenju nadzora prisustvovali su:"
"- Biljana Gajić, direktor ustanove"
"- Olivera Jovanović, broj lične karte tekretar ustanove, lice za zaštitu podataka"
"o ličnosti."
"ke"
""
"2. Predmet nadzora"
"Predmet vanrednog terenskog inspekcijskog nadzora je obrada podataka o ličnosti dece putem"
"audio video snimaka i pristanak za obradu podataka o ličnosti dece u predškolskoj ustanovi."
"3. Tok i sadržaj preduzetih radnji radi utvrđivanja činjenica i drugih radnji u"
"postupku"
"Ovlašćena lica Poverenika su utvrdila da je nadzirani subjekat dostavio Poversniku kontakt"
"podatke lica za zaštitu podataka o ličnosti, Olivere Jovanović."
"Ovlašćena lica Poverenika su utvrdila da se u predstavci, na osnovu koje je pokrenut postupak"
"vanrednog inspekcijskog nadzora, navodi da je Dragana Mikić, zaposlena kao vaspitačica PU"
"Čukarica, fotografisala i snimala dete Lazara Pavkovića svojim privatnim telefonom, bez"
"odgovarajućeg pravnog osnova, kao i da je dete, u situacijama kada nije želelo da spava,"
"ucenjivala da će ga snimiti i fotografisati."
"4. Izjave prisutnih predstavnika nadziranog subjekta"
"Na pitanje ovlašćenog lica Poverenika da li je vaspitačica Dragana Mikić fotografisala i"
"snimala dete Lazara Pavkovića, i ako jeste koja je svrha i pravni osnov obrade, predstavnici"
"nadziranog subjekta su se izjasnili na sledeći način:"
"Svi vaspitači imaju obavezu da dokumentuju svoj rad i sprovođenje propisanog programa i"
"projekata i da je fotografisanje i snimanje dece jedan od načina na koji se dokumentovanje vrši."
"Prema izjavi predstavnica nadziranog subjekta, svrha obrade i pravni osnov propisani"
"Pravilnikom o osnovama programa predškolskog vaspitanja i obrazovanja („Službeni glasnik"
"RS – Prosvetni glasnik“, broj 16/2018). Prema izjavi predstavnika, u aktu koji predstavlja"
"sastavni deo Pravilnika - Osnove programa predškolskog vaspitanja i obrazovanja, u poglavlju:"
"Praćenje, vrednovanje i dokumentovanje, podnaslov: Oblici i način praćenja, navedeno je:"
"„Proces učenja i razvoja deteta se prati i dokumen tuje kroz dečji portfolio. Kroz portfolio se"
"dokumentuje napredovanja deteta kojim se ističe šta su jake strane deteta, dečja perspektiva"
"si' tuacij a, aktivnosti i dog ađaja, način pružanja podrške detetu, naročito kada su u pitanju deca"
"iz osetljivih grupa."
"za dokumentovanje kroz individualni portfolio mogu se koristiti: različite skale i druge"
"tehnike posmatranja i praćenja, grupne i individualne priče za učenje; produkti i iskazi deteta"
"nastali u konsultovanju sa decom, produkti deteta nastali u igri i u okviru teme/projekta:"
"fotografisanje, video i audio zapisi, nastali u različitim situacijama koji su detetu posebno"
"važni.“"
"Na pitanje ovlašćenih lica Poverenika koji je pravni osnov za upotrebu ličnih telefona."
"vaspitača prilikom fotografisanja i snimanja dece, predstavnice nadziranog subjekta su"
"izjavile da su predškolske ustanove, prilikom izvršavanja obaveza iz okvira svojih"
"nadležnosti, u obavezi da primenjuju Priručnik za dokumentovanje - Pedagoška dokumentacija"
"i dokumentovanje u Osnovama programa PVO „Godine uzleta“ , autora prof. dr Živka Krnjaja"
"2"
""
"prof. dr Dragana Pavlović Breneselović, izdavač Ministarstvo prosvete, nauke i tehnološkog"
"razvoja."
"U priručniku se navodi: „Priručnik za dokumentovanje nastao je na Institutu za pedagogiju i"
"andragogiju Filozofskog fakulteta Univerziteta u Beogradu u okviru projekta „Inkluzivno"
"predškolsko vaspitanje i obrazovanje“, koji realizuje Ministarstvo prosvete, nauke i"
"tehnološkog razvoja Srbije u saradnji sa Institutom za pedagogiju i andragogiju i SMTSEE i uz"
"podršku Svetske banke. Priručnik za dokumentovanje pripada serijalu priručnika i vodiča pod"
"zajedničkim nazivom „Linije leta"" koji su pripremljeni na Institutu za pedagogiju i"
"andragogiju sa ciljem podrške primeni Osnova programa predškolskog vaspitanja i obrazovanja"
"„Godine uzleta,“"
"Predstavnice nadziranog subjekta su istakle, da je pravni osnov za upotrebu ličnih telefona"
"vaspitača sadržan u navedenom Priručniku za dokumentovanje, u kojem se na strani 53, naslov"
"Dokumentovanje nije samo fotografisanje, navodi sledeće:"
"Opo što vaspitači pajpre prepoznaju u ovom pristupu dokumentovanju jeste da je sad potrebno"
"fotografisati. Tačno je, fotoografiji se pridaje veliki značaj i da biste dokumentovali u"
"svakodnevnim situacijama potrebna vam je oprema ( idealno bi bilo foto aparat, kamera,"
"telefon, lapšton, štampač,...). To podrazumeva da vam je oprema pri ruci i na raspolaganju u"
"svakoj situaciji koju hoćete da dokumentujete. Na žalost, nemaju svi vrtići ovu opremu, niti su"
"vaspitači ti koji treba da je obezbede. Dok se ne reši pitanje opreme, uvek ćste koristiti"
"svoj telefon, ali to ne može biti konačno rešenje. Posedovanje barem minimalne opreme"
"mora postati standard i taj prioritet treba istipati u svakoj prilici. Ali to ne može biti"
"opravdanje da dokumentovanjs ne postans dso vaše svakodnevne prakse. Ne zaboravite,"
"dokumentovanje obuhvata i planiranje i razvijanje i praćenje procesa kroz panoe i panele i"
"korišćenje niza drugih tehnika osim fotografisanja."
"Na pitanje ovlašćenih lica Poverenika da li je vaspitačica Dragana Mikić, fotografisala i"
"snimala decu samo u svrhe koje su propisane Pravilnikom o osnovama programa predškolskog"
"vaspitanja i obrazovanja ili ih je fotografisala, kako se navod u prelstavci, kako bi ih"
"ucenjivala kada ne žele da spavaju, predstavnice nadziranog subjekta su izjavile da je u postupku"
"disciplinski postupak u kom se utvrđuje odgovorpost vaspitačice Dragapa Mikić u vezi sa"
"navodima iz predstavke, i da postupak nije okončan."
"Predstavnici nadziranom subjekta su priložile izjavu roditelja deteta Lazara Pavkovića,"
"kojim daju pristanak za obradu podataka o ličnosti deteta, u radnoj 2021/2022. godini. U izjavi"
"se između ostalog navodi:"
"„Svojim potpisom odobravam sledeće aktivposti u radpoj 2021/2022 godini;"
"Fotografisanje dece, snimanje video i audio zapisa javnih nastupa i različitih aktivnosti dece i objavljivanje na sajtu PU Čukarica i društvenim mrežama PU Čukarica. 2. Slanje dečijih radova na izložbe u organizaciji PU Čukarica i objavljivanje na sajtu PU 3. Formiranje on lajn zajednica Vrtić u porodici“."
"Čukarica, Jutjub kanalu i društvenim mrežama PU Čukarica")

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
