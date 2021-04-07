'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''
# import dna_tools as dna 
import random
import dna_tools as dna
import patient
'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''

# intro
print("============================================")
print("DNA Analyzer and Patient Management Tool")
print("============================================")
while True:
    try:
        dna.display_menu()
        inputed_option = int(input("Command (Enter to exit) "))
        # task 1
        if inputed_option == 1:
            dna.list_all_patient()
            dna.display_menu
        # task 2
        elif inputed_option == 2:
            dna.info()
            dna.display_menu
        # task 3
        elif inputed_option == 3:
            print(dna.remove_patient())
        # task 4
        elif inputed_option == 4:
            print(dna.insert_new_Patient())
        # task 5
        elif inputed_option == 5: 
            comp = dna.compare()
            print("\n"+comp['Statment'] + "\n"+ comp['Simler'] )
        # task 6
        elif inputed_option == 6:
            dna.compare_all()
        # task 7
        elif inputed_option == 7:
            print(dna.find_pattern())
        else:
            raise Exception("Invalied command")
    except ValueError as err:
        if err:
            print("Thanks for using this tool \n Come back soon!")
            exit()
    except Exception as err2:
        if err2:
            print(err2)
            