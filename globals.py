from functools import wraps


template_inputs = {}

'''
注解,用于优雅地扩展任务类型
'''
taskSolver = {}
def task(type: str, description = "暂无描述"):
    assert task != None
    def decoratedFunc(func):
        @wraps(func)      
        def run(*args, **kwargs):
            return func(*args, **kwargs)
        taskSolver[type] = run
        return run
    return decoratedFunc
