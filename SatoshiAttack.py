# To simulate the discovery of blocks it generates random numbers
import random

'''
simulateSatoshiAttack : function to simulate the Satoshi's attack (Double Spending Attack)
z_input_nbConfirmations [IN] : The number of confirmations for the transaction
q_input_relativeHashrateOfAttacker [IN] : The relative hashrate of the attacker
v_input_doubleSpendAmount [IN] : the amount of the double spend 
A_input_maximumAuthorizedDelay [IN] : The maximum delay authorized between the official blockchain and the attacker chain
n_input_nbCycles [IN] :  The number of cycles in the attack
'''

def simulateSatoshiAttack(z_input_nbConfirmations, q_input_relativeHashrateOfAttacker, v_input_doubleSpendAmount,
                          A_input_maximumAuthorizedDelay, n_input_nbCycles):
    # The number of cycles in the attack
    nbCycles = 0
    # The number of cycles won by the attacker
    output_number_of_cycles_won_per_attack = 0
    # This counter represents the duration of the attack
    attackDurationCounter = 1 / q_input_relativeHashrateOfAttacker
    # The total revenue of the attack
    total_revenue_of_attack = 0
    number_of_blocks_mined_in_attack = 0

    # Until we have done all the cycles
    while nbCycles < n_input_nbCycles:

        # The number of cycles in the attack
        nbCycles = nbCycles + 1
        # Represents the number of blocks found by the attacker
        counterAttacker = 0
        # Represents the number of blocks found by the honest miner
        counterHonestMiner = 0

        # ---------------------------------------- PHASE 0 -------------------------------------------------------------

        # The attacker has premined 1 block, we do not simulate this phase

        # ---------------------------------------- PHASE 1 -------------------------------------------------------------

        # At the end of this phase the merchant sends the consumer goods to the attacker
        while True:

            # This counter represents the attack
            attackDurationCounter = attackDurationCounter + 1
            # To simulate the discovery of blocks it generates random numbers
            randomNumber = (random.randint(1, 100)) / 100

            if q_input_relativeHashrateOfAttacker >= randomNumber:
                counterAttacker = counterAttacker + 1
            else:
                counterHonestMiner = counterHonestMiner + 1

            # The delay between the official blockchain and the attacker chain
            delay = counterHonestMiner - counterAttacker

            if counterHonestMiner >= z_input_nbConfirmations or delay >= A_input_maximumAuthorizedDelay + 1:
                break

        # If the attacker has not exceeded or equalized the size of the official blockchain
        if counterAttacker < counterHonestMiner and delay < A_input_maximumAuthorizedDelay:

            # ---------------------------------------- PHASE 2 -------------------------------------------------------------

            # As long as the 2 conditions are fulfilled
            # condition 1 : The delay is smaller than the maximum allowed
            # condition 2 : The counter of the attacker is smaller or equal to that of the honest minors
            # The attacker has already premined 1 block, so we stop when his block number is equal to that of the official blockchain

            while True:

                # This counter represents the duration of the attack
                attackDurationCounter = attackDurationCounter + 1

                # To simulate the discovery of blocks it generates random numbers
                randomNumber = (random.randint(1, 100)) / 100

                if q_input_relativeHashrateOfAttacker >= randomNumber:
                    counterAttacker = counterAttacker + 1
                else:
                    counterHonestMiner = counterHonestMiner + 1

                # The delay between the official blockchain and the attacker chain
                delay = counterHonestMiner - counterAttacker

                if delay >= A_input_maximumAuthorizedDelay + 1 or counterAttacker >= counterHonestMiner:
                    break

        # If the attacker has exceeded the size of the official blockchain
        if counterAttacker >= counterHonestMiner:
            # The number of cycles won by the attacker
            output_number_of_cycles_won_per_attack = output_number_of_cycles_won_per_attack + 1
            # The revenue generated by the blocks mined by the attacker
            revenue_blocks_mined = counterAttacker
            # The attacker's revenue :  (the mined blocks revenue + double spend amount) / the duration of the attack
            total_revenue_of_attack = total_revenue_of_attack + revenue_blocks_mined + v_input_doubleSpendAmount

            number_of_blocks_mined_in_attack = number_of_blocks_mined_in_attack + counterAttacker

    # The attacker revenue ratio, it's the income divided by the duration it takes to get the income
    output_revenueRatioAttacker = total_revenue_of_attack / attackDurationCounter

    output_percentage_cycles_won_per_attack = output_number_of_cycles_won_per_attack / n_input_nbCycles

    output_revenue_per_cycle = total_revenue_of_attack / n_input_nbCycles

    output_number_of_blocks_mined_per_cycle = number_of_blocks_mined_in_attack / n_input_nbCycles

    output_duration_per_cycle = attackDurationCounter / n_input_nbCycles

    # The revenue ratio of the attacker
    return output_revenueRatioAttacker, output_number_of_cycles_won_per_attack, output_percentage_cycles_won_per_attack, output_revenue_per_cycle, output_number_of_blocks_mined_per_cycle, output_duration_per_cycle, attackDurationCounter


def calculateRevenueRatioForListOfHashrates(z_input_nbConfirmations, v_input_doubleSpendAmount,
                                            A_input_maximumAuthorizedDelay, n_input_nbAttacks):
    # List to contains the hashrates
    listHashrates = [0] * 49
    # List to contains the revenues ratio
    listRevenueRatioAttacker = [0] * 49

    list_number_of_cycles_won_per_attack = [0] * 49
    list_percentage_of_cycles_won_per_attack = [0] * 49
    list_revenue_per_cycle = [0] * 49
    list_number_of_blocks_mined_per_cycle = [0] * 49
    list_duration_per_cycle = [0] * 49
    list_duration_per_attack = [0] * 49

    # This loop will run the Satoshi attack for each hashrate, I do +1 (50 instead of 49) because the function range() stop before the last number
    for index in range(1, 50):

        # To generate a Satoshi attack and put the result in the variable
        listRevenueRatioAttacker[index - 1], list_number_of_cycles_won_per_attack[index - 1], list_percentage_of_cycles_won_per_attack[index - 1], list_revenue_per_cycle[index - 1], list_number_of_blocks_mined_per_cycle[index - 1], list_duration_per_cycle[index - 1], list_duration_per_attack[index - 1] = simulateSatoshiAttack(
                                                            z_input_nbConfirmations,
                                                            index / 100,
                                                            v_input_doubleSpendAmount,
                                                            A_input_maximumAuthorizedDelay,
                                                            n_input_nbAttacks)

        # This list contains the hashrates, I do -1 because a array/list starts at zero
        listHashrates[index - 1] = index / 100

    return listRevenueRatioAttacker, listHashrates, list_number_of_cycles_won_per_attack, list_percentage_of_cycles_won_per_attack, list_revenue_per_cycle, list_number_of_blocks_mined_per_cycle, list_duration_per_cycle, list_duration_per_attack