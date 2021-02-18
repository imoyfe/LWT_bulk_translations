de_sep_prep_prefixes = ["ab", "an", "auf", "aus", "bei", "mit", "nach", "statt", "vor", "zu"]
de_sep_adv_prefixes = ["fort", "los", "nieder", "vorbei", "weg", "zurück", "zusammen"]

de_insep_prefixes = ["be", "emp", "ent", "er", "ge", "miss", "ver", "zer"]
de_sep_insep_prefixes = ["durch", "über", "um", "unter", "wider"]

de_noun_suffixes = ["ant", "antin", "är", "ärin", "art", "at", "ator", "chen", "e", "ei", "el", "ent", "entin", "er", "erei", "erin", "eur", "eurin", "euse", "heit", "i", "ie", "ik", "ismus", "ist", "ität", "istin", "keit", "kunde", "lein", "ler", "ling", "nis", "ologie", "or", "orin", "öse", "sal", "schaft", "sel", "sorte", "st", "t", "tät", "tum", "ung", "wesen", "zeug"]
de_verb_adv_suffixes = ["arm", "artig", "bar", "en", "er", "erlei", "erlich", "fach", "fältig", "frei", "gemäß", "haft", "haftig", "ig", "iv", "isch", "leer", "lich", "los", "mal", "malig", "mäßig", "reich", "voll", "sam", "wert", "würdig"]


de_prefixes = de_sep_adv_prefixes + de_sep_prep_prefixes + de_sep_insep_prefixes + de_insep_prefixes
de_prefixes = sorted(de_prefixes, reverse=True)

de_suffixes = de_noun_suffixes + de_verb_adv_suffixes
de_suffixes = sorted(de_suffixes, reverse=True)

