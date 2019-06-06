class DataInvalidaException(BaseException):
    def __init__(self,data):
        super().__init__()
        self.data = data
    def __str__(self):
        return 'A DATA NAO E VALIDA'+self.data+' FORMATO CORRETO: DIA/MES/ANO'