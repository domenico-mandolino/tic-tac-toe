# ia.py

def ia(board, signe):
    """
    Fonction d'intelligence artificielle utilisant l'algorithme minimax pour le Tic Tac Toe.

    Parameters:
    - board (list): Liste représentant l'état actuel du plateau de jeu.
    - signe (str): Le signe de l'IA ("X" ou "O").

    Returns:
    - best_move (int): La meilleure position pour le prochain mouvement de l'IA, de 0 à 8.
    - False en cas d'erreur.
    """

    # Vérifier si le signe est valide
    if signe not in ["X", "O"]:
        return False

    # Définir le signe de l'adversaire
    adversaire = "O" if signe == "X" else "X"

    # Fonction d'évaluation pour l'algorithme minimax
    def evaluate():
        # Vérifier s'il y a un gagnant
        for i in range(3):
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != 0:
                return 1 if board[i * 3] == signe else -1
            if board[i] == board[i + 3] == board[i + 6] != 0:
                return 1 if board[i] == signe else -1
        if board[0] == board[4] == board[8] != 0:
            return 1 if board[0] == signe else -1
        if board[2] == board[4] == board[6] != 0:
            return 1 if board[2] == signe else -1

        # Aucun gagnant, le jeu est soit en cours soit un match nul
        return 0

    # Fonction minimax récursive
    def minimax(depth, maximizing_player):
        score = evaluate()

        # Si la partie est terminée, retourner le score
        if score != 0:
            return score

        # Si le jeu est un match nul, retourner 0
        if 0 not in board:
            return 0

        # Maximiser ou minimiser en fonction du joueur en cours
        if maximizing_player:
            max_eval = float("-inf")
            for i in range(9):
                if board[i] == 0:
                    board[i] = signe
                    eval = minimax(depth + 1, False)
                    board[i] = 0  # Annuler le mouvement
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for i in range(9):
                if board[i] == 0:
                    board[i] = adversaire
                    eval = minimax(depth + 1, True)
                    board[i] = 0  # Annuler le mouvement
                    min_eval = min(min_eval, eval)
            return min_eval

    # Initialiser les valeurs pour choisir le meilleur mouvement
    best_eval = float("-inf")
    best_move = -1

    # Trouver le meilleur mouvement en parcourant toutes les positions possibles
    for i in range(9):
        if board[i] == 0:
            board[i] = signe
            move_eval = minimax(0, False)
            board[i] = 0  # Annuler le mouvement

            # Mettre à jour le meilleur mouvement si nécessaire
            if move_eval > best_eval:
                best_eval = move_eval
                best_move = i

    return best_move
