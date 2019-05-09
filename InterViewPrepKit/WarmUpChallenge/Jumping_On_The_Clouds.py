import sys


def jump_count(clouds, index):
    if index >= len(clouds) or clouds[index] == 1:
        return sys.maxsize
    elif index == len(clouds) - 1:
        return 0
    else:
        return min( 1 + jump_count(clouds, index + 1), 1  + jump_count(clouds, index + 2))


def get_min_jump(no_of_cloud, clouds):
        return jump_count(clouds, 0)


if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
    """
    no_of_cloud = int(input().strip())
    clouds = list(map(int, input().strip().split()))
    result  = get_min_jump(clouds)
    print(result)
