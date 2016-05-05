#PRINT OUT THIS INFO AT THE BEGINNING
print('Welcome to the HEMIS calculator for the University of Stellenbosch.\nPlease follow the prompts and enter the relevant values.\nGoodluck! Hopefully you don\'t get catched by the monster!\n')

#INDICATE IF YOU STUDY NORMAL OR EXTENDED DEGREE
possible_degree = ['n', 'e', 'N', 'E']

tf = True 
while tf:
	try:
		degree = str(input('Indicate if you are doing a normal or extended degree by entering n or e (e.g. e):\n'))
	except ValueError:
		print('Error: That is invalid!\n')
		continue
	if degree not in possible_degree:
		print('Only enter the value n or e!')
	else:
		tf = False

degree = degree.lower()
if degree == 'n':
	import normal_degree as d
elif degree == 'e':
	import extended_degree as d

#PRINT OUT THIS INFO
print('When calculating HEMIS for a half of a year it will only be weighed against the HEMIS\nyou need to come back to Residence the next year!\nSo if you don\'t live in a Residence only calculate your HEMIS based on a yearly basis!\n')

#INPUT THE VALUE OF WHICH SEMESTER YOU WANT TO CALCULATE HEMIS FOR IF THE VALUE ISN'T A FLOAT IT WILL RUN A ERROR AND ASK FOR THE INPUT AGAIN
pos_values = {0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9}

tf = True
while tf:
	try:
		semester = float(input('For which semester do you want to calculate your HEMIS?\n(e.g. 0.5 for first half of 1st year, 1.5 to first half of 2nd year etc.)\nPlease enter yours now:\n'))
	except ValueError:
		print('Error: Only input number values!\n')
		continue
	if semester not in pos_values:
		print('Error: Inpossible value was entered!\n')
	else:
		tf = False

#THIS WILL RUN IF THEY ENTERED 0.5
if semester == 0.5:
	print('You need a HEMIS of', d.accyear0_5[1], 'to stay in Residence.')
	tf = True
	while tf:
		try:
			credits_tot_0_5 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_0_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_0_5 = int(input('Total credits for semester modules past in first semester 1st year and for year subjects with a acheivement mark of 48 and higher (e.g. 62):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemistot = credits_achieved_0_5 / credits_tot_0_5
	hemistot = round(hemistot,2)

	if hemistot > d.accyear0_5[1]:
		print('\nCongratulations, you are allowed to stay in Residence!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear0_5[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence!\nYou scored a HEMIS of', hemistot)


#THIS WILL RUN IF THEY ENTERED 1
if semester == 1:
	print('You need a HEMIS of', d.accyear1[1], 'to stay in Residence and you need a HEMIS of', d.acayear1[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemistot = credits_achieved_1 / credits_tot_1
	hemistot = round(hemistot,2)

	if hemistot > d.accyear1[1] and hemistot > d.acayear1[1]:
		print('\nCongratulations, you are allowed to stay in Residence and carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear1[1] and hemistot > d.acayear1[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence but you are allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear1[1] and hemistot < d.acayear1[1]:
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence nor are you allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)


#THIS WILL RUN IF THEY ENTERED 1.5
if semester == 1.5:
	print('You need a HEMIS of', d.accyear1_5[1], 'to stay in Residence!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_1_5 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1_5 = int(input('Total credits for semester modules past in first semester 2nd year and for year subjects with a acheivement mark of 48 and higher (e.g. 62):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis1_5 = credits_achieved_1_5 / credits_tot_1_5

	hemistot = hemis1 + hemis1_5
	hemistot = round(hemistot,2)

	if hemistot > d.accyear1_5[1]:
		print('\nCongratulations, you are allowed to stay in Residence!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear1_5[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 2
if semester == 2:
	print('You need a HEMIS of', d.accyear2[1], 'to stay in Residence and you need a HEMIS of', d.acayear2[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemistot = hemis1 + hemis2
	hemistot = round(hemistot,2)

	if hemistot > d.accyear2[1] and hemistot > d.acayear2[1]:
		print('\nCongratulations, you are allowed to stay in Residence and carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear2[1] and hemistot > d.acayear2[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence but you are allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear2[1] and hemistot < d.acayear2[1]:
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence nor are you allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 2.5
if semester == 2.5:
	print('You need a HEMIS of', d.accyear2_5[1], 'to stay in Residence!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2_5 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2_5 = int(input('Total credits for semester modules past in first semester 3rd year and for year subjects with a acheivement mark of 48 and higher (e.g. 62):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis2_5 = credits_achieved_2_5 / credits_tot_2_5
	hemistot = hemis1 + hemis2 + hemis2_5
	hemistot = round(hemistot,2)

	if hemistot > d.accyear2_5[1]:
		print('\nCongratulations, you are allowed to stay in Residence!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear2_5[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 3
if semester == 3:
	print('You need a HEMIS of', d.accyear3[1], 'to stay in Residence and you need a HEMIS of', d.acayear3[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemistot = hemis1 + hemis2 + hemis3
	hemistot = round(hemistot,2)

	if hemistot > d.accyear3[1] and hemistot > d.acayear3[1]:
		print('\nCongratulations, you are allowed to stay in Residence and carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear3[1] and hemistot > d.acayear3[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence but you are allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear3[1] and hemistot < d.acayear3[1]:
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence nor are you allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 3.5
if semester == 3.5:
	print('You need a HEMIS of', d.accyear3_5[1], 'to stay in Residence!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3_5 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3_5 = int(input('Total credits for semester modules past in first semester 4th year and for year subjects with a acheivement mark of 48 and higher (e.g. 62):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis3_5 = credits_achieved_2_5 / credits_tot_2_5
	hemistot = hemis1 + hemis2 + hemis3 + hemis3_5
	hemistot = round(hemistot,2)

	if hemistot > d.accyear3_5[1]:
		print('\nCongratulations, you are allowed to stay in Residence!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear3_5[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 4
if semester == 4:
	print('You need a HEMIS of', d.accyear4[1], 'to stay in Residence and you need a HEMIS of', d.acayear4[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemistot = hemis1 + hemis2 + hemis3 + hemis4
	hemistot = round(hemistot,2)

	if hemistot > d.accyear4[1] and hemistot > d.acayear4[1]:
		print('\nCongratulations, you are allowed to stay in Residence and carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear4[1] and hemistot > d.acayear4[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence but you are allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear4[1] and hemistot < d.acayear4[1]:
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence nor are you allowed to carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 4.5
if semester == 4.5:
	print('You need a HEMIS of', d.accyear4_5[1], 'to stay in Residence!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4_5 = int(input('Total credits needed for 5th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4_5 = int(input('Total credits for semester modules past in first semester 5th year and for year subjects with a acheivement mark of 48 and higher (e.g. 62):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemis4_5 = credits_achieved_4_5 / credits_tot_4_5
	hemistot = hemis1 + hemis2 + hemis3 + hemis4
	hemistot = round(hemistot,2)

	if hemistot > d.accyear4_5[1]:
		print('\nCongratulations, you are allowed to stay in Residence!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.accyear4_5[1]: 
		print('\nUnfortunately, you didn’t get sufficient HEMIS to stay in Residence!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 5
if semester == 5:
	print('You need a HEMIS of', d.acayear5[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_5 = int(input('Total credits needed for 5th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_5 = int(input('Total credits for modules past in 5th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemis5 = credits_achieved_5 / credits_tot_5
	hemistot = hemis1 + hemis2 + hemis3 + hemis4 + hemis5
	hemistot = round(hemistot,2)

	if hemistot > d.acayear5[1]:
		print('\nCongratulations, you are allowed to go on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.acayear5[1]:
		print('\nUnfortunately, you can’t carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 6
if semester == 6:
	print('You need a HEMIS of', d.acayear6[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_5 = int(input('Total credits needed for 5th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_5 = int(input('Total credits for modules past in 5th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_6 = int(input('Total credits needed for 6th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_6 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_6 = int(input('Total credits for modules past in 6th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemis5 = credits_achieved_5 / credits_tot_5
	hemis6 = credits_achieved_6 / credits_tot_6
	hemistot = hemis1 + hemis2 + hemis3 + hemis4 + hemis5 + hemis6
	hemistot = round(hemistot,2)

	if hemistot > d.acayear6[1]:
		print('\nCongratulations, you are allowed to go on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.acayear6[1]:
		print('\nUnfortunately, you can’t carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 7
if semester == 7:
	print('You need a HEMIS of', d.acayear7[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_5 = int(input('Total credits needed for 5th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_5 = int(input('Total credits for modules past in 5th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_6 = int(input('Total credits needed for 6th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_6 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_6 = int(input('Total credits for modules past in 6th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_7 = int(input('Total credits needed for 7th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_7 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_7 = int(input('Total credits for modules past in 7th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemis5 = credits_achieved_5 / credits_tot_5
	hemis6 = credits_achieved_6 / credits_tot_6
	hemis7 = credits_achieved_7 / credits_tot_7
	hemistot = hemis1 + hemis2 + hemis3 + hemis4 + hemis5 + hemis6 + hemis7
	hemistot = round(hemistot,2)

	if hemistot > d.acayear7[1]:
		print('\nCongratulations, you are allowed to go on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.acayear7[1]:
		print('\nUnfortunately, you can’t carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 8
if semester == 8:
	print('You need a HEMIS of', d.acayear8[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_5 = int(input('Total credits needed for 5th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_5 = int(input('Total credits for modules past in 5th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_6 = int(input('Total credits needed for 6th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_6 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_6 = int(input('Total credits for modules past in 6th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_7 = int(input('Total credits needed for 7th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_7 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_7 = int(input('Total credits for modules past in 7th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_8 = int(input('Total credits needed for 8th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_8 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_8 = int(input('Total credits for modules past in 8th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemis5 = credits_achieved_5 / credits_tot_5
	hemis6 = credits_achieved_6 / credits_tot_6
	hemis7 = credits_achieved_7 / credits_tot_7
	hemis8 = credits_achieved_8 / credits_tot_8
	hemistot = hemis1 + hemis2 + hemis3 + hemis4 + hemis5 + hemis6 + hemis7 + hemis8
	hemistot = round(hemistot,2)

	if hemistot > d.acayear8[1]:
		print('\nCongratulations, you are allowed to go on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.acayear8[1]:
		print('\nUnfortunately, you can’t carry on with your academics!\nYou scored a HEMIS of', hemistot)

#THIS WILL RUN IF THEY ENTERED 9
if semester == 9:
	print('You need a HEMIS of', d.acayear9[1], 'to carry on with your academics!')
	tf = True
	while tf:
		try:
			credits_tot_1 = int(input('Total credits needed for 1st year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_1 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_1 = int(input('Total credits for modules past in 1st year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_2 = int(input('Total credits needed for 2nd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_2 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_2 = int(input('Total credits for modules past in 2nd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_3 = int(input('Total credits needed for 3rd year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_3 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_3 = int(input('Total credits for modules past in 3rd year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_4 = int(input('Total credits needed for 4th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_4 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_4 = int(input('Total credits for modules past in 4th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_5 = int(input('Total credits needed for 5th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_5 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_5 = int(input('Total credits for modules past in 5th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_6 = int(input('Total credits needed for 6th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_6 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_6 = int(input('Total credits for modules past in 6th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_7 = int(input('Total credits needed for 7th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_7 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_7 = int(input('Total credits for modules past in 7th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_8 = int(input('Total credits needed for 8th year in total (e.g. 128):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_8 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_8 = int(input('Total credits for modules past in 8th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_tot_9 = int(input('Total credits needed for 9th year in total (e.g. 129):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
			continue
		if credits_tot_9 == 0:
			print('Value can\'t be zero!')
		else:
			tf = False
	tf = True
	while tf:
		try:
			credits_achieved_9 = int(input('Total credits for modules past in 9th year (e.g. 100):\n'))
		except ValueError:
			print('Error: Only input number values!\n')
		else:
			tf = False

	hemis1 = credits_achieved_1 / credits_tot_1
	hemis2 = credits_achieved_2 / credits_tot_2
	hemis3 = credits_achieved_3 / credits_tot_3
	hemis4 = credits_achieved_4 / credits_tot_4
	hemis5 = credits_achieved_5 / credits_tot_5
	hemis6 = credits_achieved_6 / credits_tot_6
	hemis7 = credits_achieved_7 / credits_tot_7
	hemis8 = credits_achieved_8 / credits_tot_8
	hemis9 = credits_achieved_9 / credits_tot_9
	hemistot = hemis1 + hemis2 + hemis3 + hemis4 + hemis5 + hemis6 + hemis7 + hemis8 + hemis9
	hemistot = round(hemistot,2)

	if hemistot > d.acayear9[1]:
		print('\nCongratulations, you are allowed to go on with your academics!\nYou scored a HEMIS of', hemistot)
	elif hemistot < d.acayear9[1]:
		print('\nUnfortunately, you can’t carry on with your academics!\nYou scored a HEMIS of', hemistot)

#END INFO
print('\nThank you for using the calculator!\nHope you could\'ve escaped the MONSTER!')
