# Listas Usuario Região
nomes_ongs_regiao = []
representantes_ongs_regiao = []
emails_ongs_regiao = []
cnpj_ongs_regiao = []
endereços_ongs_regiao = []
areas_de_atuacao_regiao = []

# Listas Usuario Estado
nomes_ongs_estado = []
representantes_ongs_estado = []
emails_ongs_estado = []
cnpj_ongs_estado = []
endereços_ongs_estado = []
areas_de_atuacao_estado = []

# Regiões
lista_regioes = ['Norte', 'Nordeste']
norte = 4859000
nordeste = 12127000

# Estados
lista_estados = ['Amapá', 'Amapa', 'Pará', 'Para', 'Alagoas', 'Piauí', 'Piaui']
amapa = 281000
para = 2633000
alagoas = 1235000
piaui = 1128000

def regioes():
    print('')
    print('Pessoas com fome: Norte - %1.0f; Nordeste - %1.0f' % (norte, nordeste))
    print('Alimento necessário por dia: Norte - %1.0f Kg; Nordeste - %1.0f Kg' % (norte*3, nordeste*3))
    print('Alimento necessário por mês: Norte - %1.0f Kg; Nordeste - %1.0f Kg' % (norte*90, nordeste*90))
    print('Alimento necessário por ano: Norte - %1.0f Kg; Nordeste - %1.0f Kg' % (norte*1080, nordeste*1080))
    print('')

def estados():
    print('')
    print('Pessoas com fome: Amapá - %1.0f; Pará - %1.0f; Alagoas - %1.0f; Piauí - %1.0f' % (amapa, para, alagoas, piaui))
    print('Alimento necessário por dia: Amapá - %1.0f Kg; Pará - %1.0f Kg; Alagoas - %1.0f Kg; Piauí - %1.0f Kg' % (amapa*3, para*3, alagoas*3, piaui*3))
    print('Alimento necessário por mês: Amapá - %1.0f Kg; Pará - %1.0f Kg; Alagoas - %1.0f Kg; Piauí - %1.0f Kg' % (amapa*90, para*90, alagoas*90, piaui*90))
    print('Alimento necessário por ano: Amapá - %1.0f Kg; Pará - %1.0f Kg; Alagoas - %1.0f Kg; Piauí - %1.0f Kg' % (amapa*1080, para*1080, alagoas*1080, piaui*1080))
    print('')

def opcao_erro():
    print('-'*40)
    print('Opção não encontrada! Tente novamente!')
    print('-'*40)

def tracos():
    print('-'*50)

while True:
    print('--- Menu Principal ---')
    print('')
    print('1 - Nosso projeto')
    print('2 - Cadastre sua ONG')
    print('3 - Análise geral')
    print('4 - Sair do programa')
    print('')
    try:
        menu_principal = int(input('Numero referente: '))
        print('')
        match menu_principal:
            case 1:
                tracos()
                print('Opção Selecionada: Nosso projeto')
                tracos()
                print('')
                print('Nossa solução proposta consiste em um website que servirá como uma plataforma estratégica para guiar e direcionar as ONGs envolvidas na ')
                print('assistência alimentar. O objetivo central é conectar essas organizações aos locais mais necessitados de ajuda alimentar, de forma eficiente e efetiva.')
                print('Através do uso de uma IA generativa direcionada, será possível analisar indicadores socioeconômicos específicos para avaliar o potencial ')
                print('déficit alimentar de uma determinada região, e fornecer os resultados dessas avaliações para agentes responsáveis por atuar na manutenção desse')
                print('problema, visando auxiliar com o problema da fome.')
                print('No website, as ONGs terão acesso a informações atualizadas sobre as regiões e estados que enfrentam as maiores dificuldades alimentares no ')
                print('país. Através de um formulário de inscrição, as organizações poderão fornecer dados relevantes, como sua área de atuação, tipo de ajuda que podem oferecer (como alimentos, água')
                print('etc.) e outras informações importantes para compreender a dimensão da organização. Uma outra funcionalidade do website será também fornecer ')
                print('dados precisos sobre a quantidade de alimento necessária em uma determinada região ou estado, oferecendo uma visão clara da demanda por assistência alimentar.')
                print('Neste programa em Python, buscamos reproduzir como será o funcionamento da IA Generativa, através de códigos de programação e valores pré-')
                print('estabelecidos, de modo a visualizar como vai ser a utilização da versão final do programa e da aplicação WEB.')
                print('')
            case 2:
                tracos()
                print('Opção Selecionada: Cadastre sua ONG')
                tracos()
                print('')
                nome_ong = input('Insira o nome da sua ONG: ')
                representante_ong = input('Insira o nome de algum representante: ')
                email_ong = input('Insira o email de contato da ONG: ')
                cnpj_ong = int(input('Insira o CNPJ da ONG: '))
                endereço_ong = input('Insira qual seria o endereço sede da ONG: ')
                print('')
                while True:
                    print('Aqui estão o locais que precisamos de ajuda:')
                    print('')
                    print('1 - Regional')
                    print('2 - Estadual')
                    print('')
                    try:
                        local_atuacao = int(input('Onde vai querer atuar? (Se quiser cancelar, digite 3) '))
                        print('')
                        if local_atuacao == 1:
                            tracos()
                            print('Opção selecionada: Regional')
                            tracos()
                            print('')
                            print('Aqui está a tabela explicando qual tipo de ajuda precisamos nas regiões: ')
                            regioes()
                            while True:
                                escolha_regiao = input('Digite a região a qual escolheu ajudar: ').lower()
                                print('')
                                if escolha_regiao in [regiao_escolhida.lower() for regiao_escolhida in lista_regioes]:
                                    while True:
                                        ajuda_por_regiao = input('Quer ajudar %s por dia, mês ou anos? ' % escolha_regiao)
                                        print('')
                                        if ajuda_por_regiao == 'dia':
                                            print('Ajuda escolhida por dia!')
                                            print('')
                                            while True:
                                                confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                                                if confirmar_cadastro == 'sim':
                                                    nomes_ongs_regiao.append(nome_ong)
                                                    representantes_ongs_regiao.append(representante_ong)
                                                    emails_ongs_regiao.append(email_ong)
                                                    cnpj_ongs_regiao.append(cnpj_ong)
                                                    endereços_ongs_regiao.append(endereço_ong)
                                                    areas_de_atuacao_regiao.append(escolha_regiao.capitalize())
                                                    print('Cadastro finalizado!')
                                                    print('')
                                                    print('Muito obrigado pela ajuda!')
                                                    print('')
                                                    break
                                                elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                                                    print('Confimação negada!')
                                                    print('')
                                                    print('Obrigado pelo interesse!')
                                                    print('')
                                                    break
                                                else:
                                                    opcao_erro()
                                                    print('')
                                            break
                                        elif ajuda_por_regiao == 'mes' or ajuda_por_regiao == 'mês':
                                            print('Ajuda escolhida por mês!')
                                            print('')
                                            while True:
                                                confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                                                if confirmar_cadastro == 'sim':
                                                    nomes_ongs_regiao.append(nome_ong)
                                                    representantes_ongs_regiao.append(representante_ong)
                                                    emails_ongs_regiao.append(email_ong)
                                                    cnpj_ongs_regiao.append(cnpj_ong)
                                                    endereços_ongs_regiao.append(endereço_ong)
                                                    areas_de_atuacao_regiao.append(escolha_regiao.capitalize())
                                                    print('Cadastro finalizado!')
                                                    print('')
                                                    print('Muito obrigado pela ajuda!')
                                                    print('')
                                                    break
                                                elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                                                    print('Confimação negada!')
                                                    print('')
                                                    print('Obrigado pelo interesse!')
                                                    print('')
                                                    break
                                                else:
                                                    opcao_erro()
                                                    print('')
                                            break
                                        elif ajuda_por_regiao == 'ano':
                                            print('Ajuda escolhida por ano!')
                                            print('')
                                            while True:
                                                confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                                                if confirmar_cadastro == 'sim':
                                                    nomes_ongs_regiao.append(nome_ong)
                                                    representantes_ongs_regiao.append(representante_ong)
                                                    emails_ongs_regiao.append(email_ong)
                                                    cnpj_ongs_regiao.append(cnpj_ong)
                                                    endereços_ongs_regiao.append(endereço_ong)
                                                    areas_de_atuacao_regiao.append(escolha_regiao.capitalize())
                                                    print('Cadastro finalizado!')
                                                    print('')
                                                    print('Muito obrigado pela ajuda!')
                                                    print('')
                                                    break
                                                elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                                                    print('Confimação negada!')
                                                    print('')
                                                    print('Obrigado pelo interesse!')
                                                    print('')
                                                    break
                                                else:
                                                    opcao_erro()
                                                    print('')
                                            break
                                        else:
                                            opcao_erro()
                                    break
                                else:
                                    opcao_erro()
                            break
                        elif local_atuacao == 2:
                            tracos()
                            print('Opção selecionada: Estadual')
                            tracos()
                            print('')
                            print('Aqui está a tabela explicando qual tipo de ajuda precisamos nos estados: ')
                            estados()
                            while True:
                                escolha_estado = input('Digite o estado a qual escolheu ajudar: ').lower()
                                print('')
                                if escolha_estado in [estado_escolhido.lower() for estado_escolhido in lista_estados]:
                                    while True:
                                        ajuda_por_estado = input('Quer ajudar por dia, mês ou anos? ')
                                        print('')
                                        if ajuda_por_estado == 'dia':
                                            print('Ajuda escolhida por dia!')
                                            print('')
                                            while True:
                                                confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                                                if confirmar_cadastro == 'sim':
                                                    nomes_ongs_estado.append(nome_ong)
                                                    representantes_ongs_estado.append(representante_ong)
                                                    emails_ongs_estado.append(email_ong)
                                                    cnpj_ongs_estado.append(cnpj_ong)
                                                    endereços_ongs_estado.append(endereço_ong)
                                                    areas_de_atuacao_estado.append(escolha_estado.capitalize())
                                                    print('Cadastro finalizado!')
                                                    print('')
                                                    print('Muito obrigado pela ajuda!')
                                                    print('')
                                                    break
                                                elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                                                    print('Confimação negada!')
                                                    print('')
                                                    print('Obrigado pelo interesse!')
                                                    print('')
                                                    break
                                                else:
                                                    opcao_erro()
                                                    print('')
                                            break
                                        elif ajuda_por_estado == 'mes' or ajuda_por_regiao == 'mês':
                                            print('Ajuda escolhida por mês!')
                                            print('')
                                            while True:
                                                confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                                                if confirmar_cadastro == 'sim':
                                                    nomes_ongs_estado.append(nome_ong)
                                                    representantes_ongs_estado.append(representante_ong)
                                                    emails_ongs_estado.append(email_ong)
                                                    cnpj_ongs_estado.append(cnpj_ong)
                                                    endereços_ongs_estado.append(endereço_ong)
                                                    areas_de_atuacao_estado.append(escolha_estado.capitalize())
                                                    print('Cadastro finalizado!')
                                                    print('')
                                                    print('Muito obrigado pela ajuda!')
                                                    print('')
                                                    break
                                                elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                                                    print('Confimação negada!')
                                                    print('')
                                                    print('Obrigado pelo interesse!')
                                                    print('')
                                                    break
                                                else:
                                                    opcao_erro()
                                                    print('')
                                            break
                                        elif ajuda_por_estado == 'ano':
                                            print('Ajuda escolhida por ano!')
                                            print('')
                                            while True:
                                                confirmar_cadastro = input('Deseja confirmar o cadastro? (sim/não) ')
                                                if confirmar_cadastro == 'sim':
                                                    nomes_ongs_estado.append(nome_ong)
                                                    representantes_ongs_estado.append(representante_ong)
                                                    emails_ongs_estado.append(email_ong)
                                                    cnpj_ongs_estado.append(cnpj_ong)
                                                    endereços_ongs_estado.append(endereço_ong)
                                                    areas_de_atuacao_estado.append(escolha_estado.capitalize())
                                                    print('Cadastro finalizado!')
                                                    print('')
                                                    print('Muito obrigado pela ajuda!')
                                                    print('')
                                                    break
                                                elif confirmar_cadastro == 'não' or confirmar_cadastro == 'nao':
                                                    print('Confimação negada!')
                                                    print('')
                                                    print('Obrigado pelo interesse!')
                                                    print('')
                                                    break
                                                else:
                                                    opcao_erro()
                                                    print('')
                                            break
                                        else:
                                            opcao_erro()
                                    break
                                else:
                                    opcao_erro()
                            break
                        elif local_atuacao == 3:
                            print('Cadastro cancelado!')
                            break
                        else:
                            opcao_erro()
                    except ValueError:
                        opcao_erro()
            case 3:
                while True:
                    tracos()
                    print('Opção Selecionada: Análise geral')
                    tracos()
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
                                tracos()
                                print('Opção Selecionada: Análise da fome')
                                tracos()
                                regioes()
                                estados()
                            case 2:
                                tracos()
                                print('Opção Selecionada: ONGs cadastradas')
                                tracos()
                                print('')
                                for i, ongs_regiao in enumerate(nomes_ongs_regiao):
                                    print(f'{i+1}. Nome: {ongs_regiao}, Contato: {emails_ongs_regiao[i]}, Área de atuação: {areas_de_atuacao_regiao[i]}')
                                print('')
                                for i, ongs_estado in enumerate(nomes_ongs_estado):
                                    print(f'{i+1}. Nome: {ongs_estado}, Contato: {emails_ongs_estado[i]}, Área de atuação: {areas_de_atuacao_estado[i]}')
                            case 3:
                                tracos()
                                print('Opção Selecionada: Voltar ao menu principal')
                                tracos()
                                print('')
                                print('Voltando ao menu principal...')
                                print('')
                                break
                            case _:
                                opcao_erro()
                                print('')
                    except ValueError:
                        opcao_erro()
                        print('')
            case 4: 
                tracos()
                print('Opção Selecionada: Sair do programa')
                tracos()
                print('')
                print('Finalizando o programa...')
                break
            case _:
                opcao_erro()
    except ValueError:
        opcao_erro() 