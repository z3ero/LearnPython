# 一摞有序的纸牌
# 纸牌类——实现纸牌的各个相关操作
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # 表示可对该类对象 调用 len() 方法
    def __len__(self):
        return len(self._cards)

    # 表示可对该类对象
    # 1. 调用 [] 索引
    # 2. 该类对象支持切片
    # 3. 该类对象支持迭代
    def __getitem__(self, position):
        return self._cards[position]

    # 实现洗牌功能
    def __setitem__(self, key, value):
        pass

# 升序排序功能: 用点数来判定扑克牌大小，2最小，A最大; 再加上花色，黑桃 > 红桃 > 方块 > 梅花
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)   # 从FrenchDeck ranks 序列中找出 card.rank 的位置
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__=="__main__":
    deck = FrenchDeck()
    # 索引
    print(deck[4])
    # 切片
    print(deck[8:10])
    # 迭代
    for each in deck:
        print(each)
        break
    # 随机选取
    from random import choice
    print(choice(deck))

    # 按照指定的排序函数排序, 默认是升序
    for card in sorted(deck, key=spades_high):
        print(card)
