class MyArray:
    def __init__(self):
        self.data = {}
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    # 引数に指定されたindexに該当する要素を取得するメソッド
    def get(self, index):
        return self.data[index]

    # Arrayの一番最後に要素を追加するメソッド
    def push(self, item):
        # self.length-1が現状の要素の数なので、それに１を足したself.length番目に要素を追加
        self.data[self.length] = item
        # １つ要素を追加したので、要素数も +1
        self.length += 1

    # Arrayの一番最後の要素を削除し、その値を取得するメソッド
    def pop(self):
        # 削除する、Arrayの最後の要素を取得
        lastItem = self.data[self.length - 1]
        # Arrayの最後の要素を削除
        del(self.data[self.length - 1])
        # １つ要素を削除したので、要素数も -1
        self.length -= 1
        return lastItem

    # Arrayの引数に指定されたindexの要素を削除し、その値を取得するメソッド
    def delete(self, index):
        # 指定されたindexの削除する要素を取得
        deletedItem = self.data[index]
        # 指定されたindex以降の要素を１つ前にズラしていく
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        # 現状だと、元々の配列の最後の数が data[length - 2]とdata[length - 1]
        # ２つ存在している状態なので、２つ目の方を削除
        del self.data[self.length - 1]
        # １つ要素を削除したので、要素数も -1
        self.length -= 1
        return deletedItem


if __name__ == '__main__':
    myArray = MyArray()
    myArray.push('hi')
    myArray.push('you')
    myArray.push('!')
    print(myArray)