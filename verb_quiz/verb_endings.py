import conjugate

'''
to add:
	- mi verb endings
	- optative
'''

#1st pp
pres_act_ind = ['ω', 'εις', 'ει', 'ομεν', 'ετε', 'ουσι(ν)']
pres_act_ind_epsilon_contract = ['ῶ', 'εῖς', 'εῖ', 'οῦμεν', 'εῖτε', 'οῦσι(ν)']
pres_act_ind_alpha_contract = ['ῶ', 'ᾷς', 'ᾷ', 'ῶμεν', 'ᾶτε', 'ῶσι(ν)']
pres_act_ind_omicron_contract = ['ῶ', 'οῖς', 'οῖ', 'οῦμεν', 'οῦτε', 'οῦσι(ν)']

pres_mp_ind = ['ομαι', 'ῃ', 'εται', 'όμεθα', 'εσθε', 'ονται']
pres_mp_ind_epsilon_contract = ['οῦμαι', 'ῇ', 'εῖται', 'ούμεθα', 'εῖσθε', 'οῦνται']
pres_mp_ind_alpha_contract = ['ῶμαι', 'ᾷ', 'ᾶται', 'ώμεθα', 'ᾶσθε', 'ῶνται']
pres_mp_ind_omicron_contract = ['οῦμαι', 'οῖ', 'οῦται', 'ούμεθα', 'οῦσθε', 'οῦνται']

impf_act_ind = ['ον', 'ες', 'ε(ν)', 'ομεν', 'ετε', 'ον']
impf_act_ind_epsilon_contract = ['οῦν', 'εις', 'ει', 'οῦμεν', 'εῖτε', 'ουν']
impf_act_ind_alpha_contract = ['ων', 'ας', 'α', 'ῶμεν', 'ᾶτε', 'ων']
impf_act_ind_omicron_contract = ['ουν', 'ους', 'ου', 'οῦμεν', 'οῦτε', 'ουν']

impf_mp_ind = ['όμην','ου','ετο','όμεθα','εσθε','οντο']
impf_mp_ind_epsilon_contract = ['ούμην','οῦ','εῖτο','ούμεθα','εῖσθε','οῦντο']
impf_mp_ind_alpha_contract = ['ώμην','ῶ','ᾶτο','ώμεθα','ᾶσθε','ῶντο']
impf_mp_ind_omicron_contract = ['ούμην','οῦ','οῦτο','ούμεθα','οῦσθε','οῦντο']

#2nd pp
fut_act_ind = ['ω', 'εις', 'ει', 'ομεν', 'ετε', 'ουσι(ν)']
fut_act_ind_contract = ['ῶ', 'εῖς', 'εῖ', 'οῦμεν', 'εῖτε', 'οῦσι(ν)']
fut_mid_ind = ['ομαι', 'ῃ', 'εται', 'όμεθα', 'εσθε', 'ονται']
fut_mid_ind_contract = ['οῦμαι', 'ῇ', 'εῖται', 'ούμεθα', 'εῖσθε', 'οῦνται']

#3rd pp
aor2_act_ind = ['ον', 'ες', 'ε(ν)', 'ομεν', 'ετε', 'ον']
aor2_mid_ind = ['όμην','ου','ετο','όμεθα','εσθε','οντο']
aor2_ath = ['ν', 'ς', '', 'μεν', 'τε', 'σαν']

aor1_act_ind = ['α', 'ας', 'ε(ν)', 'αμεν', 'ατε', 'αν']
aor1_mid_ind = ['άμην','ω','ατο','άμεθα','ασθε','αντο']

#4th pp
pf_act_ind = ['α', 'ας', 'ε(ν)', 'αμεν', 'ατε', 'ασι(ν)']

plupf_act_ind = ['η', 'ης', 'ει(ν)', 'εμεν', 'ετε', 'εσαν']

#5th pp
pf_mp_ind = ['μαι', 'σαι', 'ται', 'μεθα', 'σθε', 'νται']
pf_mp_ind_labial = ['μμαι', 'ψαι', 'πται', 'μμεθα', 'φθε', '(part + εἰσι(ν))']
pf_mp_ind_palatal = ['γμαι', 'ξαι', 'κται', 'γμεθα', 'χθε', '(part + εἰσι(ν))']
pf_mp_ind_dental = ['σμαι', 'σαι', 'σται', 'σμεθα', 'σθε', '(part + εἰσι(ν))']

plupf_mp_ind = ['μην', 'σο', 'το', 'μεθα', 'σθε', 'ντο']
plupf_mp_ind_labial = ['μμην', 'ψο', 'πτο', 'μμεθα', 'φθε', '(part + ἦσαν)']
plupf_mp_ind_palatal = ['γμην', 'ξο', 'κτο', 'γμεθα', 'χθε', '(part + ἦσαν)']
plupf_mp_ind_dental = ['σμην', 'σο', 'στο', 'σμεθα', 'σθε', '(part + ἦσαν)']

#6th pp
aor_pass_ind = ['ην', 'ης', 'η', 'ημεν', 'ητε', 'ησαν']
fut_pass_ind = ['ήσομαι', 'ήσῃ/ήσει', 'ήσεται', 'ησόμεθα', 'ήσεσθε', 'ήσονται']

#subj
act_subj = ['ω', 'ῃς', 'ῃ', 'ωμεν', 'ητε', 'ωσι(ν)']
mp_subj = ['ωμαι', 'ῃ', 'ηται', 'ώμεθα', 'ησθε', 'ωνται']

#opt
pres_act_opt = ['οιμι', 'οις', 'οι', 'οιμεν', 'οιτε', 'οιεν']
pres_act_opt_epsilon_contract = ['οίην', 'οίης', 'οίη', 'οῖμεν', 'οῖτε', 'οῖεν']
pres_act_opt_epsilon_alt = ['οῖμι', 'οῖς', 'οῖ', 'οίημεν', 'οίητε', 'οίησαν']
pres_act_opt_alpha_contract = ['ῴην', 'ῴης', 'ῷη', 'ῷμεν', 'ῷτε', 'ῷεν']
pres_act_opt_alpha_alt = ['ῷμι', 'ῷς', 'ῷ', 'ῴημεν', 'ῴητε', 'ῷησαν']
pres_act_opt_omicron_contract = ['οίην', 'οίης', 'οίη', 'οῖμεν', 'οῖτε', 'οῖεν']
pres_act_opt_omicron_alt = ['οῖμι', 'οῖς', 'οῖ', 'οίημεν', 'οίητε', 'οίησαν']

pres_mp_opt = ['οίμην', 'οιο', 'οιτο', 'οίμεθα', 'οισθε', 'οιντο']
pres_mp_opt_epsilon_contract = ['οίμην', 'οῖο', 'οῖτο', 'οίμεθα', 'οῖσθε', 'οῖντο']
pres_mp_opt_alpha_contract = ['ῴμην', 'ῷο', 'ῷτο', 'ῴμεθα', 'ῷσθε', 'ῷντο']
pres_mp_opt_omicron_contract = ['οίμην', 'οῖο', 'οῖτο', 'οίμεθα', 'οῖσθε', 'οῖντο']

aor1_act_opt = ['αιμι', 'αις/ειας', 'αι/ειε', 'αιμεν', 'αιτε', 'αιεν/ειαν']
aor1_mid_opt = ['αίμην', 'αιο', 'αιτο', 'αίμεθα', 'αισθε', 'αιντο']

aor2_act_opt = ['οιμι', 'οις', 'οι', 'οιμεν', 'οιτε', 'οιεν']
aor2_mid_opt = ['οίμην', 'οιο', 'οιτο', 'οίμεθα', 'οισθε', 'οιντο']

#imp
pres_act_imp = ['ε', 'έτω', 'ετε', 'όντων']
pres_act_imp_epsilon = ['ει', 'είτω', 'εῖτε', 'ούντων']
pres_act_imp_alpha = ['α', 'άτω', 'ᾶτε', 'ώντων']
pres_act_imp_omicron = ['ου', 'ούτω', 'οῦτε', 'ούντων']

pres_mp_imp = ['ου', 'έσθω', 'εσθε', 'έσθων']
pres_mp_imp_epsilon = ['οῦ', 'είσθω', 'εῖσθε', 'είσθων']
pres_mp_imp_alpha = ['ῶ', 'άσθω', 'ᾶσθε', 'άσθων']
pres_mp_imp_omicron = ['οῦ', 'ούσθω', 'οῦσθε', 'ούσθων']

aor1_act_imp = ['ον', 'άτω', 'ατε', 'άντων']
aor1_mid_imp = ['αι', 'άσθω', 'ασθε', 'άσθων']

aor2_act_imp = ['ε', 'έτω', 'ετε', 'όντων']
aor2_mid_imp = ['οῦ', 'έσθω', 'εσθε', 'έσθων']

#mi-verbs


'''
stem and ending list pairs

needed paradigms:
	- pres act ind, pres mp ind
	- impf act ind, impf mp ind
	- fut act ind, fut mid ind
	- aor(1/2) act ind, aor(1/2) mid ind
	- pf act ind, plupf act ind
	- pf mp ind, plupf mp ind
	- aor pass ind, fut pass ind

	- pres act subj, pres mp subj
	- pres act opt, pres mp opt
	- aor act subj
'''

ἄγω = [
	('ἀγ', pres_act_ind),
	('ἀγ', pres_mp_ind),
	('ἠγ', impf_act_ind),
	('ἠγ', impf_mp_ind),
	('ἀξ', fut_act_ind),
	('ἀξ', fut_mid_ind),
	('ἠγαγ', aor2_act_ind),
	('ἠγαγ', aor2_mid_ind),
	('ἠχ', pf_act_ind),
	('ἠχ', plupf_act_ind),
	('ἠ', pf_mp_ind_palatal),
	('ἠ', plupf_mp_ind_palatal),
	('ἠχθ', aor_pass_ind),
	('ἀχθ', fut_pass_ind)
]

βαίνω = [
	('βαιν', pres_act_ind),
	('ἐβαιν', impf_act_ind),
	('βησ', fut_mid_ind),
	('ἐβη', aor2_ath),
	('βεβηκ', pf_act_ind),
	('ἐβεβηκ', plupf_act_ind)
]

βάλλω = [
	('βαλλ', pres_act_ind),
	('βαλλ', pres_mp_ind),
	('ἐβαλλ', impf_act_ind),
	('ἐβαλλ', impf_mp_ind),
	('βαλ', fut_act_ind_contract),
	('βαλ', fut_mid_ind_contract),
	('ἐβαλ', aor2_act_ind),
	('ἐβαλ', aor2_mid_ind),
	('βεβληκ', pf_act_ind),
	('ἐβεβληκ', plupf_act_ind),
	('βεβλη', pf_mp_ind),
	('ἐβεβλη', plupf_mp_ind),
	('ἐβληθ', aor_pass_ind),
	('βληθ', fut_pass_ind)
]



print(conjugate.full_conjugate(ἄγω))
print(conjugate.full_conjugate(βαίνω))
print(conjugate.full_conjugate(βάλλω))
