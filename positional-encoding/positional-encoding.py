import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pe = np.zeros((seq_len, d_model))
    position = np.arange(0, seq_len)
    div_term = np.power(base, (np.arange(0, d_model, 2)/d_model))
    angle = position[:,None]/div_term[None,:]
    pe[:, 0::2] = np.sin(angle)
    pe[:, 1::2] = np.cos(angle[:, :d_model//2])

    return pe