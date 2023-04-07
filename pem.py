#!/usr/bin/python3
from ic.identity import Identity
from ic.client import Client
from ic.agent import Agent
from environment import PEM_FILE, CLIENT_NET

with open(PEM_FILE, 'rb') as f:
    pem = f.read()

identity = Identity.from_pem(pem)
client = Client(url = CLIENT_NET)
agent = Agent(identity, client)
