def extract_contexts(text: str, stopwords: list) -> dict:
    """
        Extracts the context of each word in a given text, excluding stopwords.

        The function identifies the words that are not in the stopwords list and
        collects the words that appear immediately to the left and right of them.
        Stopwords may appear in the contexts of other words.

        Args:
            text (str): The input text to process.
            stopwords (list of str): A list of stopwords to exclude from keys in the resulting dictionary.

        Returns:
            dict: A dictionary where:
                - Keys are words from the text that are not stopwords.
                - Values are tuples of two sets:
                    * The first set contains words immediately to the left of the key.
                    * The second set contains words immediately to the right of the key.

        """
#text wird in wörter zerlegt
    words = text.split()

    contexts = {}

    for i, word in enumerate(words): #durchläuft alle wörter mit index
        if word not in stopwords: #ignoriert stoppwörter
            left_context = set()
            right_context = set()

            if i > 0: #prüft ob linker nachbar existiert
                left_context.add(words[i - 1]) #fügt li. wort hinzu

            if i < len(words) - 1:#prüft ob re. nachbar exist.
                right_context.add(words[i + 1])#fügt re. wort hinzu

            if word in contexts:#falls wort schon existi.
                contexts[word][0].update(
                    left_context)
                contexts[word][1].update(right_context)  # the right set for the current word is updated by adding words
                
                
            else:
                contexts[word] = (left_context, right_context)
    return contexts


my_string = "this is an example string and this example is very short"
my_stopwords = ['this', 'is', 'an', 'and', 'very']
result = extract_contexts(my_string, my_stopwords)

print(result)
# {'example': ({'an', 'this'}, {'is', 'string'}), 'string': ({'example'}, {'and'}), 'short': ({'very'}, set())}
