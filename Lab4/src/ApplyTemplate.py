import ast 
import inspect

def apply_template(*args):
    def make_decorator(func):
        dict = {}
        i = 0
        name = ""
        for arg in args:
            if i % 2 == 0:
                name = arg
            else:
                func_ast = ast.parse(inspect.getsource(arg)).body[0]   # AST för hela funktionen inklusive def
                body_node = func_ast.body       # ska vi betrakta AST för själva funktionen, inklusive def?
                dict[name] = body_node                
            i = i + 1

        template_ast = ast.parse(inspect.getsource(func))
        
        class T(ast.NodeTransformer):
            def visit_Expr(self, node):
                ret = node;
                if node.value.id == '__body__':
                    ret = dict['__body__']
                elif node.value.id == '__return__':
                    ret = dict['__return__']
                return ret

        template_ast.body[0].decorator_list.clear()
        exec(compile(T().visit(template_ast), __file__, mode='exec'))


        return locals()[template_ast.body[0].name]

    return make_decorator
