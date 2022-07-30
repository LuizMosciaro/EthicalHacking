import subprocess
import re

#Esse código encontra todas redes que o computador ja conectou
#e devolve uma lista com os valores coletados
cmdOutput = subprocess.run(args='netsh wlan show profile',capture_output=True).stdout.decode(errors='ignore')
pattern = ':(.*)\r'
profileNames = re.findall(pattern=pattern,string=cmdOutput)

listPassword = []
if len(profileNames) != 0:
    for info in profileNames:
        dictPassword = {}
        profileInfo = subprocess.run(args=f'netsh wlan show profile "{info.strip()}" key=clear',capture_output=True).stdout.decode(errors='ignore')
        if info:
            passWordPt = re.findall('da Chave            : (.*)\r',profileInfo)
            dictPassword['WiFi'] = info
            dictPassword['Password'] = passWordPt[0]
            listPassword.append(dictPassword)

            if not passWordPt:
                passWordEnglish = re.findall('Key Content            : (.*)\r',profileInfo)
                dictPassword['WiFi'] = info
                dictPassword['Password'] = passWordPt[0]
            

for i in range(len(listPassword)):
    print(listPassword[i])