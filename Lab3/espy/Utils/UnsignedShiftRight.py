def unsignedShiftRight(v, s):
  if(v < 0):
    return (v & (2**32-1)) >> s
  return v >> s