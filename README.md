# 3710_Project

## How to setup

Create virtual env

- `python -m venv .venv`

Activate env (Must do everytime you open new terminal)

- `.venv\Scripts\activate` (CMD)
- `.\.venv\Scripts\Activate.ps1` (Powershell)
- `source .venv/bin/activate` (mac)

Install all requirements in requirements.txt

- `pip install -r requirements.txt`

Run to update requirements.txt with new inputs

- `pip freeze > requirements.txt`

## How to determine first 3 moves

The simplest way to do it is to add 3 bits for the 3 first moves. The strategy will apply these 3 actions for the 3 first moves independently of what the opponent do. You could chose these 3 values randomly or select them yourself or even allow the optimization process to update them to find the 'best 3 first moves'.

#### The strategy will apply these 3 actions for the 3 first moves independently of what the opponent do

- Chose these 3 values randomly
- Select them yourself
- Allow the optimization process to update them to find the 'best 3 first moves'

#### What we are going to do (Just a first draft)

- The first three values in the array will work independantly of the other player. Then the move list will follow after
