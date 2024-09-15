# Coffee Machine Simulator ☕️

A simple Python-based coffee machine simulator that allows users to select their desired coffee from **Espresso**, **Latte**, and **Cappuccino**. This project simulates the process of making coffee, deducting ingredients, collecting payments, and providing change.

## Features

- **Menu Options**: Choose between Espresso, Latte, and Cappuccino.<br>
- **Ingredient Management**: Checks if enough ingredients are available to make the selected drink.<br>
- **Coin-Based Payment System**: Accepts quarters, dimes, nickels, and pennies for payment.<br>
- **Automated Change Calculation**: Provides change if the user pays more than the cost of the coffee.<br>
- **Real-Time Reporting**: Displays the current status of water, milk, coffee, and money collected.<br>
- **Simple User Interface**: Command-line interface to interact with the coffee machine.<br>

## Menu & Prices

- **Espresso**: $1.50<br>
- **Latte**: $2.50<br>
- **Cappuccino**: $3.00<br>

## How It Works

1. The user selects a coffee from the menu.<br>
2. The machine checks if enough resources (water, milk, coffee) are available.<br>
3. If sufficient resources are available, the user is prompted to insert coins.<br>
4. The machine calculates if the inserted amount is enough:
    - If the amount is insufficient, the money is refunded.<br>
    - If the amount is exact or more, the coffee is served, and change is provided if necessary.<br>
5. The machine deducts the used ingredients and updates the money earned.<br>



## Project Structure

- `coffee_machine.py`: Main program logic for the coffee machine simulator.<br>
- `art.py`: Contains ASCII art for the coffee machine and drink illustrations (espresso, latte, cappuccino).<br>

## Future Improvements

- Add more coffee types (e.g., Mocha, Americano).<br>
- Implement a graphical user interface (GUI).<br>
- Include options for customizing coffee (e.g., sugar levels, milk options).<br>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.<br>



