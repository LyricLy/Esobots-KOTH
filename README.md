# Esobots-KOTH
A controller for a KOTH game.

## Rules
We have a grid of different objects, called the map.
Turns will repeat until only a single Player is left. That Player is deemed the winner.

## Objects

### Empty
This does nothing.

### Projectile
Has a single attribute, the direction.
Moves in the direction every turn. If it hits a Player, the Projectile will change into a Signal and then bounce, that Player's on_hit method will be called and that Player will lose one HP.

If a Projectile tries to move into the same tile as another projectile, both projectiles will be destroyed.
If a Projectile moves into a wall, it will be destroyed.

### Signal
Has two attributes, its direction and whether it has bounced yet.
Moves in the direction every turn. If it hits a Player and has bounced at least once, the Signal will be destroyed and that Player's on_signal method will be called.

If a Signal tries to move into a wall or Projectile, or if it hits a Player and has not bounced yet, it changes direction and goes in the opposite direction instead.

### Player
Has one attribute, its health.
Has six methods, move, shoot_projectile, send_signal, on_turn, on_signal and on_hit.

on_signal and on_hit are called by Signal and Projectile.
on_turn is called after Signal and Projectile's turns have been evaluated, in a random order between all Players.

All Players are distributed onto the map at the beginning.

If a Player's health value reaches 0, it will die.

### Wall
A possible object that would be distributed onto the map at random.

If a description for another object says "wall", it means "either Wall or the edge of the map".