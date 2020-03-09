# _*_ coding:utf-8 _*_

#@Time :2019/11/27 

# @Author : litao

# @File : tornado6.py

__auth__ = "aleimu"
__doc__ = "学习tornado6.0+ 版本与python3.7+"

import time
import asyncio
import tornado.gen
import tornado.web
import tornado.ioloop
import tornado.httpserver  # tornado的HTTP服务器实现
from tornado.options import define, options
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from requests import get

settings = {'debug': True}
url = "http://127.0.0.1:5000/"  # 这是另个服务,请求5s后返回结果


# RuntimeError: Cannot run the event loop while another loop is running
# 解释:HTTPClient内部写 loop.run_xxx，因为那是启动event loop的命令，通常只再最最最外面用一次，之后的代码都应假设 loop 已经在运转了。
def synchronous_fetch(url):
    print("synchronous_fetch")
    try:
        http_client = HTTPClient()
        time.sleep(5)
        response = http_client.fetch(url)
        print(response.body)
    except Exception as e:
        print("Error: " + str(e))
        return str(e)
    http_client.close()
    return response.body


# 替代synchronous_fetch的同步请求,没有内置loop.run_xxx
def synchronous_get(url):
    response = get(url)
    time.sleep(5)
    print("synchronous_fetch")
    return response.text


# 简单的模拟异步操作,这里之后应该替换成各种异步库的函数
async def sleep():
    print("start sleep")
    await asyncio.sleep(5)
    print("end sleep")


# 异步请求
async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    print("asynchronous_fetch")
    return response.body


# 测试
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world:%s" % self.request.request_time())
        self.finish()
        print("not finish!")
        return


# 同步阻塞
class synchronous_fetcher(tornado.web.RequestHandler):
    def get(self):
        self.write("%s,%s" % (synchronous_fetch(url), self.request.request_time()))


# 同步阻塞
class synchronous_geter(tornado.web.RequestHandler):
    def get(self):
        self.write("%s,%s" % (synchronous_get(url), self.request.request_time()))


# 异步阻塞,我以为curl "127.0.0.1:8888/1" 总耗时希望为5s,可是是25s,看来异步没搞好,以下的函数都是基于此改进的
class asynchronous_fetcher_1(tornado.web.RequestHandler):
    async def get(self):
        body = await asynchronous_fetch(url)
        for i in range(3):
            print("skip %s" % i)
            await tornado.gen.sleep(5)
        time.sleep(5)
        print("end request")
        self.write("%s,%s" % (body, self.request.request_time()))

# curl "127.0.0.1:8888/1"
# b'{\n  "data": "123"\n}\n',25.026000022888184


# 异步阻塞,效果同上,这里只是证明 tornado.gen.sleep(5)和asyncio.sleep(5) 效果一致
class asynchronous_fetcher_2(tornado.web.RequestHandler):
    async def get(self):
        body = await asynchronous_fetch(url)  # 关注协程完成后返回的结果
        for i in range(3):
            print("skip %s" % i)
            await sleep()
        time.sleep(5)
        print("end request")
        self.write("%s,%s" % (body, self.request.request_time()))

# curl "127.0.0.1:8888/2"
# b'{\n  "data": "123"\n}\n',25.039999961853027


# 异步非阻塞-将部分异步操作放入组中,实现loop管理
class asynchronous_fetcher_3(tornado.web.RequestHandler):
    async def get(self):
        body = await asynchronous_fetch(url)
        await asyncio.wait([sleep() for i in range(3)])
        print("end request")
        self.write("%s,%s" % (body, self.request.request_time()))

# curl "127.0.0.1:8888/3"
# b'{\n  "data": "123"\n}\n',10.001000165939331

# 异步非阻塞-将所有异步操作放入组中,实现loop管理
class asynchronous_fetcher_4(tornado.web.RequestHandler):
    async def get(self):
        task_list = [sleep() for i in range(3)]
        task_list.append(asynchronous_fetch(url))
        body = await asyncio.wait(task_list)  # 将所有异步操作的结果返回,但是是无序的,要是需要返回结果的话解析起来比较麻烦
        #print("end request:", body)
        # print(type(body), len(body),type(body[0]),len(body[0]),type(body[0]))
        self.write("%s,%s" % ([x.result() for x in body[0] if x.result() is not None][0],
                              self.request.request_time()))
# curl "127.0.0.1:8888/4"
# b'{\n  "data": "123"\n}\n',5.006999969482422

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/1", asynchronous_fetcher_1),
        (r"/2", asynchronous_fetcher_2),
        (r"/3", asynchronous_fetcher_3),
        (r"/4", asynchronous_fetcher_4),
        (r"/5", synchronous_fetcher),
        (r"/6", synchronous_geter),

    ], **settings)


if __name__ == "__main__":
    print("server start!")
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)

    tornado.options.parse_command_line()
    server.bind(8888)
    server.start(1)  # forks one process per cpu,windows上无法fork,这里默认为1
    tornado.ioloop.IOLoop.current().start()