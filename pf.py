from p import Pessoa

#pessoa fisica herda de pessoa, todas as caracteristicas
class Pessoafisica(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento):
        super().__init__(nome, dt_nascimento) 
        self.cpf = cpf
       

    def __str__(self):
        return f'{super().__init__()} - {self.cpf}'

