
import pandas as pd

#need to change anno.res_index_label == 1.1 to isnull and notnull
def trip_mod(df):
    trimod = df[(df["anno.res_index_label"] >= 0.75) &(df['anno.res_index_label'] < 1.1) & (df["63x_call"] == "63x go")]
    return trimod

def dub_mod(df):
    dubmod = df[(((df["anno.res_index_label"] >= 0.75) & (df['anno.res_index_label'] < 1.1) & (df["63x_call"] == "63x no go")) | ((df["anno.res_index_label"] >=0.75) & (df["anno.res_index_label"] < 1.1) & (df["anno.rna_amp_pass_fail_label"] == "Fail")))]
    return dubmod

def morph_pend(df):
    morphpend = df[((df["anno.res_index_label"] >= 0.75) & (df["anno.rna_amp_pass_fail_label"] == "Pass")) & (df['anno.res_index_label'] < 1.1) & (df["63x_call"] == "No look")]
    return morphpend

def single_mod(df):
    singlemod = df[(df["anno.res_index_label"] < 0.75)]
    return singlemod

def trans_pend(df):
    transpend = df[(df["anno.res_index_label"] == 1.1)]
    return transpend


def reclassify(df):
    tri = trip_mod(df)
    tri['modality class'] = 'Triple Modality'
    dub = dub_mod(df)
    dub['modality class'] = 'Double Modality'
    morph_p = morph_pend(df)
    morph_p['modality class'] = 'Pending Morph'
    single = single_mod(df)
    single['modality class'] = 'EPhys Only'
    trans_p = trans_pend(df)
    trans_p['modality class'] = 'Pending Trans'
    return tri, dub, morph_p, single, trans_p


def concat_df(a, b, c, d, e):
    frames = (a, b, c, d, e)
    df = pd.concat(frames)
    return df


def modality_reclass(df):
    return concat_df(*reclassify(df))

