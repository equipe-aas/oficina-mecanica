class ValidaDados:
    def __isCpf__(self, cpf):
        if (len(cpf) < 11):
            return False

        n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in list(cpf):
            if (i not in n):
                return False
        return True

    def __isNumeric__(self,string):
        n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in list(string):
            if i not in n:
                return False

        return True

