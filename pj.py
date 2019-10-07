from p import Pessoa

class Pessoajuridica:
    def __init__(self, nome, cnpj, dt_criacao, endereço):
        super().__init__(nome, dt_criacao, endereço)
        self.cnpj = cnpj 

    def __str__(self):
        return f'{super().__init__()} - {self.cnpj} '
       


