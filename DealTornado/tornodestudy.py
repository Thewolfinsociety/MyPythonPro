# _*_ coding:utf-8 _*_

#@Time :2019/11/26 

# @Author : litao

# @File : tornodestudy.py

import tornado.ioloop
import tornado.web

from tornado import gen, web
import tcelery, tasks

tcelery.setup_nonblocking_producer()

class AsyncHandler(web.RequestHandler):

    async def get(self):
          tasks.echo.apply_async(args=['Hello world!'], callback=self.on_result)

    def on_result(self, response):
        self.write(str(response.result))
        self.finish()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hello",AsyncHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8887)
    tornado.ioloop.IOLoop.current().start()