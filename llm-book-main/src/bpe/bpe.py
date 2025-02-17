from collections import defaultdict
import re
from typing import Dict, List, Tuple


def get_stats(vocab: Dict[str, int]) -> Dict[Tuple[str, str], int]:
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs


def merge_vocab(pair: Tuple[str, str], vocab: Dict[str, int]) -> Dict[str, int]:
    v_out = defaultdict(int)
    bigram = " ".join(pair)
    p = re.compile(r"(?<!\S)" + re.escape(bigram) + r"(?!\S)")
    for word in vocab:
        w_out = p.sub("".join(pair), word)
        v_out[w_out] += vocab[word]
    return v_out


def bpe(vocab: Dict[str, int], num_merges: int) -> List[str]:
    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
    subwords = set()
    for word in vocab:
        for subword in word.split():
            subwords.add(subword)
    return list(subwords)


vocab = {"こ ん に ち は 世 界 。": 1, "こ ん ば ん は 世 界 。": 1}

for i in range(11):
    table = bpe(vocab, i)
    print(table)
