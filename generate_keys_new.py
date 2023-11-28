# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:29:19 2023

@author: arshy
"""
import yaml
from yaml.loader import SafeLoader
credentials:
  usernames:
    jsmith:
      email: jsmith@gmail.com
      name: John Smith
      password: 
    rbriggs:
      email: rbriggs@gmail.com
      name: Rebecca Briggs
      password: 
cookie:
  expiry_days: 30
  key: some_signature_key # Must be string
  name: some_cookie_name
preauthorized:
  emails:
  - melsby@gmail.com
  
  
  hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
  
  
  

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'sidebar')