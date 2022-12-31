class AlphaBeta:
    def max(self, alpha, beta):
        maxv = -2
        px = None
        py = None

        result = self.is_end()
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'
                    alpha = max(alpha, m)
                    if beta <= alpha:
                        break
        return (maxv, px, py)

    def min(self, alpha, beta):
        minv = 2
        qx = None
        qy = None

        result = self.is_end()
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'
                    beta = min(beta, m)
                    if beta <= alpha:
                        break
        return (minv, qx, qy)
