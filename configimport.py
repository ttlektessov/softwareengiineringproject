from configparser import ConfigParser

config = ConfigParser()
file = 'config.ini'
config.read(file)
token = config['TOKEN']['tokens']

# importing links from config
kakao = config['rus_links']['kakao']
naver = config['rus_links']['naver']
press_r = config['rus_links']['presslink_r']
google = config['rus_links']['google']

#importing links for consul
C_registration_l = config['rus_links']['Consul_registration_link']
Presidence_link_r = config['rus_links']['Presidence_docs_link_r']
Presidence_link_q_r = config['rus_links']['Presidence_docs_link_q_r']
D_back_l_r = config['rus_links']['Docs_back_link_r']
D_back_l_q_r = config['rus_links']['Docs_back_questionnaire_link_r']
C_lost_l_r = config['rus_links']['Clost_docs_link_r']
D_passport_l_r = config['rus_links']['Documents_pass_link_r']
C_out_l_r = config['rus_links']['Citizenship_out_link_r']
C_fee_l_r = config['rus_links']['Consul_fee_link_r']
R_marriage_l_r = config['rus_links']['Registration_marriage_link_r']
R_divorce_l_r = config['rus_links']['Registration_divorce_link_r']
R_birth_l_r = config['rus_links']['Registration_birth_link_r']
R_death_l_r = config['rus_links']['Registration_death_link_r']
R_paternity_l_r = config['rus_links']['Registration_paternity_link_r']
R_lostcit_l_r = config['rus_links']['Registration_lostcit_link_r']
Apostille_link_r = config['rus_links']['Apostille_fee_link_r']
Notary_fee_l_r = config['rus_links']['Notary_fee_link_r']
Documents_reclamation_l_r = config['rus_links']['Documents_reclamation_link_r']

press_k = config['kaz_links']['presslink_k']
Presidence_link1_k = config['kaz_links']['Presidence_docs_link1_k']
Presidence_link2_k = config['kaz_links']['Presidence_docs_link2_k']
D_back_l_k = config['kaz_links']['Docs_back_link_k']
C_lost_l_k = config['kaz_links']['Clost_docs_link_k']
D_passport_l_k = config['kaz_links']['Documents_pass_link_k']
C_out_l_k = config['kaz_links']['Citizenship_out_link_k']
C_fee_l_k = config['kaz_links']['Consul_fee_link_k']
R_marriage_l_k = config['kaz_links']['Registration_marriage_link_k']
R_divorce_l_k = config['kaz_links']['Registration_divorce_link_k']
R_birth_l_k = config['kaz_links']['Registration_birth_link_k']
R_death_l_k = config['kaz_links']['Registration_death_link_k']
R_paternity_l_k = config['kaz_links']['Registration_paternity_link_k']
R_lostcit_l_k = config['kaz_links']['Registration_lostcit_link_k']
Apostille_link_k = config['kaz_links']['Apostille_fee_link_k']
Notary_fee_l_k = config['kaz_links']['Notary_fee_link_k']
Documents_reclamation_l_k = config['kaz_links']['Documents_reclamation_link_k']

Visa_info_link_e = config['eng_links']['Visa_info_e']
Visa_form_link_e = config['eng_links']['Visa_form_e']
Visa_regulations_link_e = config['eng_links']['Visa_regulations_e']

Visa_info_link_kor = config['kor_links']['Visa_info_kor']
Visa_states_link_kor = config['kor_links']['Visa_states_kor']
Visa_regulations_link_kor = config['kor_links']['Visa_regulations_kor']