__author__ = 'andrei'

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:////:memory:', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # hmmm, is this secure?

    id = Column(Integer, primary_key=True)
    prenom = Column(String)
    nom = Column(String)
    alias = Column(String)
    photo = Column(String)
    n_amis = Column(Integer)
    n_avis = Column(Integer)
    n_suiveurs = Column(Integer)
    #TODO: add a list that can manage user preferences

    def __repr__(self):
        return "<User(name='%s' '%s', alias='%s', amis='%s', avis='%s', suiveurs='%s')>" % (
            self.prenom, self.nom, self.alias, self.n_amis, self.n_avis, self.n_suiveurs)


Base.metadata.create_all(engine)