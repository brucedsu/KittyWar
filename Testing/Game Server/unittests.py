import unittest

from match import Match, Ability, Chance, Player, Phases, Moves,active_map, passive_map
from network import Network, Flags


class TestServerMethods(unittest.TestCase):

    """
        --------
        SPRINT 1
        --------
    """

    def test_body_int(self):

        byte = '\x00'
        byte = Network.byte_int(byte)
        self.assertEqual(byte, 0)

    """
        --------
        SPRINT 2
        --------
    """

    """
        --------
        SPRINT 3
        --------
    """

    # Set up player with two cats
    def setUp(self):

        cats = [0, 1]
        self.player1 = Player("Moosey", None, cats)
        self.player2 = Player("Bruce", None, cats)

        self.match = Match()
        self.match.player1 = self.player1
        self.match.player2 = self.player2

    def test_int_3byte(self):

        ba = Network.int_3byte(Flags.ERROR)
        ba.append(Flags.ERROR)
        self.assertEqual(str(ba), "bytearray(b'\\x00\\x00\\x03\\x03')")

    # Test player cat property
    def test_player_cat(self):

        self.player1.cat = 0
        self.assertEqual(self.player1.cat, 0)
        self.assertEqual(self.player1.health, 8)
        self.assertIsNotNone(self.player1.cat)
        self.assertNotEqual(self.player1.health, 0)
        self.assertTrue(self.player1.cat is not None)

    # Test player chance_card property
    def test_player_chance(self):

        chance_card = self.player1.chance_card
        self.assertIsNone(chance_card)

        self.player1.chance_cards.append(0)
        chance_card = self.player1.chance_card
        self.assertEqual(chance_card, 0)

        self.player1.chance_cards.append(1)
        chance_card = self.player1.chance_card
        self.assertEqual(chance_card, 1)

    # Test transition between phases
    def test_phase_transition(self):

        # Check both players arent ready at the start
        self.assertFalse(self.player1.ready)
        self.assertFalse(self.player2.ready)

        # Set each player to ready and check
        players_ready = self.match.player_ready(self.player1)
        self.assertFalse(players_ready)
        self.assertTrue(self.player1.ready)

        players_ready = self.match.player_ready(self.player2)
        self.assertTrue(players_ready)
        self.assertTrue(self.player2.ready)

        # Prepare to test whether phase is changed or not
        self.assertEqual(self.match.phase, Phases.SETUP)

        next_phase = Phases.PRELUDE
        self.match.next_phase(next_phase)
        self.assertEqual(self.match.phase, next_phase)

        # Check that the players ready status were reset
        self.assertFalse(self.player1.ready)
        self.assertFalse(self.player2.ready)

    # Test match select_cat function
    def test_select_cat(self):

        # Check non existent cat
        valid_cat = Match.select_cat(self.player1, 3)
        self.assertFalse(valid_cat)

        # Check existent cat and health for assigned cat
        valid_cat = Match.select_cat(self.player1, 1)
        self.assertTrue(valid_cat)
        self.assertEqual(self.player1.health, 10)

        # Add a cat and check if still working
        self.player1.cats.append(2)
        valid_cat = Match.select_cat(self.player1, 2)
        self.assertTrue(valid_cat)
        self.assertEqual(self.player1.cat, 2)
        self.assertEqual(self.player1.health, 12)

    # Test match select_move function
    def test_select_move(self):

        # Confirm no move exists at the start
        self.assertIsNone(self.player1.move)
        self.assertIsNone(self.player2.move)

        # Select two moves for the two players
        self.match.select_move(self.player1, Moves.PURR)
        self.match.select_move(self.player2, Moves.GUARD)

        # Confirm the moves were actually selected
        self.assertEqual(self.player1.move, Moves.PURR)
        self.assertEqual(self.player2.move, Moves.GUARD)

    # Test Chance random_chances function
    def test_random_chances(self):

        self.assertEqual(len(self.player1.chance_cards), 0)
        Chance.random_chances(self.player1)
        self.assertEqual(len(self.player1.chance_cards), 2)

    # Test Chance has_chance function
    def test_has_chance(self):

        has_chance = Chance.has_chance(self.player1, 4)
        self.assertFalse(has_chance)

        self.player1.chance_cards.append(4)
        has_chance = Chance.has_chance(self.player1, 4)
        self.assertTrue(has_chance)

    # Test ability on_cooldown function
    def test_on_cooldown(self):

        # Check ability not on cooldown
        ability_id = 999
        cooldown = Ability.on_cooldown(self.player1, ability_id)
        self.assertFalse(cooldown)

        # Check ability on cooldown
        self.player1.cooldowns.append((ability_id, 2))
        cooldown = Ability.on_cooldown(self.player1, ability_id)
        self.assertTrue(cooldown)

    # Test ability random_ability function
    def test_random_ability(self):

        self.assertEqual(self.player1.rability, 0)
        Ability.random_ability(self.player1)
        self.assertIsNot(self.player1.rability, 0)

    # Test ability 00 Rejuvenation
    def test_ability00(self):

        correct_phase = Phases.POSTLUDE
        wrong_phase = Phases.PRELUDE

        ability_used = active_map[0](wrong_phase, self.player1)
        self.assertFalse(ability_used)

        ability_used = Ability.a_ability00(wrong_phase, self.player1)
        self.assertFalse(ability_used)

        ability_used = Ability.a_ability00(correct_phase, self.player1)
        self.assertTrue(ability_used)
        self.assertEqual(self.player1.health, 1)

    # Test ability 01 Gentleman
    def test_ability01(self):

        correct_phase = Phases.POSTLUDE
        wrong_phase = Phases.PRELUDE

        ability_used = passive_map[1](wrong_phase, self.player1)
        self.assertFalse(ability_used)

        ability_used = Ability.p_ability01(wrong_phase, self.player1)
        self.assertFalse(ability_used)

        ability_used = Ability.p_ability01(correct_phase, self.player1)
        self.assertFalse(ability_used)

        self.player1.ddodged = 2
        ability_used = Ability.p_ability01(correct_phase, self.player1)
        self.assertTrue(ability_used)
        self.assertEqual(len(self.player1.chance_cards), 1)

    # Test ability 06 Attacker
    def test_ability06(self):

        correct_phase = Phases.POSTLUDE
        wrong_phase = Phases.PRELUDE

        ability_used = Ability.p_ability06(wrong_phase, self.player1)
        self.assertFalse(ability_used)

        ability_used = Ability.p_ability06(correct_phase, self.player1)
        self.assertFalse(ability_used)

        self.player1.ddealt = 2
        ability_used = Ability.p_ability06(correct_phase, self.player1)
        self.assertTrue(ability_used)
        self.assertEqual(len(self.player1.chance_cards), 1)

    # Test ability 07 Critical
    def test_ability07(self):

        correct_phase = Phases.PRELUDE
        wrong_phase = Phases.POSTLUDE

        ability_used = Ability.a_ability07(wrong_phase, self.player1)
        self.assertFalse(ability_used)

        ability_used = Ability.a_ability07(correct_phase, self.player1)
        self.assertTrue(ability_used)

        self.assertEqual(self.player1.modifier, 2)
        self.assertEqual(len(self.player1.cooldowns), 1)


if __name__ == '__main__':
    unittest.main()
