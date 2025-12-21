import random
E_health=100
p_health=100
                                        
while True:
    ch=['attack','defend','heal']
    player=(random.choice(ch))
    print(player)
    enemy='attack'
    print(enemy)               
    if E_health < 0 :
        print("Player wins")
        break
    if p_health <0:
        print("Enemy wins")
        break
    if player=="attack":
        p_score=random.randint(10,30)
        E_health-=p_score
        print(f'player:-{p_health}\n enemy:-{E_health}')
    elif  player=='defend' :
                     enemy_damage=random.randint(10,35)
                     e_score=enemy_damage//2
                     p_health-=e_score
                     print(f'{p_health},{e_score}')
    elif player=="heal":  
                    p_score=random.randint(10,25) 
                    p_health+=p_score
                    if  p_health >100:
                            p_health=100
                    enemy_damage = random.randint(10,35)
                    p_health -= enemy_damage
                    print(f'player:-{p_health}\n enemy:-{E_health}')   
                                                   
    else:
                        print("Restart again")



     

      