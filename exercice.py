#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	d_power = voltage**2/resistance
	return d_power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	scalar_prod = v1[0] * v2[0] + v1[1] * v2[1]
	if scalar_prod == 0:
		return True
	else:
		return False
def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	num_element = 0
	sum = 0
	for v in values:
		if v >= 0:
			sum += v
			num_element += 1


	average = sum /num_element

	return average

		# La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		twenties = 0
		tens = 0
		fives = 0
		ones= 0

		while value >= 20:
			value -= 20
			twenties += 1
		while value >= 10:
			value -= 10
			tens += 1
		while value >= 5:
			value -=5
			fives += 1
		while value >= 1:
			value -= 1
			ones += 1

	return (twenties, tens, fives, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		smallest_digit = abs_value % base
		result += digit_letters [smallest_digit]
		abs_value = abs_value // base

	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result += "-"

	result = result[::-1]
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
