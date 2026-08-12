class CombatManager:
    
     # Meccaniche di combattimento
    
    def attack(self, attacker, defender):
        damage = attacker.attack - defender.defense
        
        if damage < 0: damage = 0
        
        defender.hp -= damage
        
        self.update_battle(attacker, defender, damage)

        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")
    
    def escape(self, player, enemy):
        if player.speed > enemy.speed:
            print(f"{player.name} escaped from the battle")
            return True
        else:
            print(f"{player.name} failed to escape from the battle")
            return False
    
    
    def determine_turn_order(self, player, enemy):
        if player.speed >= enemy.speed:
            return player, enemy
        else:
            return enemy, player
    
    def update_battle(self, attacker, defender, damage):
        print(f"{attacker.name} attacks {defender.name}!")
        print(f"{defender.name} takes {damage} damage.")
        
