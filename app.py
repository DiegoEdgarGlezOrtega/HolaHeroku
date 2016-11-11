import web

render = web.template.render('')
urls = (
    '/','index'
    #,'/variables(.*)','variables',
    #'/parametro(.*)','parametro',
)
class index:
    def GET (self):
        return render.index()
 
if __name__ == '__main__':
    app = web.application(urls,globals())
    web.config.debug = True
    app.run()
