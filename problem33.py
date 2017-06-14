from fractions import Fraction
p = 1
for numer in range (10, 100):
   for denom in range (numer + 1, 100):
      frac = Fraction(numer, denom)
      nstr = str(numer)
      dstr = str(denom)
      if nstr[0] == dstr[1] and Fraction(int(nstr[1]), int(dstr[0])) == frac: p *= frac
      elif nstr[1] == dstr[0] and dstr[1] != "0" and Fraction(int(nstr[0]), int(dstr[1])) == frac: p *= frac
      elif nstr[0] == dstr[0] and dstr[1] != "0" and Fraction(int(nstr[1]), int(dstr[1])) == frac: p *= frac
      elif nstr[1] == dstr[1] and Fraction(int(nstr[0]), int(dstr[0])) == frac and nstr[1] != "0": p *= frac
print p.denominator
