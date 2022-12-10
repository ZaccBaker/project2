import string
import csv

def warframe(frame):
    """
    Method to find warframe information
    :param frame: Name of the warframe
    :return: Name and if owned parts associated with warframe
    """
    if frame == '':
        raise ValueError
    with open('files/frames.csv', 'r') as csvfile:
        for line in csvfile:
            if line.startswith(frame):
                info_list = line.split(',')
                for i, a in enumerate(info_list):
                    #Prime & Normal variant test
                    if i == 1 or i == 3:
                        if a == 'o':
                            info_list[i] = 'Not Owned'
                        elif a == 'x':
                            info_list[i] = 'Owned'
                        else:
                            info_list[i] = 'No prime variant'
                    #Prime parts needed
                    if i == 2:
                        if a == '-':
                            info_list[2] = 'No parts'
                    #Mastery
                    if i == 4:
                        if a == 'n\n':
                            info_list[4] = 'Normal'
                        elif a == 'p\n':
                            info_list[4] = 'Prime'
                        elif a == 'b\n':
                            info_list[4] = 'Normal & Prime'
                        else:
                            if a == 'n':
                                info_list[4] = 'Normal'
                            elif a == 'p':
                                info_list[4] = 'Prime'
                            elif a == 'b':
                                info_list[4] = 'Normal & Prime'
                            else:
                                info_list[4] = 'No Mastery'

                        name = ''.join(info_list[0]).capitalize()
                        prime = ''.join(info_list[1])
                        prime_parts = ''.join(info_list[2])
                        normal = ''.join(info_list[3])
                        mastery = ''.join(info_list[4])
                        return name,prime,prime_parts,normal,mastery


def primary(weapon):
    """
    Method to find primary weapon information
    :param weapon: Name of primary weapon
    :return: Name and if owned parts associated with primary weapon
    """
    if weapon == '':
        raise ValueError
    
    name_sep = weapon.split()
    name_length = len(name_sep)

    with open('files/primary.csv', 'r') as csvfile:
        for line in csvfile:
            #Single index primary weapons
            if name_length == 1:
                name = weapon.capitalize()
                if line.startswith(name):
                    info_list = line.split(',')
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery
            #Two index primary weapons
            else:
                name = string.capwords(weapon, sep=None)
                if line.startswith(name):
                    info_list = line.split(',')
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery


def secondary(weapon):
    """
    Method to find secondary weapon information
    :param weapon: Name of secondary weapon
    :return: Name and if owned parts associated with secondary weapon
    """
    if weapon == '':
        raise ValueError

    name_sep = weapon.split()
    name_length = len(name_sep)

    with open('files/secondary.csv', 'r') as csvfile:
        for line in csvfile:
            #Single index secondary weapon
            if name_length == 1:
                name = weapon.capitalize()
                if line.startswith(name):
                    info_list = line.split(',')
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            name = ''.join(info_list[0])
                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery
            #Two index secondary weapon
            if name_length > 1:
                name = string.capwords(weapon, sep=None)
                if line.startswith(name):
                    info_list = line.split(',')
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            name = ''.join(info_list[0])
                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery


def melee(weapon):
    """
    Method to find melee weapon information
    :param weapon: Name of melee weapon
    :return: Name and if owned parts associated with melee weapon
    """
    if weapon == '':
        raise ValueError
    
    name_sep = weapon.split()
    name_length = len(name_sep)

    with open('files/melee.csv', 'r') as csvfile:
        for line in csvfile:
            #Single index secondary weapon
            if name_length == 1:
                name = weapon.capitalize()
                if line.startswith(name):
                    info_list = line.split(',')
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            elif a == '-':
                                info_list[i] = 'No variant'
                            #else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            name = ''.join(info_list[0])
                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery
            #Two index weapon name
            if name_length > 1:
                name = string.capwords(weapon, sep=None)
                if line.startswith(name):
                    info_list = line.split(',')
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            name = ''.join(info_list[0])
                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery
            #Three index weapon name (all have '&' in them)
            if name_length == 3:
                name = weapon.split()
                for i, letter in enumerate(name):
                    if letter != '&':
                        name[i] = letter.capitalize()
                name = string.capwords(weapon, sep=None)
                if line.startswith(name):
                    info_list = line.split(',')
                    info_list[0] = name
                    for i, a in enumerate(info_list):
                        #Prime & Normal variant test
                        if i == 1 or i == 2:
                            if a == 'o':
                                info_list[i] = 'Not Owned'
                            elif a == 'x':
                                info_list[i] = 'Owned'
                            else:
                                info_list[i] = 'No prime variant'
                        #Prime parts needed
                        if i == 3:
                            if a == '-':
                                info_list[3] = 'No parts'
                        #Mastery
                        if i == 4:
                            if a == 'n\n':
                                info_list[4] = 'Normal'
                            elif a == 'p\n':
                                info_list[4] = 'Prime'
                            elif a == 'b\n':
                                info_list[4] = 'Normal & Prime'
                            else:
                                if a == 'n':
                                    info_list[4] = 'Normal'
                                elif a == 'p':
                                    info_list[4] = 'Prime'
                                elif a == 'b':
                                    info_list[4] = 'Normal & Prime'
                                else:
                                    info_list[4] = 'No Mastery'

                            name = ''.join(info_list[0])
                            normal = ''.join(info_list[1])
                            prime = ''.join(info_list[2])
                            prime_parts = ''.join(info_list[3])
                            mastery = ''.join(info_list[4])
                            return name,normal,prime,prime_parts,mastery


def primary_variant(variant,name):
    """
    Method to find primary variant information
    :param variant: Name of variant type
    :param name: Name of the variant weapon
    :return: Name and if owned parts associated with variant weapon
    """
    with open('files/primary_variant.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                info_list = line.split(',')
                for i, a in enumerate(info_list):
                    #Prime & Normal variant test
                    if i == 1:
                        if a == 'o':
                            info_list[i] = 'Not Owned'
                        elif a == 'x':
                            info_list[i] = 'Owned'
                        else:
                            info_list[i] = 'Not available'
                    #Prime parts needed
                    elif i == 2:
                        if a == 'o':
                            info_list[i] = 'Not Mastered'
                        elif a == 'x':
                            info_list[i] = 'Mastered'
                        elif a == '-':
                            info_list[i] = 'Not Mastered'

                        owned = ''.join(info_list[1])
                        mastery = ''.join(info_list[2])
                        return owned,mastery


def secondary_variant(variant,name):
    """
    Method to find secondary variant information
    :param variant: Name of variant type
    :param name: Name of variant weapon
    :return: Name and if owned parts associated with variant weapon
    """
    with open('files/secondary_variant.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                info_list = line.split(',')
                for i, a in enumerate(info_list):
                    #Prime & Normal variant test
                    if i == 1:
                        if a == 'o':
                            info_list[i] = 'Not Owned'
                        elif a == 'x':
                            info_list[i] = 'Owned'
                        else:
                            info_list[i] = 'Not available'
                    #Prime parts needed
                    elif i == 2:
                        if a == 'o':
                            info_list[i] = 'Not Mastered'
                        elif a == 'x':
                            info_list[i] = 'Mastered'
                        elif a == '-':
                            info_list[i] = 'Not Mastered'

                        owned = ''.join(info_list[1])
                        mastery = ''.join(info_list[2])
                        return owned,mastery


def melee_variant(variant,name):
    """
    Method to find melee variant information
    :param variant: Name of variant type
    :param name: Name of variant weapon
    :return: Name and if owned parts associated with variant weapon
    """
    with open('files/melee_variant.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                info_list = line.split(',')
                for i, a in enumerate(info_list):
                    #Prime & Normal variant test
                    if i == 1:
                        if a == 'o':
                            info_list[i] = 'Not Owned'
                        elif a == 'x':
                            info_list[i] = 'Owned'
                        else:
                            info_list[i] = 'Not available'
                    #Prime parts needed
                    elif i == 2:
                        if a == 'o':
                            info_list[i] = 'Not Mastered'
                        elif a == 'x':
                            info_list[i] = 'Mastered'
                        elif a == '-':
                            info_list[i] = 'Not Mastered'

                        owned = ''.join(info_list[1])
                        mastery = ''.join(info_list[2])
                        return owned,mastery


def primary_checkPrime(name):
    """
    Method to check if primary weapon has a prime variant
    :param name: Name of prime primary weapon
    :return: True: Weapon has prime variant, False: Does not have prime variant
    """
    with open('files/primary_primeParts.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                return True
        return False


def secondary_checkPrime(name):
    """
    Method to check if secondary weapon has a prime variant
    :paam name: Name of prime secondary weapon
    :return: True: Weapon has prime variant, False: Does not have prime variant
    """
    with open('files/secondary_primeParts.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                return True
        return False


def melee_checkPrime(name):
    """
    Method to check if melee weapon has a prime variant
    :param name: Name of prime melee weapon
    :return: True: Weapon has prime variant, False: Does not have prime variant
    """
    with open('files/melee_primeParts.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                return True
        return False
    

def primary_parts(name):
    """
    Method to get the total list of primary weapon parts to compare against and their order
    :param name: Name of primary weapon
    :return: Total list of primary parts
    """
    with open('files/primary_primeParts.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                info_list = line.split(',')
                #Remove name & \n
                del info_list[0]
                del info_list[-1]
                return info_list


def secondary_parts(name):
    """
    Method to get the total list of secondary weapon parts to compare against and their order
    :param name: Name of secondary weapon
    :return: Total list of secondary parts
    """
    with open('files/secondary_primeParts.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                info_list = line.split(',')
                #Remove name & \n
                del info_list[0]
                del info_list[-1]
                return info_list


def melee_parts(name):
    """
    Method to get the total list of melee weapon parts to compare against and their order
    :param name: Name of melee weapon
    :return: Total list of melee parts
    """
    with open('files/melee_primeParts.txt', 'r') as file:
        for line in file:
            if line.startswith(name):
                info_list = line.split(',')
                #Remove name & \n
                del info_list[0]
                del info_list[-1]
                return info_list

#Number of parts from player inventory
def secondary_partNum(name):
    """
    Method to get secondary parts from player inventory
    :param name: Name of secondary weapon
    :return: Player secondary parts
    """
    name = name.split(';')
    for i, b in enumerate(name):
        if ':' in b:
            new = b.split(':')
            name[i] = new
    return name

#Number of parts total for secondary prime weapon
def secondary_partNumTotal(name):
    """
    Method to get total number of secondary parts
    :param name: Name of prime secondary weapon
    :return: Total prime parts
    """
    for i, a in enumerate(name):
        if ':' in a:
            new = a.split(':')
            name[i] = new
    return name

#Number of parts from player inventory
def melee_partNum(name):
    """
    Method to get melee parts from player inventory
    :param name: Name of melee weapon
    :return: Player melee parts
    """
    name = name.split(';')
    for i, b in enumerate(name):
        if ':' in b:
            new = b.split(':')
            name[i] = new
    return name

#Number of parts total for secondary prime weapon
def melee_partNumTotal(name):
    """
    Method to get total number of melee parts
    :param name: Name of prime melee weapon
    :return: Total prime parts
    """
    for i, a in enumerate(name):
        if ':' in a:
            new = a.split(':')
            name[i] = new
    return name
