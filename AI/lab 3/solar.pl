rotates(earth,sun).
rotates(mars,sun).
rotates(moon,earth).
planet(X) :-rotates(X,sun).
