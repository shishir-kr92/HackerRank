def remove_duplicate(score_board):
    new_board = []
    for i in range(len(score_board)):
        if i == 0:
            new_board.append(score_board[i])
        elif score_board[i] != new_board[-1]:
            new_board.append(score_board[i])
    return new_board


def get_nearest_match(score_board, score, l_limit, u_limit):
    if u_limit > l_limit:
        mid = l_limit + int((u_limit - l_limit)/2)

        if score == score_board[mid]:
            return mid
        elif score < score_board[mid] :
            return get_nearest_match(score_board, score, mid+1, u_limit)

        return get_nearest_match(score_board, score, l_limit, mid-1 )
    else:
        if score < score_board[l_limit] :
            return l_limit + 1
        else:
            return l_limit


def climbing_leader_board(score_board, alice_score):
    score_board = remove_duplicate(score_board)
    rank_list = []
    for score in alice_score:
        j = 0
        index = get_nearest_match(score_board, score, 0, len(score_board)-1)
        rank_list.append(index + 1)
    return rank_list


def climbing_leader_board_old(score_board, alice_score):
    rank_list = []
    for score in alice_score:
        j = 0
        rank = 1
        while j < len(score_board):
            if score_board[j] > score:
                if j == 0:
                    rank += 1
                elif j != 0 and score_board[j] != score_board[j-1]:
                    rank += 1
                j +=1
            elif score_board[j] <= score:
                break
        rank_list.append(rank)
    return rank_list


if __name__ == "__main__":
    '''
        https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
        
    '''
    n = int(input().strip())
    score_board = list(map(int, input().strip().split()))
    m = int(input())
    alice_score = list(map(int, input().strip().split()))
    result = climbing_leader_board(score_board, alice_score)
    print(result)


