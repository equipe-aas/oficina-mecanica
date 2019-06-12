from excessoes.DataInvalidaException import DataInvalidaException
from excessoes.DescricaoInvalidaException import DescricaoInvalidaException
from excessoes.EmailInvalidoException import EmailInvalidoException
from excessoes.CnpjInvalidoException import CnpjInvalidoException
from excessoes.EnderecoInvalidoException import EnderecoInvalidoException
from excessoes.CpfInvalidoException import CpfInvalidoException
from excessoes.NomeInvalidoException import NomeInvalidoException
from excessoes.RgInvalidoException import RgInvalidoException
from excessoes.TelefoneInvalidoException import TelefoneInvalidoException
from excessoes.ValorInvalidoException import ValorInvalidoException

class ValidaDados:
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    @staticmethod
    def __isCpf__(cpf):
        if (len(cpf) < 11):
            return False
        for i in list(cpf):
            if (i not in ValidaDados.n):
                return False
        return True

    @staticmethod
    def __isNumeric__(string):

        for i in list(string):
            if i not in ValidaDados.n:
                return False

        return True
    @staticmethod
    def isEmail(email):
        if '@' in list(email):
            return True
        else:
            return False
    @staticmethod
    def validaFornecedor(cnpj, nome, telefone, email, endereco):
        if not ValidaDados.__isNumeric__(cnpj):
            raise CnpjInvalidoException(cnpj)
        if len(nome) < 5:
            raise NomeInvalidoException(nome)
        if len(telefone) < 8 and ValidaDados.__isNumeric__(telefone):
            raise TelefoneInvalidoException(telefone)
        if not ValidaDados.isEmail(email):
            raise EmailInvalidoException(email)
        if(len(endereco) < 5):
            raise EnderecoInvalidoException()
        else:
            return True
    @staticmethod
    def validaCliente(cpf, nome, endereco, telefone):
        if not ValidaDados.__isCpf__(cpf):
            raise CpfInvalidoException(cpf)
        if len(nome) < 5:
            raise NomeInvalidoException(nome)
        if len(telefone) < 8:
            raise TelefoneInvalidoException(telefone)
        if (len(endereco) < 5):
            raise EnderecoInvalidoException()
        else:
            return True
    @staticmethod
    def validaFuncionario(rg, cpf, nome, data_nasc, salario,endereco,telefone):
        if len(data_nasc) == 10 and\
           ValidaDados.__isNumeric__(data_nasc[0]) and ValidaDados.__isNumeric__(data_nasc[1]) and data_nasc[2] == '/' and\
           ValidaDados.__isNumeric__(data_nasc[3]) and ValidaDados.__isNumeric__(data_nasc[4]) and data_nasc[5] == '/' and\
           ValidaDados.__isNumeric__(data_nasc[6]) and ValidaDados.__isNumeric__(data_nasc[7]) and\
           ValidaDados.__isNumeric__(data_nasc[8]) and ValidaDados.__isNumeric__(data_nasc[9]):
            raise DataInvalidaException(data_nasc)
        if ValidaDados.__isCpf__(cpf):
            raise CpfInvalidoException(cpf)
        if ValidaDados.__isNumeric__(rg) != None:
            raise RgInvalidoException(rg)
        if len(nome) < 5:
            raise NomeInvalidoException(nome)
        if (len(endereco) < 5):
            raise EnderecoInvalidoException()
        if(salario < 0):
            raise ValorInvalidoException(salario)
        if(len(telefone) < 8 or not ValidaDados.__isNumeric__(telefone)):
            raise TelefoneInvalidoException(telefone)
        else:
            return True
    @staticmethod
    def validaPeca(descricao, preco_custo, preco_venda, quantidade):
        if len(descricao)<5 :
            raise DescricaoInvalidaException(descricao)
        if preco_custo < 0:
            raise ValorInvalidoException(preco_custo)
        if preco_venda < 0:
            raise ValorInvalidoException(preco_venda)
        if quantidade < 0:
            raise ValorInvalidoException(quantidade)
    @staticmethod
    def validaServico( descricao, preco_venda):
        if (len(descricao) < 5):
            raise DescricaoInvalidaException(descricao)
        if (preco_venda < 0):
            raise ValorInvalidoException(preco_venda)
