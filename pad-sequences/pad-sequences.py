import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)
    longest = max((len(seq) for seq in seqs), default=0)
    if max_len is None:
        L = longest
    else:
        L = max_len
    out = np.full((N, L), pad_value)
    
    for i, seq in enumerate(seqs):
        seq = np.asarray(seq)
        copy_len = min(len(seq), L)  # cắt chuỗi nếu dài hơn L
        out[i, :copy_len] = seq[:copy_len]
    
    return out
    pass