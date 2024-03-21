class Character {
    constructor(name, health, attack, defense, speed) {
        this.name = name;
        this.health = health;
        this.attack = attack;
        this.defense = defense;
        this.speed = speed;
    }

    attackOpponent(opponent) {
        if (this.speed >= opponent.speed) {
            const damageDealt = Math.max(0, this.attack - opponent.defense);
            opponent.health -= damageDealt;
            updateBattleLog(`${this.name} attacks ${opponent.name} for ${damageDealt} damage!`);

            if (opponent.health <= 0) {
                updateBattleLog(`${opponent.name} has been defeated!`);
            }
        } else {
            updateBattleLog(`${opponent.name} is too quick and dodges the attack`);
        }
    }
}