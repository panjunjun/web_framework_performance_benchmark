# coding: utf-8
# __author__: u"John"
import tornado.ioloop
import tornado.web
import json
import redis

r = redis.Redis(host=u"localhost", port=6379, db=0)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(u"Hello World!")

    def post(self):
        data = json.loads(self.request.body)
        value = r.get(data[u"key"])
        r.set(data[u"key"], data[u"value"])
        self.write(value)


application = tornado.web.Application([
    (ur"/", MainHandler),
])

if __name__ == u"__main__":
    application.listen(8124)
    tornado.ioloop.IOLoop.instance().start()

