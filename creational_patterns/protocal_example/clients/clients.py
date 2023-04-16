"""A module to combine the sub structures in dogs and humans"""
from creational_patterns.protocal_example.clients.humans import get_clients as get_human_clients
from creational_patterns.protocal_example.clients.dogs import get_clients as get_dog_clients

def get_clients() -> list:
    """returns all the dogs and humans in one list"""
    return get_human_clients() + get_dog_clients()
