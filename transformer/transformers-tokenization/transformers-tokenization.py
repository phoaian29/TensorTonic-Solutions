class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        """
        self.word_to_id = {
            self.pad_token: 0,
            self.unk_token: 1,
            self.bos_token: 2,
            self.eos_token: 3,
        }
        words = sorted({
            word
            for text in texts
            for word in text.lower().split()
        })
        for word in words:
            if word not in self.word_to_id:
                new_id = len(self.word_to_id)
                self.word_to_id[word] = new_id

        self.id_to_word = {v: k for k, v in self.word_to_id.items()}
        self.vocab_size = len(self.id_to_word)


    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        text = text.lower()
        tokens = text.split()
        
        und_id = self.word_to_id.get(self.unk_token, 1)
        ids = [self.word_to_id.get(token, und_id) for token in tokens]
        return ids

    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        tokens = [self.id_to_word.get(idx, self.unk_token) for idx in ids]
        tokens = " ".join(tokens)
        return tokens