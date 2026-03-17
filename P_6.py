import math

def minimax_pruned(level, node_pos, is_max_turn, leaf_scores, alpha, beta):

    if level == 3:
        return leaf_scores[node_pos]

    if is_max_turn:
        optimal = -math.inf

        for branch in range(2):
            child_val = minimax_pruned(level + 1, node_pos * 2 + branch,
                             False, leaf_scores, alpha, beta)
            optimal = max(optimal, child_val)
            alpha = max(alpha, optimal)

            if beta <= alpha:
                break

        return optimal

    else:
        optimal = math.inf

        for branch in range(2):
            child_val = minimax_pruned(level + 1, node_pos * 2 + branch,
                             True, leaf_scores, alpha, beta)
            optimal = min(optimal, child_val)
            beta = min(beta, optimal)

            if beta <= alpha:
                break

        return optimal


leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]

final_score = minimax_pruned(0, 0, True, leaf_scores, -math.inf, math.inf)

print("The optimal value is:", final_score)