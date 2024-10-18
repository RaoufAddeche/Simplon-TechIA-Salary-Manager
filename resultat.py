import json
#charger les fichiers json
with open("/home/addeche/Documents/Projet_Simplon/Brief_Calcul_des_Salaires_Mensuels/info_salariés.json", "r") as f:
    data = json.load(f)


#fonction pour calculer le salaire mensuel

def calcul_des_salaires_mensuels(employe):
    
     #calcul salaire hebdo
     salaire_hebdo = employe["hourly_rate"] * employe["weekly_hours_worked"]
     
     #si heures sup
     if employe["weekly_hours_worked"] > employe["contract_hours"]:
        calcul_SalaireBonus = ((employe["weekly_hours_worked"] - employe["contract_hours"]) * (employe["hourly_rate"]) *1.5)
        salaire_hebdo = employe["hourly_rate"] * employe["contract_hours"] + calcul_SalaireBonus
    
          
     #calcul salaire mensuel (4,33=Moyenne de semaines dans un mois)
     salaire_mensuel = salaire_hebdo * 4.33
     return salaire_mensuel


# Afficher le salaire de chaque employé dans la filiale au choix en forme dictionnaire

entreprise = {}


for filiales, employes in data.items():
    entreprise [filiales] = []
    for employe in employes:
        dictio_employés= {
          "name":employe['name'],
          "job": employe['job'],
          "salaire mensuel": calcul_des_salaires_mensuels(employe)}
        
        entreprise [filiales].append(dictio_employés)



#fonction pour calculer les statistiques

def calcul_des_stats(entreprise):

    statistiques= {}

    for filiales, employes in entreprise.items():
        salaires = [employe['salaire mensuel'] for employe in employes]
        if salaires:
            statistiques[filiales]= {'salaire moyen': sum(salaires) / len(salaires),
                              'salaire max': max(salaires),
                              'salaire minimum': min(salaires)}
    return statistiques

statistiques = calcul_des_stats(entreprise)




# Afficher le salaire de chaque employé dans la filiale au choix en forme f'string
print('\nEntreprise : Techcorp\n')
for employe in entreprise['TechCorp']:
    print(f"{employe['name']:<20} | {employe['job']:<20} | Salaire mensuel: {employe['salaire mensuel']:.2f} €")

print ("\n=========================================================\n")
print('Statistiques des salaires pour l\'entreprise TechCorp:')
print(f"Salaire moyen :{statistiques['TechCorp']["salaire moyen"]:.2f}€")
print(f"Salaire maximum : {statistiques['TechCorp']['salaire max']:.2f}€")
print(f'Salaire minimum : {statistiques['TechCorp']['salaire minimum']:.2f}€')
print ("\n=========================================================\n")

print('\nEntreprise : ProjectLead\n')
for employe in entreprise['ProjectLead']:
    print(f"{employe['name']:<20} | {employe['job']:<20} | Salaire mensuel: {employe['salaire mensuel']:.2f} €")





print ("\n=========================================================\n")
print('Statistiques des salaires pour l\'entreprise ProjectLead:')
print(f"Salaire moyen :{statistiques['ProjectLead']["salaire moyen"]:.2f}€")
print(f"Salaire maximum : {statistiques['ProjectLead']['salaire max']:.2f}€")
print(f'Salaire minimum : {statistiques['ProjectLead']['salaire minimum']:.2f}€')
print ("\n=========================================================\n")


print('\nEntreprise : DesignWorks\n')
for employe in entreprise['DesignWorks']:
    print(f"{employe['name']:<20} | {employe['job']:<20} | Salaire mensuel: {employe['salaire mensuel']:.2f} €")

print ("\n=========================================================\n")
print('Statistiques des salaires pour l\'entreprise DesignWorks:')
print(f"Salaire moyen :{statistiques['DesignWorks']["salaire moyen"]:.2f}€")
print(f"Salaire maximum : {statistiques['DesignWorks']['salaire max']:.2f}€")
print(f'Salaire minimum : {statistiques['DesignWorks']['salaire minimum']:.2f}€')
print ("\n=========================================================\n")
