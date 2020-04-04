# Double_spending_attack_simulator
Allows you to visualize the profitability of a double-spend attack on the Bitcoin network, I also deployed this code on a web server (I used Django) :

https://doublespendingattack.herokuapp.com/doubleSpendingAttack_app/simulateAttack/

To start this program just run the GUI.py file

SatoshiAttach.py :

	function simulateSatoshiAttack : Simulates a double-spend attack for the parameters provided

	function calculateRevenueRatioForListOfHashrates : Simulates a double-spend attack for a list of relative hashrates. Relative hasrates range from 1 to 49, because it is assumed that the attacker has less than half the hashing power of the Bitcoin network


GUI.py : graphical console that allows the user to change attack parameters and see the impact on the profitability of the attack

![Alt text](screenshot/GUI.png?raw=true "GUI screenshot")



