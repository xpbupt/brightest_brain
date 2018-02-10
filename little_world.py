# coding:utf8
import numpy as np
import random


# params:
# dimension: 点灯矩阵的大小， 可以自行设置
# turns: 游戏的轮数上线（不过当所有灯被点亮，游戏会提前结束）


def gen_metrcis(dimension):
    metrics = np.zeros((dimension, dimension))
    for i in range(dimension):
        for j in range(dimension):
            if i == j:
                metrics[i][j] = 1
            else:
                metrics[i][j] = 1 if random.random() > 0.7 else 0
    # 对称矩阵
    metrics = np.triu(metrics)
    metrics += metrics.T - np.diag(metrics.diagonal())
    return metrics

def light_node(metrics, node_num, available_node, set_add, set_minus, dimension):
    row_list = metrics[node_num]
    node_list = set([node_num+1])
    for i in range(dimension):
        if row_list[i]:
            node_list.add(i+1)
    set_add.update(node_list)
    set_minus.difference_update(node_list)
    available_node.difference_update(node_list)


def get_input(available_node):
    while available_node:
        input_num = input()
        if input_num in available_node:
            return input_num
        else:
            print 'please input availabled num'
    return 0

def get_available_node(dimension):
    available_node = range(dimension+1)
    available_node.pop(0)
    return set(available_node)


def start_game(metrics, dimension, turns):
    available_node = get_available_node(dimension)
    player_a_node = set()
    player_b_node = set()
    for i in range(turns):
        print 'Player A, input: '
        a = get_input(available_node) - 1
        if a == -1: break
        light_node(metrics, a, available_node, player_a_node, player_b_node, dimension)
        print 'Score A:B = %d:%d' %(len(player_a_node), len(player_b_node))
        print 'Player_A: %s\nPlayer_B: %s' % (list(player_a_node), list(player_b_node))
        print 'Number Availabled: %s' % available_node

        print 'Player B, input: '
        b = get_input(available_node) - 1
        if b == -1: break
        light_node(metrics, b, available_node, player_b_node, player_a_node, dimension)
        print 'Score A:B = %d:%d' % (len(player_a_node), len(player_b_node))
        print 'Player_B: %s\nPlayer_A:%s' % (list(player_b_node), list(player_a_node))
        print 'Number Availabled: %s' % available_node

    print 'Final result: \n Player_A: %s \n Player_B: %s' % (list(player_a_node), list(player_b_node))
    print 'Winner: Player_A' if len(player_a_node) > len(player_b_node) else\
          'Winner: Player_B' if len(player_a_node) < len(player_b_node) else\
          'Deuce！'

def main():
    print 'input dimension:'
    dimension = input()
    print 'input turns:'
    turns = input()
    metrics = gen_metrcis(dimension)
    print 'metrics: \n %s' % metrics
    start_game(metrics, dimension, turns)

main()
