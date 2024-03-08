# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    give_bmi.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hchaguer <hchaguer@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/08 23:19:53 by hchaguer          #+#    #+#              #
#    Updated: 2024/03/08 23:48:52 by hchaguer         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def give_bmi(height: list[float], weight: list[float]) -> list[float]:

    # formulat BMI = weight / height power of 2

    BMI = []
    for i in range(len(height) and len(weight)):
        BMI.append(weight[i] / (height[i] * height[i]))
    return BMI

def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    
    etat = []
    
    for i in range(len(bmi)):
        if bmi[i] >= limit:
            etat.append(True)
        else:
            etat.append(False)
    return etat
    
    
    

def main():
    
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()

    
    