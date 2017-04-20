
classes =  { 'Novice':set(['Fighter','Hunter','SpellCaster']),
             
             'Fighter':set(['Warrior']),
             'Warrior':set(['Fighter','Berserker','Paladins']),
             'Berserker':set(['Warrior','Warlord']),
             'Paladins':set(['Warrior','Templar',]),
             'Warlord':set(['Berserker']),
             'Templar':set(['Paladins']),
             
             'Hunter':set(['Archer']),
             'Archer':set(['Hunter','Ranger','Assasin']),
             'Ranger':set(['Archer','Sharpshooter']),
             'Assasin':set(['Archer','Darkstalker']),
             'Darkstalker':set(['Assasin']),
             'SharpShooter':set(['Ranger']),
             
             'SpellCaster':set(['Mage']),
             'Mage':set(['SpellCaster','Necromancer','Wizard']),
             'Necromancer':set(['Mage','Demonologist']),
             'Wizard':set(['Mage','Archmages']),
             'Archmages':set(['Wizard']),
             'Demonologist':set(['Necromancer'])
         }

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
     
        jalur = queue.pop(0)

       
        state = jalur[-1]

      
        if state == tujuan:
            return jalur
    
        elif state not in visited:
           
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang)
                queue.append(jalur_baru)

          
            visited.add(state)

     
        isi = len(queue)
        if isi == 0:
            print("Mapping tidak ditemukan karena Classes Berbeda")


