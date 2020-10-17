import random
import csv

with open('Dummy Set for Monogenic Genetic Diseases - Sheet1.csv', 'w', newline='') as csvfile:
    mdata = csv.writer(csvfile, delimiter=',', )
    mfeature = csv.reader(csvfile, delimiter=',', )

    bloodlist = [1, -1, 2, -2, 3, -3, 4, -4]

    for healthy_patient in range(50):
        deoxyhemoglobin = round(random.uniform(0.65, 2.38), 2)
        MCHC = round(random.uniform(33.4, 35.5), 2)
        iron_absorption = round(random.uniform(13.7, 15.1), 2)
        po2 = round(random.uniform(74, 79), 2)
        MCV = round(random.uniform(80, 96), 2)
        Elliptocytosis = round(random.uniform(6, 30), 2)
        schistocytes = round(random.uniform(1, 12), 2)
        hemoglobin = round(random.uniform(13.5, 17.5), 2)
        ESR = round(random.randint(0, 29), 2)
        HB = round(random.randint(20, 22), 2)
        White_bloodcells = round(random.uniform(0.9, 1.2), 2)
        neutrophil = round(random.uniform(42, 76), 2)
        Glomerular_filtration = round(random.uniform(83, 124), 2)
        blood_pressure = round(random.randint(100, 126), 2)
        hyperkalemia = round(random.uniform(3.4, 5.3), 2)
        plasma_renin = round(random.randint(95, 361), 2)
        platelet = random.randint(150, 400)
        troponin_t = round(random.uniform(0, 0.7), 2)
        target_cells = round(random.uniform(5, 20), 2)
        G6PD = round(random.uniform(10, 16), 2)
        blood_type = round(random.choice(bloodlist), 2)
        blood_sugar = round(random.uniform(100, 140), 2)
        methemaglobin = round(random.uniform(3, 14), 2)
        ferric_iron = round(random.randint(22, 338), 2)
        delta_beta = round(random.randint(90, 97), 2)
        hematocrit = round(random.uniform(35, 52), 2)
        classification = '1'


        mdata.writerow([str(deoxyhemoglobin), str(MCHC), str(iron_absorption), str(po2),
                        str(MCV), str(Elliptocytosis), str(schistocytes), str(hemoglobin),
                        str(ESR), str(HB), str(White_bloodcells), str(neutrophil),
                        str(Glomerular_filtration), str(blood_pressure), str(hyperkalemia), str(plasma_renin),
                        str(troponin_t),  str(platelet), str(target_cells), str(G6PD), str(blood_type), str(blood_sugar),
                        str(methemaglobin), str(ferric_iron), str(delta_beta), str(hematocrit),
                        classification])


    for cf_patient in range(50):
        deoxyhemoglobin = round(random.uniform(3.54, 14), 2)
        MCHC = round(random.uniform(2, 28), 2)
        iron_absorption = round(random.uniform(2, 10), 2)
        po2 = round(random.uniform(12, 70), 2)
        MCV = round(random.uniform(74.41, 24), 2)
        Elliptocytosis = round(random.uniform(52, 99), 2)
        schistocytes = round(random.uniform(40, 92), 2)
        hemoglobin = round(random.uniform(0, 9), 2)
        ESR = round(random.randint(40, 79), 2)
        HB = round(random.randint(96, 212), 2)
        White_bloodcells = round(random.uniform(9, 23), 2)
        neutrophil = round(random.uniform(45, 77), 2)
        Glomerular_filtration = round(random.uniform(112, 149), 2)
        blood_pressure = round(random.randint(70, 90), 2)
        hyperkalemia = round(random.uniform(5.8, 36.5), 2)
        plasma_renin = round(random.randint(95, 361), 2)
        platelet = random.randint(497, 595)
        troponin_t = round(random.uniform(1.4, 7.9), 2)
        target_cells = round(random.uniform(35, 64), 2)
        G6PD = round(random.uniform(0, 4.29), 2)
        blood_type = round(random.choice(bloodlist), 2)
        blood_sugar = round(random.uniform(150, 210), 2)
        methemaglobin = round(random.uniform(5, 16), 2)
        ferric_iron = round(random.randint(400, 900), 2)
        delta_beta = round(random.uniform(0, 5.8), 2)
        hematocrit = round(random.uniform(35.5, 48.6), 2)
        classification = '2'

        mdata.writerow([str(deoxyhemoglobin), str(MCHC), str(iron_absorption), str(po2),
                            str(MCV), str(Elliptocytosis), str(schistocytes), str(hemoglobin),
                            str(ESR), str(HB), str(White_bloodcells), str(neutrophil),
                            str(Glomerular_filtration), str(blood_pressure), str(hyperkalemia), str(plasma_renin),
                            str(troponin_t), str(platelet), str(target_cells), str(G6PD), str(blood_type),
                            str(blood_sugar),
                            str(methemaglobin), str(ferric_iron), str(delta_beta), str(hematocrit),
                            classification])




    for glanzmann_patient in range(50):
        deoxyhemoglobin = round(random.uniform(0, 2.38), 2)
        MCHC = round(random.uniform(0, 26.9), 2)
        iron_absorption = round(random.uniform(0, 0.9), 2)
        po2 = round(random.uniform(70, 79), 2)
        MCV = round(random.uniform(74.41, 24), 2)
        Elliptocytosis = round(random.uniform(0, 56), 2)
        schistocytes = round(random.uniform(10, 16), 2)
        hemoglobin = round(random.uniform(0, 9), 2)
        ESR = round(random.randint(15, 32), 2)
        HB = round(random.randint(0, 40), 2)
        White_bloodcells = round(random.uniform(0.9, 1.1), 2)
        neutrophil = round(random.uniform(77, 89), 2)
        Glomerular_filtration = round(random.uniform(90, 120), 2)
        blood_pressure = round(random.randint(100, 127), 2)
        hyperkalemia = round(random.uniform(0.5, 4), 2)
        plasma_renin = round(random.randint(95, 361), 2)
        platelet = random.randint(170, 310)
        troponin_t = round(random.uniform(2, 10.9), 2)
        target_cells = round(random.uniform(35, 64), 2)
        G6PD = round(random.uniform(30, 120), 2)
        blood_type = round(random.choice(bloodlist), 2)
        blood_sugar = round(random.uniform(130, 210), 2)
        methemaglobin = round(random.uniform(5, 16), 2)
        ferric_iron = round(random.randint(0, 200), 2)
        delta_beta = round(random.uniform(10.8, 87), 2)
        hematocrit = round(random.uniform(0.78, 19.4), 2)
        classification = '3'

        mdata.writerow([str(deoxyhemoglobin), str(MCHC), str(iron_absorption), str(po2),
                            str(MCV), str(Elliptocytosis), str(schistocytes), str(hemoglobin),
                            str(ESR), str(HB), str(White_bloodcells), str(neutrophil),
                            str(Glomerular_filtration), str(blood_pressure), str(hyperkalemia), str(plasma_renin),
                            str(troponin_t), str(platelet), str(target_cells), str(G6PD), str(blood_type),
                            str(blood_sugar),
                            str(methemaglobin), str(ferric_iron), str(delta_beta), str(hematocrit),
                            classification])




    for bernar_soulier in range(50):
        deoxyhemoglobin = round(random.uniform(0, 2.38), 2)
        MCHC = round(random.uniform(33.4, 35.5), 2)
        iron_absorption = round(random.uniform(13.7, 15.1), 2)
        po2 = round(random.uniform(70, 79), 2)
        MCV = round(random.uniform(80, 96), 2)
        Elliptocytosis = round(random.uniform(6, 20), 2)
        schistocytes = round(random.uniform(1, 5), 2)
        hemoglobin = round(random.uniform(13.5, 17.5), 2)
        ESR = round(random.randint(0, 29), 2)
        HB = round(random.randint(0, 21), 2)
        White_bloodcells = round(random.uniform(0.9, 1.1), 2)
        neutrophil = round(random.uniform(45, 78), 2)
        Glomerular_filtration = round(random.uniform(90, 120), 2)
        blood_pressure = round(random.randint(100, 127), 2)
        hyperkalemia = round(random.uniform(3.6, 5.2), 2)
        plasma_renin = round(random.randint(95, 361), 2)
        platelet = random.randint(0, 50)
        troponin_t = round(random.uniform(0, 0.4), 2)
        target_cells = round(random.uniform(5, 10), 2)
        G6PD = round(random.uniform(10.15, 14.71), 2)
        blood_type = round(random.choice(bloodlist), 2)
        blood_sugar = round(random.uniform(0, 140), 2)
        methemaglobin = round(random.uniform(0, 3), 2)
        ferric_iron = round(random.randint(24, 336), 2)
        delta_beta = round(random.uniform(87, 97), 2)
        hematocrit = round(random.uniform(36.1, 50.3), 2)
        classification = '4'

        mdata.writerow([str(deoxyhemoglobin), str(MCHC), str(iron_absorption), str(po2),
                            str(MCV), str(Elliptocytosis), str(schistocytes), str(hemoglobin),
                            str(ESR), str(HB), str(White_bloodcells), str(neutrophil),
                            str(Glomerular_filtration), str(blood_pressure), str(hyperkalemia), str(plasma_renin),
                            str(troponin_t), str(platelet), str(target_cells), str(G6PD), str(blood_type),
                            str(blood_sugar),
                            str(methemaglobin), str(ferric_iron), str(delta_beta), str(hematocrit),
                            classification])





    for sickle_cell in range(50):
        deoxyhemoglobin = round(random.uniform(0, 2.38), 2)
        MCHC = round(random.uniform(33.4, 35.5), 2)
        iron_absorption = round(random.uniform(13.7, 15.1), 2)
        po2 = round(random.uniform(0, 63), 2)
        MCV = round(random.uniform(80, 96), 2)
        Elliptocytosis = round(random.uniform(6, 20), 2)
        schistocytes = round(random.uniform(1, 5), 2)
        hemoglobin = round(random.uniform(1, 8.55), 2)
        ESR = round(random.randint(0, 5), 2)
        HB = round(random.randint(0, 21), 2)
        White_bloodcells = round(random.uniform(1.2, 1.6), 2)
        neutrophil = round(random.uniform(64, 81), 2)
        Glomerular_filtration = round(random.uniform(90, 120), 2)
        blood_pressure = round(random.randint(100, 127), 2)
        hyperkalemia = round(random.uniform(3.6, 5.2), 2)
        plasma_renin = round(random.randint(95, 361), 2)
        platelet = random.randint(72, 434)
        troponin_t = round(random.uniform(0, 0.4), 2)
        target_cells = round(random.uniform(5, 10), 2)
        G6PD = round(random.uniform(10.15, 14.71), 2)
        blood_type = round(random.choice(bloodlist), 2)
        blood_sugar = round(random.uniform(0, 140), 2)
        methemaglobin = round(random.uniform(0, 3), 2)
        ferric_iron = round(random.randint(24, 336), 2)
        delta_beta = round(random.uniform(87, 97), 2)
        hematocrit = round(random.uniform(14.3, 25.7), 2)
        classification = '5'

        mdata.writerow([str(deoxyhemoglobin), str(MCHC), str(iron_absorption), str(po2),
                            str(MCV), str(Elliptocytosis), str(schistocytes), str(hemoglobin),
                            str(ESR), str(HB), str(White_bloodcells), str(neutrophil),
                            str(Glomerular_filtration), str(blood_pressure), str(hyperkalemia), str(plasma_renin),
                            str(troponin_t), str(platelet), str(target_cells), str(G6PD), str(blood_type),
                            str(blood_sugar),
                            str(methemaglobin), str(ferric_iron), str(delta_beta), str(hematocrit),
                            classification])