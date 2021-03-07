"""
Verificação de CNPJ.

Módulo de cálculo de CNPJ completo.
"""
from collections import (
    deque,
    defaultdict
)
nums = defaultdict(lambda: 0)


def verif_cnpj(pass_cnpj):
    calculo_cnpj = []
    calculo_cnpj2 = []
    digitos = []
    if len(pass_cnpj) > 14:
        pass_cnpj = pass_cnpj.split(".")
        pass_cnpj = "".join(pass_cnpj)
        pass_cnpj = pass_cnpj.split("/")
        pass_cnpj = "".join(pass_cnpj)
        pass_cnpj = pass_cnpj.split("-")
        pass_cnpj = "".join(pass_cnpj)
    if len(pass_cnpj) < 14:
        return False
    cnpjv = deque(pass_cnpj)
    y = 0
    if len(digitos) < 1:
        for x in range(5, 1, -1):
            nums[y] = int(cnpjv[y])
            nums[y] = nums[y] * x
            calculo_cnpj.append(nums[y])
            y += 1
        for x in range(9, 1, -1):
            nums[y] = int(cnpjv[y])
            nums[y] = nums[y] * x
            calculo_cnpj.append(nums[y])
            y += 1
    calculo_cnpj = 0 + sum(calculo_cnpj)
    if 11 - (calculo_cnpj % 11) < 2:
        digitos.append(0)
    else:
        digitos.append(11 - (calculo_cnpj % 11))
    y = 0
    for x in range(6, 1, -1):
        nums[y] = int(cnpjv[y])
        nums[y] = nums[y] * x
        calculo_cnpj2.append(nums[y])
        y += 1
    for x in range(9, 1, -1):
        nums[y] = int(cnpjv[y])
        nums[y] = nums[y] * x
        calculo_cnpj2.append(nums[y])
        if y == 12:
            break
        y += 1
    calculo_cnpj2 = 0 + sum(calculo_cnpj2)
    if 11 - round(calculo_cnpj2 % 11) < 2:
        digitos.append(0)
    else:
        digitos.append(11 - (calculo_cnpj2 % 11))
    if digitos[0] == int(cnpjv[12]) and digitos[1] == int(cnpjv[13]):
        return True
    else:
        return False


def imprime_cnpj(pass_cnpj):
    if len(pass_cnpj) > 12:
        pass_cnpj = pass_cnpj.split(".")
        pass_cnpj = "".join(pass_cnpj)
        pass_cnpj = pass_cnpj.split("/")
        pass_cnpj = "".join(pass_cnpj)
        pass_cnpj = pass_cnpj.split("-")
        pass_cnpj = "".join(pass_cnpj)
    cnpj1 = pass_cnpj[0:2]
    cnpj2 = pass_cnpj[2:5]
    cnpj3 = pass_cnpj[5:8]
    cnpj4 = pass_cnpj[8:12]
    cnpj5 = pass_cnpj[12:15]
    return f"{cnpj1}.{cnpj2}.{cnpj3}/{cnpj4}-{cnpj5}"
