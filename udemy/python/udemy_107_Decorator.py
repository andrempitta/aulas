"""
Decoradores (Decorator)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators tmabém são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar / Açuar Sintático)

/-----------------------------------------------/
/           Function Decorator                  /
/-----------------------------------------------/


/-----------------------------------------------/
/ / ------------------------------------------/ /
/ /            Função Decorada                / /
/ / ------------------------------------------/ /
/-----------------------------------------------/


OBS: Não confundir Decorator (Decorador) de Decoretion Function (Função Decoradora)

"""
# Decoretors como função (Syntax não recomendada / Sem açucar sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
     print('Seja bem vindo ao MBR')


# Testando 1:

teste = seja_educado(saudacao)
teste()

# Testando 2:

def raiva():
    print('EU TE ODEIO!')

teste2 = seja_educado(raiva)
teste2()

# Decorator com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print()
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro.')

apresentando()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
| -------------------------------------------------------|
|  Home  |   Serviços    |  Produtos  |  Administrativo  |
| -------------------------------------------------------|

https://www.suaempresa.com/br/home
https://www.suaempresa.com/br/servicos
https://www.suaempresa.com/br/produtos
https://www.suaempresa.com/br/admin


def checa_usuario():
    if not request.usuario:
        redirect('https://www.suaempresa.com/br/home')
        
def home(request):
    return 'Pode acessar Home'

def servicos(request):
    return 'Pode acessar Serviços'
    
def produto(request):
    return 'Pode acessar Produtos'
    
@ checa_usuario
def admin(request):
    return 'Pode acessar Adminstrativo'   

"""


