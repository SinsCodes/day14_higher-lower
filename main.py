
import random
from game_data import data
from art import logo,vs
from replit import clear

def data_transfer(account):
  account_name=account["name"]
  account_description=account["description"]
  account_country=account["country"]
  return (f"{account_name},a {account_description},from {account_country}")

def compare_data(guess,a_follower,b_follower):
  
  if a_follower > b_follower:
    return guess=="a"
  else:
    return guess=="b"
    
  


def game():
  
  
  score=0  
  should_continue=True
  account_b=random.choice(data)
  while should_continue:
    

      # create random profile
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
      account_b=random.choice(data)
   # compare each profile
    
    print(f"compare A {data_transfer(account_a)}")
    print(vs)
    print(f"against B {data_transfer(account_b)}")
    
    guess=input(f"who has more followers?Type 'A'or 'B': ").lower()
    a_follower=account_a["follower_count"]
    b_follower=account_b["follower_count"]
    is_correct=compare_data(guess,a_follower,b_follower)
    clear()
    print(logo)
    if is_correct:
      score+=1
      print(f"you are right! current score{score} ")
      
    else:
      should_continue=False
      print(f"sorry,thats wrong! final score{score}")
      
game()    