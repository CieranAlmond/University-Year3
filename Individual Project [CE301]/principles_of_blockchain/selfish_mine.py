# code here is based on theories discussed in
# "Majority is not Enough: Bitcoin Mining is Vulnerable" - Ittay Eyal and Emin Gun Sirer
# and also "Blockchain Mining Games" - Aggelos Kiayias, Elias Koutsoupias, Maria kyropoulou and Yiannis Tselekounis

import random
import time
import sys

class pool:
    def __init__(self, selfishmine, honestmine, selfishorphan, honestorphan, selfishblock, honestblock):
        self.selfishmine = selfishmine
        self.honestmine = honestmine
        self.selfishorphan = selfishorphan
        self.honestorphan = honestorphan
        self.selfishblock = selfishblock
        self.honestblock = honestblock
# This function will be used to simulate the stra tegy of selfish mining based off Markov principle

def Mine(alpha, gamma, q):
    # define delta value as selfish miners lead on honest miners?
    state = 0
    privatechain = 0
    publicchain = 0
    # def Mine will return the number of blocks in the chain "longest chain" that belong to the miners using the selfish mining strategy

    # iterate through a loop
    # check state 0
    # if the value of random<=alpha, where alpha represents the percentage of overall computing power the selfish miner has = 0.35
    # if r<=alpha change state to 1
    # alpha has to be between values 0-0.5, since more means you have majority control of network..

    # else increment public chain since honest miners found the block..
    # state will remain 0
    for i in range(q):
        r = random.random()
        if state == 0:
            # initial state - selfish miners have 0 blocks in their private tree
            if r <= alpha:
                state = 1
                #P.selfishmine +=1
                # selfish miner finds a block but doesnt publish
            else:
                # honest miners find a block, and is published to chain
                publicchain += 1
                state = 0

                # can use concept of honest miner, selfish miner in selfish_mine_simulator ...

        elif state == 1:
            # in this state, there is 1 selfish block lead to the selfish miners
            if r <= alpha:
                # selfish miners gain another block to their private tree which also isn't published. bringing total to 2
                state = 2
                n = 2
            else:
                state = -1
        elif state == -1:
            # in state -1 the honest miners found a block, creating a fork of length 1
            if r <= alpha:
                # selfish miner found a block in their fork
                privatechain += 1
                publicchain += 2
                state = 0

                # as discussed with maria, this formula needs to be changed as it is inaccurate.
                """elif r <= alpha + (1 - alpha) * gamma:
                    privatechain += 1
                    publicchain += 2
                    state = 0
                    """
            #here if r is less than gamma, ie honest minor ratio, we will increase the private chain
            elif privatechain > 0 and r<= float(gamma):
                    privatechain += 1
                    state = 0

            elif privatechain > 0 and r >= float(gamma):
                    publicchain += 2
                    state = 0
            #above elifs are changed to resolve incorrect maths

            else:
                privatechain += 0
                publicchain += 2
                state = 0

        elif state == 2:
            # back to where selfish miners have two blocks
            if r <= alpha:
                # selfish miners gain another block
                n += 1
                state = 3
            else:
                # honest miner find another block
                #this forces selfish miners to publish their block since they are within length n-1 of honest miners
                # selfish miners publish n blocks
                publicchain += n
                privatechain += n
                state = 0
        elif state >= 2:
            if r <= alpha:
                # selfish miners find another block
                n += 1
                state += 1
            else:
                # honest miners find a block, meaning selfish miners are behind by 1 block. This results in no pay and a waste of time for that chain
                state -= 1

    return float(privatechain) / publicchain


def main():
    alpha = 0.33
    gamma = 0.3
    n = 10 ** 7 #nb simulators
    simulations = 100
    print("\n Iterationations | %d \n α (Alpha) | %f (Selfish miner hash power) \n γ (Gamma) | %f (Proportion of honest miners which mine on the selfish pool)" % (
            simulations, alpha, gamma))

    print("Theoretical probability of selfish miner hash power | ",
          (alpha * (1 - alpha) ** 2 * (4 * alpha + gamma * (1 - 2 * alpha)) - alpha ** 3) / (
                  1 - alpha * (1 + (2 - alpha) * alpha)))
    print("Simulated probability of selifsh miner hash power | ", Mine(alpha, gamma, n))

main()




