import sys
import time
import RaspagemDadosMTBF
import EnviarMsgWhatsapp


def relatorio_MTBF():
    time.sleep(1)
    start2.escrever_msg("Boa tarde TIME!!")
    start2.escrever_msg("Está em desenvolvimento...")
    start2.escrever_msg("Segue o relatório de Segunda/terça/Sexta.")
    start2.pular_linha_msg()
    start2.escrever_msg("Hrs de trab. / Qtds de falhas")
    start2.escrever_msg("MTBF. STS acima de *70.00* ideal.")
    start2.escrever_msg("MTBF. RTG acima de *40.00* ideal.")
    start2.escrever_msg("MTBF. CT  acima de *100.00* ideal.")
    start2.escrever_msg("MTBF. RS  acima de *70.00* ideal.")
    start2.escrever_msg("MTBF. EV  acima de *70.00* ideal.")
    start2.escrever_msg("-------------------------------------------------------")
    start2.pular_linha_msg()
    start2.escrever_msg("*MTBF* como está hoje.")
    start2.escrever_msg("MTBF. STS  *{}* MTBF.".format(start1.MTBF_PT))
    start2.escrever_msg("MTBF. RTG *{}* MTBF.".format(start1.MTBF_RTG))
    start2.escrever_msg("MTBF. CT  *{}* MTBF.".format(start1.MTBF_CT))
    start2.escrever_msg("MTBF. RS  *{}* MTBF.".format(start1.MTBF_RS))
    start2.escrever_msg("MTBF. EV  *{}* MTBF.".format(start1.MTBF_EV))
    start2.escrever_msg("-------------------------------------------------------")
    start2.pular_linha_msg()
    start2.escrever_msg("Quantidade de falhas por Família, do inicio do mês até hoje!")
    start2.escrever_msg("*STS* = Com *{}* Falhas.".format(start1.Qtde_Falhas_STS))
    start2.escrever_msg("*RTG* = Com *{}* Falhas.".format(start1.Qtde_Falhas_RTG))
    start2.escrever_msg("*RS* = Com *{}* Falhas.".format(start1.Qtde_Falhas_RS))
    start2.escrever_msg("*EV* = Com *{}* Falhas.".format(start1.Qtde_Falhas_EV))
    start2.escrever_msg("*CT* = Com *{}* Falhas.".format(start1.Qtde_Falhas_CT))
    start2.pular_linha_msg()
    start2.pular_linha_msg()
    start2.escrever_msg("*Obs:* Contando com erros operacionais!!")
    start2.escrever_msg("Data Update {}".format(start1.Ultima_Atualizacao))
    
    start2.enviar_msg()


start1 = RaspagemDadosMTBF.RaspagemDadosMTBF()

start1.raspagem_dados_MTBF()
start1.raspagem_dados_qtdade_falhas()
start1.raspagem_dados_atualizacao()

start1.fechar_browser()

start2 = EnviarMsgWhatsapp.EnviarMsg()
start2.encontar_contato("melhor manu")
relatorio_MTBF()

start2.encontar_contato("turno tcp")
relatorio_MTBF()

start2.encontar_contato("tcp coord")
relatorio_MTBF()


time.sleep(10)
start2.fechar_msg()

sys.exit()