def tournamentWinner(competitions, results):
    # Write your code here.
	current_winner = ""
	win_tally = {current_winner: 0}
	
	for i, result in enumerate(results):
		winner = competitions[i][1 - result]
		if winner in win_tally:
			win_tally[winner] += 3
		else:
			win_tally[winner] = 3
		
		if win_tally[winner] > win_tally[current_winner]:
			current_winner = winner
        
    return current_winner