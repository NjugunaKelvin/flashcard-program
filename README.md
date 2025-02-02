# Learn French Flashcards

This project is a simple flashcard application to help users learn French vocabulary. It uses the 

tkinter library for the GUI and 

pandas for data manipulation.

## Features

- Displays French words and their English translations.
- Allows users to mark words as known.
- Saves progress to a CSV file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/learn-french-flashcards.git
    cd learn-french-flashcards
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install pandas
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. The application window will open, displaying a French word.

3. Click the "✓" button if you know the word, or the "✗" button if you don't.

4. The application will automatically save your progress to `words_to_learn.csv`.

## File Structure
main.py
: The main application script.

data.csv
: The initial dataset of French and English words.

images
: Folder containing images used in the application.

.gitignore
: Specifies files and directories to be ignored by Git.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- The tkinter library for the GUI.
- The pandas library for data manipulation.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
