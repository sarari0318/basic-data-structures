from random import randint


class HashMap:
    def __init__(self):
        # Space:50 のHashMapを生成
        self.mydict = ['None']*50
        self.add_list = []

    def __str__(self):
        return str(self.__dict__)

    # データを追加する場所をここでランダムに指定
    def _hash(self):
        while True:
            # 0 <= n <= 49の整数を返す
            x = randint(0, 49)
            # add_listにxが存在しないとき、
            # つまり、addressがx、つまりはxがkeyのhashにデータが存在しないとき
            # この条件によって、Hash Collisionsが起こっていないaddressを把握することができる！
            if x not in self.add_list:
                return x

    def set(self, key, value):
        # _hashで生成したランダムな数字を、追加するデータのアドレスとする
        # つまり、_hashで決まった数のhashにデータを追加する！
        address = self._hash()
        # addressをkeyとするmydictのvalueとして[key, value]を追加する
        self.mydict[address] = [key, value]
        self.add_list.append(address)

    def get(self, key):
        for i in self.add_list:
            # もし、mydict[i][0]、つまり、mydictのi番目のkeyと、引数のkeyが等しければ、
            if self.mydict[i][0] == key:
                # mydict[i][1]、つまり、mydictのi番目のvalueを返す！
                return self.mydict[i][1]

    def keys(self):
        key_arr = []
        # こうすることで、今回でいうと50のハッシュ全てを確認するのではなく、
        # 値が入っているところだけ！をチェックできるので、非常に効率的！！！！！
        for i in self.add_list:
            # add_listに入っている数、つまりmydictの中でもデータが入った所のkeyをkey_arrに追加する
            key_arr.append(self.mydict[i][0])
        return key_arr


h=HashMap()
h.set('grapes',1000)
h.set('apples',10)
h.set('oranges',300)
h.set('bananas',200)
x=h.get('grapes')
key_arr = h.keys()
print(h)
print(x)
print(key_arr)