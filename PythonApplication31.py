"""Main python file the will iterate over all design pattern examples and execute them"""
import builtins as b

def indent_print(*args, **kwargs) -> None:
    """
    A function that will indent the print
    overwritten the builtins.print to give a nice output
    """
    b.__print("      ",*args,**kwargs)

def importer(item: str) -> None:
    """Import the actual module"""
    __import__(item)

def import_list(items: list[str]) -> None:
    """A list of items to import, pre print the module for clarity"""
    for this_import in items:
        print("####  ", this_import, "  ####")
        b.print = indent_print
        importer(this_import)
        b.print = b.__print

def main() -> None:
    b.__print = b.print

    #Structural design patterns
    import_list(["structural_patterns.adapter_example.main",
                 "structural_patterns.bridge_example.main",
                "structural_patterns.composite_example.main",
                "structural_patterns.decorator_example.main",
                "structural_patterns.delegation_example.main",
                "structural_patterns.facade_example.main",
                "structural_patterns.flyweight_example.main",
                "structural_patterns.front_controller_example.main",
                "structural_patterns.proxy_example.main"])

    #Behavioural design patterns
    import_list(["behavioural_patterns.chain_of_responsibility_example.main",
                 "behavioural_patterns.command_example.main",
                "behavioural_patterns.iterator_example.main",
                "behavioural_patterns.mediator_example.main",
                "behavioural_patterns.memento_example.main",
                "behavioural_patterns.observer_example.main",
                "behavioural_patterns.servant_example.main",
                "behavioural_patterns.state_example.main",
                "behavioural_patterns.strategy_example.main",
                "behavioural_patterns.template_method_example.main",
                "behavioural_patterns.visitor_example.main"])

    #Creational design patterns
    import_list(["creational_patterns.factory_abstract_example.main",
                 "creational_patterns.factory_method_example.main",
                "creational_patterns.builder_example.main",
                "creational_patterns.dependency_injection_example.main",
                "creational_patterns.lazy_initialization_example.main",
                "creational_patterns.object_pool_example.main",
                "creational_patterns.singleton_example.main"])

    del b.__print

main()
