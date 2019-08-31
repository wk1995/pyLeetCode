import abc


class Q(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def answer(self):
        '子类必须定义读功能'
        pass
