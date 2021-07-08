def fibada(n):
	if n == 1 or n == 0:
		return 1
	else:
		aux = fibada(n-1) + fibada(n-2)
		return aux


