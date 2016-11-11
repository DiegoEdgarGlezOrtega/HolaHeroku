import web

render = web.template.render('/')
urls = (
    '/home','index'
    #,'/variables(.*)','variables',
    #'/parametro(.*)','parametro',
)
class index:
    def GET (self):
        return render.index()
 '''
class variables:
    def GET(self,nombre):
        nombre = 'Dieguin'
        return render.variables(nombre)

class parametro:
    def GET(self,nombre):
        i = web.input(nombre=None)

        return render.parametro(i.nombre) 
 '''
if __name__ == '__main__':
    app = web.application(urls,globals())
    web.config.debug = True
    app.run()
