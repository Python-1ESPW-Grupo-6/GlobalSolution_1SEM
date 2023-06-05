# Listas Usuario
nomes_ongs = []
representantes_ongs = []
emails_ongs = []
cnpj_ongs = []
endereços_ongs = []
areas_de_atuacao = []

# Listas Ficticias
ongs_ficticias = []
contato_ficticio = []
areas_de_atuacao_ficticias = []

# Regiões
norte = (4859000)
nordeste = (12127000)

# Estados
amapa = (281000)
para = (2633000)
alagoas = (1235000)
piaui = (1128000)

def regioes():
    #print('Essas são algumas das ONGs que nos ajudam nessas regiões: ')
    print('')
    print('Pessoas com fome: Norte - %1.0f; Nordeste - %1.0f' % norte, nordeste)
    print('Alimento necessário por dia: Norte - %1.0f Kg; Nordeste - %1.0f Kg' % norte*3, nordeste*3)
    print('Alimento necessário por mês: Norte - %1.0f Kg; Nordeste - %1.0f Kg' % norte*90, nordeste*90)
    print('Alimento necessário por ano: Norte - %1.0f Kg; Nordeste - %1.0f Kg' % norte*1080, nordeste*1080)
    print('')

def estados():
    #print('Essas são algumas das ONGs que nos ajudam nesses estados: ')
    print('')
    print('Pessoas com fome: Amapá - %1.0f; Pará - %1.0f; Alagoas - %1.0f; Piauí - %1.0f' % amapa, para, alagoas, piaui)
    print('Alimento necessário por dia: Amapá - %1.0f Kg; Pará - %1.0f Kg; Alagoas - %1.0f Kg; Piauí - %1.0f Kg' % amapa*3, para*3, alagoas*3, piaui*3)
    print('Alimento necessário por mês: Amapá - %1.0f Kg; Pará - %1.0f Kg; Alagoas - %1.0f Kg; Piauí - %1.0f Kg' % amapa*90, para*90, alagoas*90, piaui*90)
    print('Alimento necessário por ano: Amapá - %1.0f Kg; Pará - %1.0f Kg; Alagoas - %1.0f Kg; Piauí - %1.0f Kg' % amapa*1080, para*1080, alagoas*1080, piaui*1080)
    print('')

def opcao_erro():
    print('-'*40)
    print('Opção não encontrada! Tente novamente!')
    print('-'*40)

while True:
    print('Menu Principal')
    print('')
    print('1 - Nosso projeto')
    print('2 - Cadastre sua ONG')
    print('3 - Menu de ajuda')
    print('4 - Análise geral')
    print('5 - Sair do programa')
    print('')
    try:
        menu_principal = int(input('Numero referente: '))
        match menu_principal:
            case 1:
                print('Opção Selecionada: Nosso projeto')
                print('')
                print('Nossa solução proposta consiste em um website que servirá como uma plataforma estratégica para guiar e direcionar as ONGs envolvidas na ')
                print('assistência alimentar. O objetivo central é conectar essas organizações aos locais mais necessitados de ajuda alimentar, de forma eficiente e efetiva.')
                print('Através do uso de uma IA generativa direcionada, será possível analisar indicadores socioeconômicos específicos para avaliar o potencial ')
                print('déficit alimentar de uma determinada região, e fornecer os resultados dessas avaliações para agentes responsáveis por atuar na manutenção desse ')
                print('problema, visando auxiliar com o problema da fome.')
                print('No website, as ONGs terão acesso a informações atualizadas sobre as regiões e estados que enfrentam as maiores dificuldades alimentares no ')
                print('país. Através de um formulário de inscrição, as organizações poderão fornecer dados relevantes, como sua área de atuação, tipo de ajuda que podem oferecer (como alimentos, água')
                print('etc.) e outras informações importantes para compreender a dimensão da organização. Uma outra funcionalidade do website será também fornecer ')
                print('dados precisos sobre a quantidade de alimento necessária em uma determinada região ou estado, oferecendo uma visão clara da demanda por assistência alimentar.')
                print('Neste programa em Python, buscamos reproduzir como será o funcionamento da IA Generativa, através de códigos de programação e valores pré-')
                print('estabelecidos, de modo a visualizar como vai ser a utilização da versão final do programa e da aplicação WEB.')
            case 2:
                print('Opção Selecionada: Cadastre sua ONG')
                print('')
                nome_ong = input('Insira o nome da sua ONG: ')
                representante_ong = input('Insira o nome de algum representante: ')
                email_ong = input('Insira o email de contato da ONG: ')
                cnpj_ong = int(input('Insira o CNPJ da ONG:'))
                endereço_ong = input('Insira qual seria o endereço sede da ONG: ')
                print('')
                print('Antes de confirmar o cadastro, é necessario saber em qual área quer atuar?')
                print('')
                print('Aqui estão o locais que precisamos de ajuda:')
                print('')
                print('Regional')
                regioes()
                print('Estadual')
                estados()
                print('')
                local_atuacao = input('Onde vai querer atuar? ').capitalize()
                print('')
                while True:
                    confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                    if confirmar_cadastro == 'sim':
                        nomes_ongs.append(nome_ong)
                        representantes_ongs.append(representante_ong)
                        emails_ongs.append(email_ong)
                        cnpj_ongs.append(cnpj_ong)
                        endereços_ongs.append(endereço_ong)
                        areas_de_atuacao.append(local_atuacao)
                        print('Cadastro finalizado!')
                        print('')
                        print('Muito obrigado pela ajuda!')
                        break
                    elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                        print('Confimação negada!')
                        print('')
                        print('Obrigado pelo interesse!')
                        break
                    else:
                        opcao_erro()
                        print('')
            case 3:
                print('Opção Selecionada: Menu de ajuda')
                print('')
                print('Esse menu é dedicado a ')
            case 4:
                while True:
                    print('Opção Selecionada: Análise geral')
                    print('')
                    print('1 - Análise da fome')
                    print('2 - ONGs cadastradas')
                    print('3 - Voltar ao menu principal')
                    print('')
                    try:
                        menu_analise = int(input('Número referente: '))
                        print('')
                        match menu_analise:
                            case 1:
                                print('Opção Selecionada: Análise da fome')
                                print('')
                                regioes()
                                print('')
                                estados()
                                print('')
                            case 2:
                                print('Opção Selecionada: ONGs cadastradas')
                                print('')
                                for i, ongs in enumerate(nomes_ongs):
                                    print(f'{i+1}. Nome: {ongs}, Contato: {emails_ongs}, Área de atuação: {areas_de_atuacao}')
                            case 3:
                                print('Opção Selecionada: Voltar ao menu principal')
                                print('')
                                print('Voltando ao menu principal...')
                                break
                            case _:
                                opcao_erro()
                                print('')
                    except ValueError:
                        opcao_erro()
                        print('')
            case 5: #colocar um histórico de acesso
                print('Opção Selecionada: Sair do programa')
                print('')
                print('Finalizando o programa...')
                break
            case _:
                opcao_erro()
    except ValueError:
        opcao_erro()