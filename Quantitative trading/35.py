""""
import requests
import timeit


def get_orderbook():
  orderbook = requests.get("https://api.gemini.com/v1/book/btcusd").json()


n = 10
latency = timeit.timeit('get_orderbook()', setup='from __main__ import get_orderbook', number=n) * 1.0 / n
print('Latency is {} ms'.format(latency * 1000))

"""

import websocket
import _thread
import  time

# 在接收到服务器发送消息时调用
def on_message(ws, message):
    print('Received: ' + message)


# 在和服务器建立完成连接时调用
def on_open(ws):
    # 线程运行函数
    def gao():
        # 往服务器依次发送0-4，每次发送完休息0.01秒
        for i in range(5):
            time.sleep(0.01)
            msg = "{0}".format(i)
            ws.send(msg)
            print('Sent: ' + msg)
        # 休息1秒用于接收服务器回复的消息
        time.sleep(1)

        # 关闭Websocket的连接
        ws.close()
        print("Websocket closed")

    # 在另一个线程运行gao()函数
    thread.start_new_thread(gao, ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                                on_message=on_message,
                                on_open=on_open)

    ws.run_forever()
