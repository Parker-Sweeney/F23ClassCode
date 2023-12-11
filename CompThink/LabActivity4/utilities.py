# -*- coding: utf-8 -*-
"""

Parker Sweeney 01389288

Lab Activity 3

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")

def getGender():
    
    df_m = df.loc[(df.sex == 0) & (df.attack == 1)]
    m_heart_attacks = len(df_m)
    
    df_f = df.loc[(df.sex == 1) & (df.attack == 1)]
    f_heart_attacks = len(df_f)
    
    t_heart_attacks = m_heart_attacks + f_heart_attacks
    
    male_percent_notation = "{:,.2f}%".format(m_heart_attacks/t_heart_attacks*100)
    print("Male heart attacks: ", male_percent_notation)
    
    female_percent_notation = "{:,.2f}%".format(f_heart_attacks/t_heart_attacks*100)
    print("Female heart attacks: ", female_percent_notation)
    
    labels = 'Male', 'Female'
    sizes = [m_heart_attacks, f_heart_attacks]
    
    fig1, ax1 = plt.subplots()
    
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    
    # Set Title
    ax1.set_title('Heart Attack Ratio Between Males and Females')
    
    # Show Graphic
    fig1 = plt.gcf()
    plt.show()
    plt.close()
    fig1.savefig('Gender.png')
    
def getExercise():
    
    exang_val_counts = df.groupby("exng")["attack"].value_counts()
    
    exang_heart_attack = (exang_val_counts[1][1] / (exang_val_counts[1][1]+exang_val_counts[1][0]))
    
    no_exang_heart_attack = (exang_val_counts[0][1] / (exang_val_counts[0][1]+exang_val_counts[0][0]))
    
    percent_notation = "{:,.2f}%".format(exang_heart_attack*100)
    print("\nPercent who Exercised and had a heart attack: ", percent_notation)
    
    percent_notation = "{:,.2f}%".format(no_exang_heart_attack*100)
    print("\nPercent who Didn't Exercise and had a heart attack: ", percent_notation)
    
    data = {"Yes":exang_heart_attack*100, "No":no_exang_heart_attack*100}
    
    courses = list(data.keys())
    values = list(data.values())
    
    plt.figure(figsize = (10,5))
    plt.bar(courses, values, color = 'purple', width = 0.7)
    plt.xlabel("Exercise")
    plt.ylabel("Percent Heart Attack")
    plt.title("Percent Heart Attack If Exercising")
    fig1 = plt.gcf()
    
    plt.show()
    plt.close()
    fig1.savefig('Exercise.png')

def getHeart():
    
    heart_attack_percentage = df['attack'].value_counts(normalize=True) * 100
    print("The percent of heart attacks in the data: {:,.2f}%".format(heart_attack_percentage[1]))
    print("The percent of no heart attacks in the data: {:,.2f}%".format(heart_attack_percentage[0]))
    
    plt.figure(figsize = (10,5))
    plt.pie(heart_attack_percentage, labels=['Heart Attack','No Heart Attack'], autopct='%1.2f%%', colors = ['blue', 'orange'])
    plt.title("Heart Attack Ratio in Data")
    plt.savefig('HeartAttack.png')
    # COME BACK TO TO FIX THE ROTATION OF THE CHART TO LOOK LIKE EXAMPLE
    #plt.xticks(rotation=45, ha='right')
    #plt.tight_layout()
    plt.show()
    plt.close()
    
    
def getEKG():
    ekg_percentage = df.groupby('restecg')['attack'].mean() * 100
    ekg_types = {0: 'EKG (Type 0) was normal', 1: 'EKG (Type 1) had an abnormality wiht ST-T Wave', 2: 'EKG (Type 2) had an abnormality in the left ventricular'}
    
    for ekg_type, percentage in zip(ekg_types.keys(), ekg_percentage):
        print("{} and had this percent of heart attacks: {:.2f}%".format(ekg_types[ekg_type], percentage))
    
    plt.figure(figsize = (10,5))
    plt.bar(ekg_types.values(), ekg_percentage, color = 'red', width = 0.5)
    plt.xlabel("EKG Type")
    plt.ylabel("Percent")
    plt.title("Percent Heart Attack With Resting EKG")
    fig1 = plt.gcf()
    
    plt.show()
    plt.close()
    fig1.savefig('EKG.png')
    
