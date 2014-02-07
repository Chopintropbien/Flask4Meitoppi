__author__ = 'andrei'

from sqlalchemy.orm import sessionmaker
from Datamodel import engine,User

Session = sessionmaker(bind=engine)
session = Session()


def generate_example_usr(usr_dict):
    ex_usr = User(prenom=usr_dict['prenom'],
                  nom=usr_dict['nom'],
                  alias=usr_dict['alias'],
                  n_amis=usr_dict['n_amis'],
                  n_avis=usr_dict['n_avis'],
                  n_suiveurs=usr_dict['n_suiveurs']
                    )
    session.add(ex_usr)


