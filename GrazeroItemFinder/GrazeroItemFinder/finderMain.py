"""
ItemFinderメインクラス
"""

from urllib.request import urlopen

# コンスト
ITEM_LIST_URL = 'http://game.granbluefantasy.jp/#item'
HTTP_STATUS_OK = '200'

# restでアイテムリストを取得してHTML形式を返す。
def get_item_list():
    return urlopen(ITEM_LIST_URL)







# 実行クラス
def finderMain():
    res = get_item_list()
    if str(res.getcode()) != HTTP_STATUS_OK:
        print('アイテムリスト取得失敗！：' + str(res.getcode()))
    else:
        print(res.read().decode('utf-8'))