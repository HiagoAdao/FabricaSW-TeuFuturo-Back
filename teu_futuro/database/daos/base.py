from abc import ABCMeta, abstractmethod


class DAOBase(metaclass=ABCMeta):

    @abstractmethod
    def obter_todos(self):
        pass

    @abstractmethod
    def salvar(self):
        pass
