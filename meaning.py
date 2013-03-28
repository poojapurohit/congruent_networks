def make_chapter_json(file):
    paras = get_paragraphs(file) # Requires paragraph-splitting function
    chapter = []
    for para in paras:
        paragraph = []
        sents = nltk.sent_tokenize(para)
        for sent in sents:
            sentence = []
            tokens = nltk.word_tokenize(sent)
            tag_tuples = nltk.pos_tag(tokens)
            for (string, tag) in tag_tuples:
                token = {'word':string, 'pos':tag}
                sentence.append(token)
            paragraph.append(sentence)
        chapter.append(paragraph)
    json_text = json.dumps(chapter)
    return json_text

def wordnet_pos_label(tag):
    if tag.startswith('NN'):
        return "Noun"
    elif tag.startswith('VB'):
        return "Verb"
    elif tag.startswith('JJ'):
        return "Adjective"
    elif tag.startswith('RB'):
        return "Adverb"
    else:
        return tag

def is_stopword(string):
    if string.lower() in nltk.corpus.stopwords.words('english'):
        return True
    else:
        return False

def is_punctuation(string):
    for char in string:
        if char.isalpha() or char.isdigit():
            return False
    return True
