#### main.py
import csv
import os
import sys
print(os.getcwd())
os.chdir("C:\\Users\\gutie\\Dropbox\\Documentos Insumos\\PREWORK_CGF\\Module-3\\Homework\\PyPoll\\")
sys.stdout = open('output.txt', 'w')
i=0
v=0
j=0
candidatos=[]
votos=[]
pcVotos=[]
vMax=0
with open('election_data.csv','r', newline='') as file:
    electoral=csv.reader(file, delimiter=',')
    print(electoral)
    headers=next(electoral)
    print(f"CSV Header: {headers}")
    for row in electoral:
        i=i+1
        if(row[2] not in candidatos):
            candidatos.append(row[2])
            votos.append(0)
            pcVotos.append(0)
        for k in range(len(candidatos)):
            if(row[2]==candidatos[k]):
                votos[k]=votos[k]+1
                pcVotos[k]=(votos[k]/i)*100

for k in range(len(votos)):
    if votos[k]==max(votos):
        winner=candidatos[k]
        
print("\nElection Results\n-------------------------")
print(f"Total Votes: {i}")
print(f"-------------------------")
for k in range(len(candidatos)):
    print(f"{candidatos[k]}: {pcVotos[k]}% ({votos[k]})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

sys.stdout.close()