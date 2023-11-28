# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:36:28 2023

@author: arshy
"""

import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Aditi", "Aryan"]
usernames = ["aditi", "aryan"]
passwords = ["abc123", "def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)