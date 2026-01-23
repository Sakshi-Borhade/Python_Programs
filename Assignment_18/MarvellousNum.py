def ChkPrime(Numbers):

    iSum = 0

    for No in Numbers:

        if(No > 1):

            for i in range(2,No):

                if(No % i == 0):

                    break

                else : 

                    iSum = iSum + No

    return iSum