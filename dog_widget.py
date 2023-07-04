import streamlit as st
import math

def get_result_prob(n_wolf):
    if (n_wolf > 3) or (n_wolf < 0):
        raise Exception("That cannot work")
    # yeah, should use cases here, but I'm too lazy to learn atm
    if n_wolf == 3: #www
        return {'bb':0, 'bw':0, 'ww':1}        
    elif n_wolf == 2: #bww
        return {'bb':0, 'bw':1/3., 'ww':2/3.}    
    elif n_wolf == 1: #bbw
        return {'bb':1/3., 'bw':2/3., 'ww':0}        
    elif n_wolf == 0: #bbb
        return {'bb':1, 'bw':0, 'ww':0}


def get_comb_chance(n_players, n_wolf, n_dog_w, n_dog=3):
    # derive number of civilians from other numbers    
    n_civ = n_players-n_wolf
    # derive number of civilians in dog result from other numbers
    n_dog_c = n_dog-n_dog_w
    # compute number of combinations that contain n_dog_w
    n_comb_w = math.comb(n_wolf, n_dog_w)
    # compute number of combinations that contain n_dog_c
    n_comb_c = math.comb(n_civ, n_dog_c)
    # compute total number of combinations
    n_comb_t = math.comb(n_players, n_dog)
    # compute chance of set for dog claim
    return (n_comb_w*n_comb_c)/n_comb_t


def get_chance_dog_result(n_players, n_wolf):
    # Compute the chance of dog results given number of players and wolves.
    # I'm quite sure this can be done better, but this seems to work.
    if (n_wolf > n_players):
        raise Exception("That's no fun")
    p_nwolf_in_comb = {i: get_comb_chance(n_players, n_wolf, i) for i in range(4)}
    out = {'bb':0, 'bw': 0, 'ww': 0}
    for n, p in p_nwolf_in_comb.items(): 
        for res,p_res in get_result_prob(n).items():            
            out[res] += p_res*p
    return out
                          

st.title('Dorpsgekkie')

n_players = st.slider('Aantal spelers', min_value=1, max_value=50, value=12)
n_wolf = st.slider('Aantal wolven', min_value=1, max_value=n_players, value=1)

res = get_chance_dog_result(n_players, n_wolf)

st.markdown(f"""
DoG uitslagen bij willekeurige keuze:
* BB: {int(math.round(100*res['bb']))}%
* BW: {int(math.round(100*res['bw']))}%
* WW: {int(math.round(100*res['ww']))}%
""")





