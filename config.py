##
#   This file is used fr the configurations of each data rate.
#   The protocols in terms of TCP and UDP are defined as an array.
#   The 802.11 standards are defined as nested dictionaries where the "standards" dictionary's keys are the standards themselves
#   followed by their Data Rates, the data of each individual data rate, their MAC Header, SIFS, Preamble, Max Nss and Max NChan
##



#FIXME perhaps look at changing the dictionaries to
# 802.11a :{ 54: { Nbits : 1, Crate : 2 etc etc
#The protocols to choose from
protocol = ["TCP", "UDP"]
#Data is in the format of NBits, CRate, NChan, SDur, Nss
standards = {
    "802.11a": {
        "Data Rates": [54, 48, 36, 24, 18, 12, 9, 6],
        "Data Rate's Data": [[6, 3 / 4, 48, 4, 1],
                              [6, 2 / 3, 48, 4, 1],
                              [4, 3 / 4, 48, 4, 1],
                              [4, 1 / 2, 48, 4, 1],
                              [2, 3 / 4, 48, 4, 1],
                              [2, 1 / 2, 48, 4, 1],
                              [1, 3 / 4, 48, 4, 1],
                              [1, 1 / 2, 48, 4, 1]],
        "MAC Header": 34,
        "SIFS": 16,
        "Preamble": [20]
    },
    "802.11g": {
        "Data Rates": [54, 48, 36, 24, 18, 12, 9, 6],
        "Data Rate's Data": [[6, 3 / 4, 48, 4, 1],
                              [6, 2 / 3, 48, 4, 1],
                              [4, 3 / 4, 48, 4, 1],
                              [4, 1 / 2, 48, 4, 1],
                              [2, 3 / 4, 48, 4, 1],
                              [2, 1 / 2, 48, 4, 1],
                              [1, 3 / 4, 48, 4, 1],
                              [1, 1 / 2, 48, 4, 1]],
        "MAC Header": 34,
        "SIFS": 10,
        "Preamble": [20]
    },
    "802.11n":{
        "Data Rates": [72.2, 65, 57.8, 43.3, 28.9, 21.7, 14.4, 7.2],
        "Data Rate's Data": [[6, 5 / 6, 52, 3.6, 1],
                            [6, 3 / 4, 52, 3.6, 1],
                            [6, 2 / 3, 52, 3.6, 1],
                            [4, 3 / 4, 52, 3.6, 1],
                            [4, 1 / 2, 52, 3.6, 1],
                            [2, 3 / 4, 52, 3.6, 1],
                            [2, 1 / 2, 52, 3.6, 1],
                            [1, 1 / 2, 52, 3.6, 1]],
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 108,
        "Max Nss": 4,
        "Preamble": [20, 46]
    },
    "802.11ac_w1" : {
        "Data Rates": [ 96.3, 86.7, 72.2, 65, 57.8, 43.3, 28.9, 21.7, 14.4, 7.2],
        "Data Rate's Data": [[8, 5 / 6, 52, 3.6, 1],
                            [8, 3 / 4, 52, 3.6, 1],
                            [6, 5 / 6, 52, 3.6, 1],
                            [6, 3 / 4, 52, 3.6, 1],
                            [6, 2 / 3, 52, 3.6, 1],
                            [4, 3 / 4, 52, 3.6, 1],
                            [4, 1 / 2, 52, 3.6, 1],
                            [2, 3 / 4, 52, 3.6, 1],
                            [2, 1 / 2, 52, 3.6, 1],
                            [1, 1 / 2, 52, 3.6, 1]],
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 234,
        "Max Nss": 3,
        "Preamble": [20, 56.8]
    },

    "802.11ac_w2": {
        "Data Rates": [96.3, 86.7, 72.2, 65, 57.8, 43.3, 28.9, 21.7,
                       14.4, 7.2],
        "Data Rate's Data": [[8, 5 / 6, 52, 3.6, 1],
                            [8, 3 / 4, 52, 3.6, 1],
                            [6, 5 / 6, 52, 3.6, 1],
                            [6, 3 / 4, 52, 3.6, 1],
                            [6, 2 / 3, 52, 3.6, 1],
                            [4, 3 / 4, 52, 3.6, 1],
                            [4, 1 / 2, 52, 3.6, 1],
                            [2, 3 / 4, 52, 3.6, 1],
                            [2, 1 / 2, 52, 3.6, 1],
                            [1, 1 / 2, 52, 3.6, 1]],
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 468,
        "Max Nss": 8,
        "Preamble": [20, 92.8]
    },

    "802.11ax": {
        "Data Rates": [143.4, 129, 114.7, 103.2, 86.0, 77.4, 68.8, 51.6, 34.4, 25.8, 17.2, 8.6],
        "Data Rate's Data": [[10, 5 / 6, 234, 13.6, 1],
                             [10, 3 / 4, 234, 13.6, 1],
                             [8, 5 / 6, 234, 13.6, 1],
                             [8, 3 / 4, 234, 13.6, 1],
                             [6, 5 / 6, 234, 13.6, 1],
                             [6, 3 / 4, 234, 13.6, 1],
                             [6, 2 / 3, 234, 13.6, 1],
                             [4, 3 / 4, 234, 13.6, 1],
                             [4, 1 / 2, 234, 13.6, 1],
                             [2, 3 / 4, 234, 13.6, 1],
                             [2, 1 / 2, 234, 13.6, 1],
                             [1, 1 / 2, 234, 13.6, 1]],
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 1960,
        "Max Nss": 8,
        "Preamble": [20, 92.8]
    }
}
