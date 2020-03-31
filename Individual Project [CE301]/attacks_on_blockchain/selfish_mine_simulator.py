# code here is based on theories discussed in
# "Majority is not Enough: Bitcoin Mining is Vulnerable" - Ittay Eyal and Emin Gun Sirer
# and also "Blockchain Mining Games" - Aggelos Kiayias, Elias Koutsoupias, Maria kyropoulou and Yiannis Tselekounis

import random
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


class Mine:

    # initialises the variables i will be using for the selfish mine simulator. These variables will be parsed in an object oriented fashion
    def __init__(self, selfish_chain, honest_chain, selfish_orphan, honest_orphan, selfish_block, honest_block):
        self.selfish_chain = selfish_chain  # length of selfish miner chain
        self.honest_chain = honest_chain  # length of honest miner chain
        self.selfish_orphan = selfish_orphan  # number of blocks lost for selfish chain
        self.honest_orphan = honest_orphan  # number of blocks lost for honest chain
        self.selfish_block = selfish_block  # number of blocks mined for selfish miner
        self.honest_block = honest_block  # number of blocks mined for honest miner

        # self.pool = 0
        # self.count = 0
        # self.total_mined_block = 0


def strategy1(alpha, gamma, simulations):
    chain = Mine(0, 0, 0, 0, 0, 0)  # initalising all chain/orphan/blocks to 0

    for i in range(1, simulations):
        # for loop with be iterated through n number of simulations, which is defined in the main
        if random.uniform(0, 1) <= alpha:
            # if random int value between 0,1 is less than equal to alpha

            if chain.selfish_chain > 0 and chain.selfish_chain == chain.honest_chain:
                chain.selfish_chain += 1  # state is 1
                chain.selfish_block += chain.selfish_chain  # selfish block mined is added onto the selfish chain
                chain.honest_orphan += chain.honest_chain  # honest block is added to the orphan as that isn't the longest chain
                chain.honest_chain, chain.selfish_chain = 0, 0
                # in this case we assume that the selfish miner doesnt publish the block

            else:
                chain.selfish_chain += 1
                # selfish miner doesnt publish the block

        else:  # in this instance the honest miners get a block

            if chain.selfish_chain == 0:
                chain.honest_chain += 1
                chain.honest_block += chain.honest_chain
                chain.honest_chain = 0

            elif chain.selfish_chain == chain.honest_chain and random.uniform(0, 1) < float(gamma):
                # where gamma = ratio of honest miners who mine on the selfish chain
                chain.selfish_block += chain.selfish_chain
                chain.honest_orphan += chain.honest_chain
                chain.honest_block += 1
                chain.selfish_chain, chain.honest_chain = 0, 0
            # elif chain.selfish_mine_chain == chain.honest_mine_chain and random.uniform(0, 1) >= float(gamma):

            else:
                # append block onto the selfish chain
                chain.honest_chain += 1

                if chain.selfish_chain == chain.honest_chain + 1:
                    # honest miners gains are orphaned since selfish miner chain is the longest
                    chain.selfish_block += chain.selfish_chain
                    chain.honest_orphan += chain.honest_chain
                    chain.selfish_chain, chain.honest_chain = 0, 0

                if chain.honest_chain > chain.selfish_chain:
                    # selfish miners gains are orphaned since honest miner chain is the longest
                    chain.honest_block += chain.honest_chain
                    chain.selfish_orphan += chain.selfish_chain
                    chain.honest_chain, chain.selfish_chain = 0, 0

    return chain


# what happens if selfish miner keeps mining, instead of abandoning their branch once 1 block behind honest miner

def strategy2(alpha, gamma, simulations):
    chain2 = Mine(0, 0, 0, 0, 0, 0)

    for i in range(1, simulations):
        if random.uniform(0, 1) <= alpha:
            # if random int value between 0,1 is less than equal to alpha
            if chain2.selfish_chain > 0 and chain2.selfish_chain == chain2.honest_chain:
                chain2.selfish_chain += 1  # state is 1
                chain2.selfish_block += chain2.selfish_chain  # selfish block mined is added onto the selfish chain
                chain2.honest_orphan += chain2.honest_chain  # honest block is added to the orphan as that isn't the longest chain
                chain2.honest_chain, chain2.selfish_chain = 0, 0
                # in this case we assume that the selfish miner doesnt publish the block

            else:
                chain2.selfish_chain += 1
                # selfish miner doesnt publish the block

        else:  # in this instance the honest miners get a block

            if chain2.selfish_chain == 0:
                chain2.honest_chain += 1
                chain2.honest_block += chain2.honest_chain
                chain2.honest_chain = 0

            elif chain2.selfish_chain == chain2.honest_chain and random.uniform(0, 1) < float(gamma):
                # where gamma = ratio of honest miners who mine on the selfish chain
                chain2.selfish_block += chain2.selfish_chain
                chain2.honest_orphan += chain2.honest_chain
                chain2.honest_block += 1
                chain2.selfish_chain, chain2.honest_chain = 0, 0

            else:
                # append block onto the selfish chain
                chain2.honest_chain += 1

                """
                THIS IS THE SELFISH MINER STRATEGY
                """

                if chain2.honest_chain > chain2.selfish_chain:

                    chain2.honest_block += chain2.honest_chain
                    # now honest miner is 2 blocks ahead...

                    if random.uniform(0, 1) <= alpha:
                        # if random int value between 0,1 is less than equal to alpha

                        if chain2.selfish_chain > 0 and chain2.selfish_chain == chain2.honest_chain:
                            chain2.selfish_chain += 1  # state is 1
                            chain2.selfish_block += chain2.selfish_chain  # selfish block mined is added onto the selfish chain
                            chain2.honest_orphan += chain2.honest_chain  # honest block is added to the orphan as that isn't the longest chain
                            chain2.honest_chain, chain2.selfish_chain = 0, 0
                            # in this case we assume that the selfish miner doesnt publish the block

                        else:
                            chain2.selfish_chain += 1
                            # selfish miner doesnt publish the block

                    else:  # in this instance the honest miners get a block

                        if chain2.selfish_chain == 0:
                            chain2.honest_chain += 1
                            chain2.honest_block += chain2.honest_chain
                            chain2.honest_chain = 0

                        elif chain2.selfish_chain == chain2.honest_chain and random.uniform(0, 1) < float(gamma):
                            # where gamma = ratio of honest miners who mine on the selfish chain
                            chain2.selfish_block += chain2.selfish_chain
                            chain2.honest_orphan += chain2.honest_chain
                            chain2.honest_block += 1
                            chain2.selfish_chain, chain2.honest_chain = 0, 0
                        # elif chain.selfish_mine_chain == chain.honest_mine_chain and random.uniform(0, 1) >= float(gamma):

                        else:
                            # append block onto the selfish chain
                            chain2.honest_chain += 1

                            if chain2.selfish_chain == chain2.honest_chain + 1:
                                # honest miners gains are orphaned since selfish miner chain is the longest
                                chain2.selfish_block += chain2.selfish_chain
                                chain2.honest_orphan += chain2.honest_chain
                                chain2.selfish_chain, chain2.honest_chain = 0, 0

                            if chain2.honest_chain > chain2.selfish_chain:
                                # selfish miners gains are orphaned since honest miner chain is the longest
                                chain2.honest_block += chain2.honest_chain
                                chain2.selfish_orphan += chain2.selfish_chain
                                chain2.honest_chain, chain2.selfish_chain = 0, 0

    return chain2


def strategy3(alpha, gamma, simulations):

    chain3 = Mine(0, 0, 0, 0, 0, 0)  # initalising all chain/orphan/blocks to 0

    for i in range(1, simulations):
        # for loop with be iterated through n number of simulations, which is defined in the main
        if random.uniform(0, 1) <= alpha:
            # if random int value between 0,1 is less than equal to alpha

            if chain3.selfish_chain > 0 and chain3.selfish_chain == chain3.honest_chain:
                chain3.selfish_chain += 1  # state is 1
                chain3.selfish_block += chain3.selfish_chain  # selfish block mined is added onto the selfish chain
                chain3.honest_orphan += chain3.honest_chain  # honest block is added to the orphan as that isn't the longest chain
                chain3.honest_chain, chain3.selfish_chain = 0, 0
                # in this case we assume that the selfish miner doesnt publish the block

            else:
                chain3.selfish_chain += 1
                # selfish miner doesnt publish the block
                "maybe logic here changes to see when selfish miner > 2 and publish when 3 blocks ahead"

        else:  # in this instance the honest miners get a block

            if chain3.selfish_chain == 0:
                chain3.honest_chain += 1
                chain3.honest_block += chain3.honest_chain
                chain3.honest_chain = 0

            elif chain3.selfish_chain == chain3.honest_chain and random.uniform(0, 1) < float(gamma):
                # where gamma = ratio of honest miners who mine on the selfish chain
                chain3.selfish_block += chain3.selfish_chain
                chain3.honest_orphan += chain3.honest_chain
                chain3.honest_block += 1
                chain3.selfish_chain, chain3.honest_chain = 0, 0
            # elif chain.selfish_mine_chain == chain.honest_mine_chain and random.uniform(0, 1) >= float(gamma):
            if chain3.selfish_chain == 3:
                chain3.selfish_block += chain3.selfish_chain  # selfish block mined is added onto the selfish chain
                chain3.honest_orphan += chain3.honest_chain  # honest block is added to the orphan as that isn't the longest chain
                chain3.honest_chain, chain3.selfish_chain = 0, 0

            else:
                # append block onto the selfish chain
                chain3.honest_chain += 1

                if chain3.selfish_chain == chain3.honest_chain + 1:
                    # honest miners gains are orphaned since selfish miner chain is the longest, publishing the blocks and adopting the selfish chain
                    #print("test chain length", chain3.selfish_chain)
                    chain3.selfish_block += chain3.selfish_chain
                    chain3.honest_orphan += chain3.honest_chain
                    chain3.selfish_chain, chain3.honest_chain = 0, 0

                if chain3.honest_chain > chain3.selfish_chain:
                    # selfish miners gains are orphaned since honest miner chain is the longest
                    chain3.honest_block += chain3.honest_chain
                    chain3.selfish_orphan += chain3.selfish_chain
                    chain3.honest_chain, chain3.selfish_chain = 0, 0



    return chain3


def write_chain1(simulations, alpha, gamma, chain):
    chain_results = [simulations, alpha, gamma,
                     ((alpha * (1 - alpha) ** 2 * (4 * alpha + gamma * (1 - 2 * alpha)) - alpha ** 3) / (
                             1 - alpha * (1 + (2 - alpha) * alpha))),
                     chain.selfish_block / float(chain.selfish_block + chain.honest_block),
                     chain.selfish_block, chain.honest_block, chain.selfish_orphan, chain.honest_orphan,
                     (chain.selfish_block / float(chain.selfish_block / chain.honest_block)),
                     int(chain.selfish_block - chain.honest_block),
                     100 * round(chain.selfish_block / (chain.selfish_block + chain.honest_block), 3)]
    with open('results.csv', 'a', encoding='utf-8') as lines:
        lines.write(', '.join([str(x) for x in chain_results]) + '\n')
#test git commit

def write_chain2(simulations, alpha, gamma, chain2):
    chain_results2 = [simulations, alpha, gamma,
                      ((alpha * (1 - alpha) ** 2 * (4 * alpha + gamma * (1 - 2 * alpha)) - alpha ** 3) / (
                              1 - alpha * (1 + (2 - alpha) * alpha))),
                      chain2.selfish_block / float(chain2.selfish_block + chain2.honest_block),
                      chain2.selfish_block, chain2.honest_block, chain2.selfish_orphan, chain2.honest_orphan,
                      (chain2.selfish_block / float(chain2.selfish_block / chain2.honest_block)),
                      int(chain2.selfish_block - chain2.honest_block),
                      100 * round(chain2.selfish_block / (chain2.selfish_block + chain2.honest_block), 3)]
    with open('results2.csv', 'a', encoding='utf-8') as lines:
        lines.write(', '.join([str(x) for x in chain_results2]) + '\n')

def write_chain3(simulations, alpha, gamma, chain3):
    chain_results3 = [simulations, alpha, gamma,
                      ((alpha * (1 - alpha) ** 2 * (4 * alpha + gamma * (1 - 2 * alpha)) - alpha ** 3) / (
                              1 - alpha * (1 + (2 - alpha) * alpha))),
                      chain3.selfish_block / float(chain3.selfish_block + chain3.honest_block),
                      chain3.selfish_block, chain3.honest_block, chain3.selfish_orphan, chain3.honest_orphan,
                      (chain3.selfish_block / float(chain3.selfish_block / chain3.honest_block)),
                      int(chain3.selfish_block - chain3.honest_block),
                      100 * round(chain3.selfish_block / (chain3.selfish_block + chain3.honest_block), 3)]
    with open('results3.csv', 'a', encoding='utf-8') as lines:
        lines.write(', '.join([str(x) for x in chain_results3]) + '\n')


def plot():
    df = pd.read_csv('results.csv')
    df2 = pd.read_csv('results2.csv')
    df3 = pd.read_csv('results3.csv')
    df.head()
    df2.head()
    df3.head()
    print(df)
    print(df2)
    print(df3)
    # x should show alpha values from 0-0.5
    # y should show revenue ratio for selfish miners

    figure1 = px.scatter(df, x=' α_Mining Power', y=' r_Revenue ratio for Selfish Miners',
                         title='Simulated Revenue Ratio - Ittays Selfish Mining Strategy',
                         color=' γ_Ratio of honest miners who choose to mine on the pools block')
    figure2 = px.scatter(df2, x=' α_Mining Power', y=' r_Revenue ratio for Selfish Miners',
                         title='Simulated Revenue Ratio - Selfish Miner Attempts To Mine at 2 Block Deficit',
                         color=' γ_Ratio of honest miners who choose to mine on the pools block')
    figure1.show()
    figure2.show()

    figure7 = px.scatter(df3, x=' α_Mining Power', y=' r_Revenue ratio for Selfish Miners',
                         title='Simulated Revenue Ratio - Selfish Miners Always Publish their Chain When 3 Blocks Ahead',
                         color=' γ_Ratio of honest miners who choose to mine on the pools block')

    figure7.show()

def plot_orphans():
    df_strat = pd.read_csv('results.csv')
    df_alternate_strat = pd.read_csv('results2.csv')
    df_third_strat = pd.read_csv('results3.csv')
    df_strat.head()
    df_alternate_strat.head()
    df_third_strat.head()
    print(df_strat)
    print(df_alternate_strat)

    # graphs showing number of selfish miners blocks orphaned by the honest miners chain
    figure3 = px.scatter(df_strat, x=' s_Selfish Orphan Blocks Count', y=' r_Revenue ratio for Selfish Miners',
                         title='Number of Selfish Miners Blocks Orphaned - Ittays Selfish Mining Strategy',
                         color=' α_Mining Power')
    figure3.show()
    figure4 = px.scatter(df_alternate_strat, x=' s_Selfish Orphan Blocks Count',
                         y=' r_Revenue ratio for Selfish Miners',
                         title='Number of Selfish Miners Blocks Orphaned - Selfish Miner Attempts To Mine at 2 Block Deficit',
                         color=' α_Mining Power')
    figure4.show()

    figure8 = px.scatter(df_third_strat, x=' s_Selfish Orphan Blocks Count',
                         y=' r_Revenue ratio for Selfish Miners',
                         title='Simulated Revenue Ratio - Selfish Miners Always Publish their Chain When 3 Blocks Ahead',
                         color=' α_Mining Power')
    figure8.show()


def plot_blocks():
    df_strat = pd.read_csv('results.csv')
    df_alternate_strat = pd.read_csv('results2.csv')
    df_third_strat = pd.read_csv('results3.csv')
    df_strat.head()
    df_alternate_strat.head()
    df_third_strat.head()

    # do honest chain - the selfish chain total to get the length of the total chain
    # as the length of the chain increases, so does the revenue earned
    figure5 = px.scatter(df_strat, x=' α_Mining Power', y=' l_Length of Chain',
                         title='Length of the Longest Chain Proportional to α_Alpha  (Selfish Blocks - Honest Blocks)',
                         color=' γ_Ratio of honest miners who choose to mine on the pools block')
    figure5.show()
    figure6 = px.scatter(df_alternate_strat, x=' α_Mining Power', y=' l_Length of Chain',
                         title='Length of the Longest Chain Proportional to α_Alpha (Selfish Blocks - Honest Blocks) - Selfish Miner Attempts To Mine at 2 Block Deficit',
                         color=' γ_Ratio of honest miners who choose to mine on the pools block')
    figure6.show()
    figure7 = px.scatter(df_alternate_strat, x=' α_Mining Power', y=' l_Length of Chain',
                         title='Length of the Longest Chain Proportional to α_Alpha (Selfish Blocks - Honest Blocks) - Selfish Miners Always Publish their Chain When 3 Blocks Ahead',
                         color=' γ_Ratio of honest miners who choose to mine on the pools block')
    figure7.show()


def main():
    simulations = 200000
    # computational resources for selfish miners
    # ratio of honest miners who chose to mine on selfish pool
    #global chain3, chain2, chain, gamma, simulations


    """
    need to automate alpha/gamma so that:
    x number of simulations ran at alpha = 0.01, gamma from 0.01-0.5
    x number of simulations ran at alpha = 0.02, gamma from 0.01-0.5
    etc
    """

    alpha = 0.50
    temp_gamma = np.longdouble(0.00)
    count = 0

    for i in range(0, 50):
        # print(i)
        temp_gamma += 1
        gamma = float(temp_gamma / 100)
        count = count + 1
        print(gamma)
        # print(count)

        # calls the functions and runs with parameters defined in the main
        chain = strategy1(alpha, gamma, simulations)
        chain2 = strategy2(alpha, gamma, simulations)
        chain3 = strategy3(alpha, gamma, simulations)

        # calls the writing to csv functions with parementers defined in the main
        write_chain1(simulations, alpha, gamma, chain)
        write_chain2(simulations, alpha, gamma, chain2)
        write_chain3(simulations, alpha, gamma, chain3)

    # plots the data
    plot()
    plot_orphans()
    plot_blocks()

    print("\n")
    print("Selfish Miner Strategy 1")
    print(
        "\n Number of Simulations | %d \n α (Alpha) | %f (Selfish miner hash power) \n γ (Gamma) | %f (Proportion of honest miners which mine on the selfish pool)" % (
        simulations, alpha, gamma))
    print("Theoretical probability of selfish miner hashing power | ", (
                (alpha * (1 - alpha) ** 2 * (4 * alpha + gamma * (1 - 2 * alpha)) - alpha ** 3) / (
                    1 - alpha * (1 + (2 - alpha) * alpha))))
    #print("Simulated probability of selfish miner hashing power | ",
          #chain.selfish_block / float(chain.selfish_block + chain.honest_block))
    print("Number of Selfish Blocks Mined | ", chain.selfish_block)
    print("Number of Honest Blocks Mined | ", chain.honest_block)
    # print("Selfish Blocks Mined / Honest Blocks Mined | ", chain.selfish_block / float(chain.selfish_block / chain.honest_block))
    print("Number of Selfish Orphan Blocks | ", chain.selfish_orphan)
    print("Number of Honest Orphan Blocks | ", chain.honest_orphan)
    print("Difficulty (%) ", float(chain.honest_block + chain.selfish_block) / simulations * 100)
    print("Profitability | ", 100 * round(chain.selfish_block / (chain.selfish_block + chain.honest_block), 3))

    print("\n")
    print("\n")
    print("\n")

    print("Selfish Miner Strategy 2 \n")
    print("Number of Selfish Blocks Mined | ", chain2.selfish_block)
    print("Number of Honest Blocks Mined | ", chain2.honest_block)
    print("Selfish Blocks Mined / Honest Blocks Mined | ",
          chain2.selfish_block / float(chain2.selfish_block / chain2.honest_block))
    print("Number of Selfish Orphan Blocks | ", chain2.selfish_orphan)
    print("Number of Honest Orphan Blocks | ", chain2.honest_orphan)
    print("Difficulty (%) ", float(chain2.honest_block + chain2.selfish_block) / simulations * 100)
    print("Profitability | ", 100 * round(chain2.selfish_block / (chain2.selfish_block + chain2.honest_block), 3))

    print("\n")
    print("\n")
    print("\n")

    print("Selfish Miner Strategy 3 \n")
    print("Number of Selfish Blocks Mined | ", chain3.selfish_block)
    print("Number of Honest Blocks Mined | ", chain3.honest_block)
    print("Selfish Blocks Mined / Honest Blocks Mined | ",
          chain3.selfish_block / float(chain3.selfish_block / chain3.honest_block))
    print("Number of Selfish Orphan Blocks | ", chain3.selfish_orphan)
    print("Number of Honest Orphan Blocks | ", chain3.honest_orphan)
    print("Difficulty (%) ", float(chain3.honest_block + chain3.selfish_block) / simulations * 100)
    print("Profitability | ", 100 * round(chain3.selfish_block / (chain3.selfish_block + chain3.honest_block), 3))

main()
