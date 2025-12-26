"""

decision:
    player makes decision - fight, item, run:

    if fight:
        fastest fighter attacks first
        slower fighter attacks
        back to decision

    if item:
        player selects item:
            if weapon or armour:
                player makes decision - switch, drop, view:
                    if view:
                        selected item viewed
                        return to decision
                    if switch:
                        selected item swaps with current weapon/armour
                        if current weapon is fists, fists deleted from inv
                    if drop:
                        selected item removed
                    enemy attacks

            if potion:
                player decides - use, view:
                    (view is same as before)

                    if use:
                        player can use 1 potion as long as it isnt on cooldown
                        potion goes on cooldown
                        enemy attacks

    if run:
        using speed and chances, determine if player can run
        if not enemy attacks








"""