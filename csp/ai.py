class CSP:
    def next_move(self):
        moves = []
        
        for i in range(0, 3):
            for j in range(0, 3):
                
                if self.current_state[i][j] == '.':
                    
                    self.current_state[i][j] = 'O'
                    result = self.is_end()
                    if result == 'O':
                        return (i, j)
                    
                    self.current_state[i][j] = 'X'
                    result = self.is_end()
                    if result == 'X':
                        return (i, j)
                    
                    self.current_state[i][j] = '.'
                    moves.append((i,j))
        
        if (1,1) in moves:
            return (1,1)
        
        return sorted(moves)[-1]

