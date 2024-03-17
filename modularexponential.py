def mod_exp(base, exponent, modulus):
  """
  This function calculates the modular exponentiation (base ^ exponent) % modulus.

  Args:
      base: The base number.
      exponent: The exponent.
      modulus: The modulus.

  Returns:
      The result of (base ^ exponent) % modulus.
  """
  result = 1
  while exponent > 0:
    # If the exponent is odd, multiply by base
    if exponent % 2 == 1:
      result = (result * base) % modulus
    # Square the base and halve the exponent (binary exponentiation)
    exponent //= 2
    base = (base * base) % modulus
  return result

# Example usage
base = 2
exponent = 5
modulus = 13

result = mod_exp(base, exponent, modulus)
print(f"{base}^{exponent} % {modulus} = {result}")
