def num_reversal(start, stop, round=5, forward = True):
	while round >0:
		if forward:
			for i in range(start,stop+1):
				print (i, end=' ')
			print ('\n')
			forward =False
		else:
			for i in range(stop,start-1, - 1):
				print (i, end =' ')
			print ('\n')
			forward = True
		round -= 1

start = int(input ('start from: '))
end = int(input ('end at: '))
round = int(input ('how many rounds: '))

num_reversal(start, end, round)