def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    x_old = x0
    for i in range(steps):
        x_new = x_old - lr * (2*a*x_old + b)
        x_old = x_new
    return x_new