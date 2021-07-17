# Verificador-De-CPF
Um verificador de CPF criado em Python
<h1> Olá!</h1>
Sou novato em Python e até mesmo em programação, mas busco melhorar, então se o código tiver algum erro ou alguma imperfeição visível, por favor me mostre.

1° O cpf será passado da classe principal para essa classe, onde ocorrerá todo o processo</br>
========
2° Seria bom se o CPF fosse passado em String ou em Int mesmo, mas o melhor seria sem a máscara, entretanto 
      foi feito um laço de condicional para caso alguém utilize a máscara  de CPF.</br>    
========
3° O programa faz um Cast de String para Int, então não é necessário se preocupar com a chance de dar erro caso seja colocado em String. Pensei em fazer o Cast de String para 
Int para dar a oportunidade de caso o usuário queira seja permitido inserir o CPF com a máscara já inclusa,  não tenha chances de dar erro.</br>
========

4° Foi adicionado um outro módulo para ser feito a verificação de CNPJ</br>
========
Exemplo de código para caso ocorram dúvidas.</br>
from Util import VerifCPF</br>

cpf = input("Informe o cpf")</br>
if verif_cpf(cpf):</br>
    print(f"O CPF {imprime_cpf(cpf) é válido!}")</br>
else:</br>
    print(f"O CPF {imprime_cpf(cpf) é inválido!}")</br>
