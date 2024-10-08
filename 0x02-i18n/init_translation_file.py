# # Extract translatable strings into a .pot file
# $ pybabel extract -F babel.cfg -o messages.pot .

# # Initialize the English translation file
# $ pybabel init -i messages.pot -d translations -l en

# # Initialize the French translation file
# $ pybabel init -i messages.pot -d translations -l fr

# # Compile the translations using
# $ pybabel compile -d translations

# T < L < I < G
# T - t9n: translation (rendering text/speech from one human language to another) convert language
# L - l10n: localization (user experience of a product natively for a specific locale)
# I - i18n: internationalization (a product use case for international markets)
# G - g11n: globalization (creating a product for a global customer base) express multi-lingually
