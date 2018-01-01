'''
needed paradigms:
	- pres act ind, pres mp ind
	- impf act ind, impf mp ind
	- fut act ind, fut mid ind
	- aor(1/2) act ind, aor(1/2) mid ind
	- pf act ind, plupf act ind
	- pf mp ind, plupf mp ind
	- aor pass ind, fut pass ind
'''

pres_act_ind = ['ω', 'εις', 'ει', 'ομεν', 'ετε', 'ουσι(ν)']
pres_act_ind_epsilon_contract = ['ῶ', 'εῖς', 'εῖ', 'οῦμεν', 'εῖτε', 'οῦσι(ν)']
pres_act_ind_alpha_contract = ['ῶ', 'ᾷς', 'ᾷ', 'ῶμεν', 'ᾶτε', 'ῶσι(ν)']
pres_act_ind_omicron_contract = ['ῶ', 'οῖς', 'οῖ', 'οῦμεν', 'οῦτε', 'οῦσι(ν)']

pres_mp_ind = ['ομαι', 'ῃ', 'εται', 'όμεθα', 'εσθε', 'ονται']
pres_mp_ind_epsilon_contract = ['οῦμαι', 'ῇ', 'εῖται', 'ούμεθα', 'εῖσθε', 'οῦνται']
pres_mp_ind_alpha_contract = ['ῶμαι', 'ᾷ', 'ᾶται', 'ώμεθα', 'ᾶσθε', 'ῶνται']
pres_mp_ind_omicron_contract = ['οῦμαι', 'οῖ', 'οῦται', 'ούμεθα', 'οῦσθε', 'οῦνται']

fut_act_ind = ['ω', 'εις', 'ει', 'ομεν', 'ετε', 'ουσι(ν)']
fut_mid_ind = ['ομαι', 'ῃ', 'εται', 'όμεθα', 'εσθε', 'ονται']

impf_act_ind = ['ον', 'ες', 'ε(ν)', 'ομεν', 'ετε', 'ον']
impf_act_ind_epsilon_contract = ['οῦν', 'εις', 'ει', 'οῦμεν', 'εῖτε', 'ουν']
impf_act_ind_alpha_contract = ['ων', 'ας', 'α', 'ῶμεν', 'ᾶτε', 'ων']
impf_act_ind_omicron_contract = ['ουν', 'ους', 'ου', 'οῦμεν', 'οῦτε', 'ουν']

impf_mp_ind = ['όμην','ου','ετο','όμεθα','εσθε','οντο']
impf_mp_ind_epsilon_contract = ['ούμην','οῦ','εῖτο','ούμεθα','εῖσθε','οῦντο']
impf_mp_ind_alpha_contract = ['ώμην','ῶ','ᾶτο','ώμεθα','ᾶσθε','ῶντο']
impf_mp_ind_omicron_contract = ['ούμην','οῦ','οῦτο','ούμεθα','οῦσθε','οῦντο']

aor2_act_ind = ['ον', 'ες', 'ε(ν)', 'ομεν', 'ετε', 'ον']
aor2_mid_ind = ['όμην','ου','ετο','όμεθα','εσθε','οντο']

aor1_act_ind = ['α', 'ας', 'ε(ν)', 'αμεν', 'ατε', 'αν']
aor1_mid_ind = ['άμην','ω','ατο','άμεθα','ασθε','αντο']

pf_act_ind = ['α', 'ας', 'ε(ν)', 'αμεν', 'ατε', 'ασι(ν)']

pf_mp_ind = ['μαι', 'σαι', 'ται', 'μεθα', 'σθε', 'νται']
pf_mp_ind_labial = ['μμαι', 'ψαι', 'πται', 'μμεθα', 'φθε', '(part + εἰσι(ν))']
pf_mp_ind_palatal = ['γμαι', 'ξαι', 'κται', 'γμεθα', 'χθε', '(part + εἰσι(ν))']
pf_mp_ind_dental = ['σμαι', 'σαι', 'σται', 'σμεθα', 'σθε', '(part + εἰσι(ν))']

plupf_act_ind = ['η', 'ης', 'ει(ν)', 'εμεν', 'ετε', 'εσαν']

plupf_mp_ind = ['μην', 'σο', 'το', 'μεθα', 'σθε', 'ντο']
plupf_mp_ind_labial = ['μμην', 'ψο', 'πτο', 'μμεθα', 'φθε', '(part + ἦσαν)']
plupf_mp_ind_palatal = ['γμην', 'ξο', 'κτο', 'γμεθα', 'χθε', '(part + ἦσαν)']
plupf_mp_ind_dental = ['σμην', 'σο', 'στο', 'σμεθα', 'σθε', '(part + ἦσαν)']

aor_pass_ind = ['ην', 'ης', 'η', 'ημεν', 'ητε', 'ησαν']
fut_pass_ind = ['ήσομαι', 'ήσῃ/ήσει', 'ήσεται', 'ησόμεθα', 'ήσεσθε', 'ήσονται']

def simple_conjugate(stem, ending_list):

	finished_list = []

	for ending in ending_list:

		verb = stem + ending
		finished_list.append(verb)

	return finished_list

outfile = open('verb_paradigms.py', mode='w')
outfile.write(str(simple_conjugate('ἠγαγ', aor2_act_ind)))
outfile.close()