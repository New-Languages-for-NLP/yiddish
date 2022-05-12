import re


def normalize(input, remove_diacritics=False, normalize_final_characters=False, tokenization_exceptions=False, normalize_double_quotes=True, normalize_hyphens=True, normalize_apostrophe=True):
    # https://nlp.stanford.edu/IR-book/html/htmledition/accents-and-diacritics-1.html
    # https://en.wikipedia.org/wiki/Hebrew_(Unicode_block)
    # https://www.cl.cam.ac.uk/~mgk25/ucs/quotes.html
    output = input
    # strip html tags
    regex = r"<(?:\\?).*?>"
    output = re.sub(regex, " ", output, 0, re.MULTILINE)

    # diacritics - chr(0x0591) - chr(0x05c7), except of chr(0x05be); ײַ שרײַבן
    if remove_diacritics is True:
        for c in range(1425, 1480):
            if c == 1470:
                continue
            output = output.replace(chr(c), "")
    # oy, ey, ... - 05f0, 05f1, 05f2: 'װ ױ ײ'
    output = output.replace(chr(0x05f0), "וו")
    output = output.replace(chr(0x05f1), "וי")
    output = output.replace(chr(0x05f2), "יי")
    # apostrophe - "' ′ ‘ ’ -> ׳" (chr(39)+" "+chr(0x2032)+" "+chr(0x2018)+" "+chr(0x2019)+" -> "+chr(0x05f3))
    if normalize_apostrophe is True:
        for c in [39, 0x2032, 0x2018, 0x2019]:
            output = output.replace(chr(c), chr(0x05f3))
    # double quotes : '" “ ” -> ״' (chr(0x22)+" "+chr(0x201c)+" "+chr(0x201d)+" -> "+chr(0x5f4))
    if normalize_double_quotes is True:
        for c in [0x22, 0x201c, 0x201d]:
            output = output.replace(chr(c), chr(0x05f4))
    # top hyphen 0x05be vs 0x2d: אני כותב בעברית - כך וכך, תל-אביב תל־אביב תל־אביב
    # output = re.sub("(\w+)-(\w+)", r"\1־\2", output)
    if normalize_hyphens is True:
        output = re.sub(r"(\w+)-(\w+)", rf"\1{chr(0x05be)}\2", output)
    # chr(0x05f3)+chr(0x05f3) inside a word -> to chr(0x5f4))
    output = re.sub(rf"(\w+){chr(0x05f3)}{chr(0x05f3)}(\w+)", rf"\1{chr(0x05f4)}\2", output)

    output = re.sub(r"(\w+)!(\w+)", rf"\1! \2", output)
    output = re.sub(r"(\w+)\?(\w+)", rf"\1\? \2", output)
    output = re.sub(r"(\w+)\.(\w+)", rf"\1\. \2", output)
    output = re.sub(r"(\w+);(\w+)", rf"\1; \2", output)

    if normalize_final_characters is True:
        output = output.replace('ם', 'מ')
        output = output.replace('ך', 'כ')
        output = output.replace('ץ', 'צ')
        output = output.replace('ף', 'פ')
        output = output.replace('ן', 'נ')

    if tokenization_exceptions is True:
        output = re.sub(r"\s?כ׳(\w+)", "כ׳ "+r"\1", output)
        output = re.sub(r"\s?ר׳(\w+)", "ר׳ "+r"\1", output)
        output = re.sub(r"\s?מ׳(\w+)", "מ׳ "+r"\1", output)
        output = re.sub(r"\s?ס׳(\w+)", "ס׳ "+r"\1", output)

    return output
