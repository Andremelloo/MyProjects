import time
import RaspagemDadosSitePowerBi
import EnviarMsgWhatsapp


def relatorio_diario():
    time.sleep(1)
    start2.escrever_msg("Boa tarde TIME!!")
    start2.escrever_msg("Está em desenvolvimento...")
    start2.escrever_msg("Segue o relatório de Segunda a Sexta.")
    start2.pular_linha_msg()
    start2.escrever_msg("*METAS* Disponibilidade e Confiabilidade.")
    start2.escrever_msg("Disp. STS   acima de *95%*  Conf. *98,5%*.")
    start2.escrever_msg("Disp. RTG   acima de *90%*  Conf. *97,5%*.")
    start2.escrever_msg("Disp. RS/EV acima de *90%*  Conf. *97%*.")
    start2.escrever_msg("Disp. CT    acima de *95%*  Conf. *99%*.")
    start2.pular_linha_msg()
    start2.escrever_msg("*META MTTR* ")
    start2.escrever_msg("STS/RTG abaixo de *30minutos*.")
    start2.pular_linha_msg()
    start2.escrever_msg("---------------------------------------------------------")
    start2.escrever_msg("Como estamos hoje.!!")
    start2.pular_linha_msg()
    start2.escrever_msg("Disponibilidade e Confiabilidade.")
    start2.escrever_msg("Disp. STS *{}* Conf. *{}*.".format(start1.Disp_PT, start1.Conf_STS))
    start2.escrever_msg("Disp. RTG *{}* Conf.*{}*.".format(start1.Disp_RTG, start1.Conf_RTG))
    start2.escrever_msg("Disp. RS  *{}* Conf. *{}*.".format(start1.Disp_RS, start1.Conf_RS))
    start2.escrever_msg("Disp. EV  *{}* Conf. *{}*.".format(start1.Disp_EV, start1.Conf_EV))
    start2.escrever_msg("Disp. CT  *{}* Conf. *{}*.".format(start1.Disp_CT, start1.Conf_CT))
    start2.escrever_msg("Disp. EPP *{}* Conf. *{}*.".format(start1.Disp_EPP, start1.Conf_EPP))
    start2.escrever_msg("Disp. CF  *{}* Conf. *{}*.".format(start1.Disp_CF, start1.Conf_FC))
    start2.pular_linha_msg()
    start2.escrever_msg("*MTTR*")
    start2.escrever_msg("STS *{}* minutos.".format(start1.MTTR_STS))
    start2.escrever_msg("RTG *{}* minutos.".format(start1.MTTR_RTG))
    start2.pular_linha_msg()
    start2.escrever_msg("Um ótimo trabalho a todos!!")
    start2.escrever_msg("Data Update{}".format(start1.Ultima_Atualizacao_Principal))
    start2.enviar_msg()

def relatorio_diario_custo():
    time.sleep(1)
    start2.escrever_msg("Segue o relatório de custos. Segunda a sexta.")
    start2.pular_linha_msg()
    start2.escrever_msg("Limite por mês, por Família.")
    start2.escrever_msg("*STS* Material - R$  ***** ")
    start2.escrever_msg("*STS* Serviço - R$ *4.500,00*")
    start2.escrever_msg("*RTG* Material - R$ *455.000,00*")
    start2.escrever_msg("*RTG* Serviço - R$ *8.000,00* ")
    start2.escrever_msg("*RS* Material - R$ *139.000,00* ")
    start2.escrever_msg("*RS* Serviço - R$ *8.700,00* ")
    start2.escrever_msg("*EV* Material - R$ *24.000,00* ")
    start2.escrever_msg("*EV* Serviço - R$ *900,00*  ")
    start2.escrever_msg("*TTs* Material - R$ *255.000,00*")
    start2.escrever_msg("*TTs* Serviço - R$ *52.000,00* ")
    start2.escrever_msg("------------------------------------------------------")
    start2.escrever_msg("Gastos atualmente no mês, até hoje.")
    start2.pular_linha_msg()
    start2.escrever_msg("*STS* Em material - R$ *{}* ".format(start1.Custo_STS_Atual))
    start2.escrever_msg("*STS* Em serviço - R$ *{}* ".format(start1.Custo_STS_Serv_Atua))
    start2.escrever_msg("*RTG* Em material - R$ *{}* ".format(start1.Custo_RTG_Atual))
    start2.escrever_msg("*RTG* Em serviço - R$ *{}* ".format(start1.Custo_RTG_Serv_Atua))
    start2.escrever_msg("*RS* Em material - R$ *{}* ".format(start1.Custo_RS_Atual))
    start2.escrever_msg("*RS* Em serviço - R$ *{}* ".format(start1.Custo_RS_Serv_Atua))
    start2.escrever_msg("*EV* Em material - R$ *{}* ".format(start1.Custo_EV_Atual))
    start2.escrever_msg("*EV* Em serviço - R$ *{}* ".format(start1.Custo_EV_Serv_Atua))
    start2.escrever_msg("*TTs* Em material - R$ *{}* ".format(start1.Custo_TT_Atual))
    start2.escrever_msg("*TTs* Em serviço - R$ *{}* ".format(start1.Custo_TT_Serv_Atua))
    start2.pular_linha_msg()
    start2.pular_linha_msg()
    start2.escrever_msg("Total de lançando até hoje - R$ *{}* ".format(start1.Custo_Gasto_Total_mes))
    start2.escrever_msg("Limite pra gastar no mês - R$ *1.407.756,79* ")
    start2.pular_linha_msg()
    start2.escrever_msg("*OBS:* Valores sujeitos à alteração, pode ter algo que precise classificar pra _CAPEX_.")
    start2.escrever_msg("Data Update{}".format(start1.Ultima_Atualizacao_Custo))

    start2.enviar_msg()

## Raspagem de dados no powerBI
start1 = RaspagemDadosSitePowerBi.RaspagemDadosPowerBi()

start1.raspagem_dados_disponibilidade()
start1.raspagem_dados_confibilidade()
start1.raspagem_dados_mttr()
start1.site_custo()
start1.raspagem_dados_custos_fixos()
start1.raspagem_dados_atualizacao()
start1.fechar_browser()

## Entrando no whatsapp e enviando os relatórios.
start2 = EnviarMsgWhatsapp.EnviarMsg()
start2.encontar_contato("melhor manu")
relatorio_diario()
start2.encontar_contato("turno tcp")
relatorio_diario()
start2.encontar_contato("tcp coord")
relatorio_diario_custo()

time.sleep(10)
start2.fechar_msg()


