"""This module contains a singleton decorator for a class"""

def singleton(this_class):
    """With this decorator, only one instance of the class can ever be instantiated"""
    singleton_instances = {}
    def get_instance():
        if this_class not in singleton_instances:
            singleton_instances[this_class] = this_class()
        return singleton_instances[this_class]
    return get_instance
